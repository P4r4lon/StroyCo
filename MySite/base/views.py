from django.shortcuts import render, get_object_or_404, redirect
from .models import Deal, Apartment, Invoice, CounterAgent, Employer
from .forms import DealForm, ApartmentForm, InvoiceForm, EmployerForm, CounterAgentForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.db.models import Avg, Max

# Create your views here.

def index(request):
    return render(request, 'base/index.html')


# ___deals___
def deals(request):
    deal = Deal.objects.all()
    return render(request, 'base/deals.html', {'deals': deal})


def deals_create(request):
    return Create(request, DealForm, 'deals')


class deals_detail(DetailView):
    model = Deal
    template_name = 'base/deals_detail.html'
    context_object_name = 'd'


class deals_update(UpdateView):
    model = Deal
    template_name = 'base/create.html'
    form_class = DealForm


class deals_delete(DeleteView):
    model = Deal
    context_object_name = 'deal'
    success_url = '/deals'
    template_name = 'base/delete.html'


# ___counteragents___
def counteragents(request):
    counteragent = CounterAgent.objects.all()
    return render(request, 'base/counteragents.html', {'counteragents': counteragent})


def counteragents_create(request):
    return Create(request, CounterAgentForm, 'counteragents')

class counteragents_detail(DetailView):
    model = CounterAgent
    template_name = 'base/counteragents_detail.html'
    context_object_name = 'd'


class counteragents_update(UpdateView):
    model = CounterAgent
    template_name = 'base/create.html'
    form_class = CounterAgentForm


class counteragents_delete(DeleteView):
    model = CounterAgent
    context_object_name = 'ca'
    success_url = '/counteragents'
    template_name = 'base/delete.html'

# ___employers___
def employers(request):
    employer = Employer.objects.all()

    if employer:
        max_deals = Employer.objects.all().aggregate(Max('quantityOfDeals'))['quantityOfDeals__max']
        bestman = Employer.objects.filter(quantityOfDeals=max_deals)
        return render(request, 'base/employers.html', {'employers': employer, 'bestman': bestman})
    else:
        return render(request, 'base/employers.html', {'employers': employer, 'bestman': ""})

class employers_detail(DetailView):
    model = Employer
    template_name = 'base/employers_detail.html'
    context_object_name = 'd'


class employers_update(UpdateView):
    model = Employer
    template_name = 'base/create.html'
    form_class = EmployerForm

class employers_delete(DeleteView):
    model = Employer
    context_object_name = 'em'
    success_url = '/employers'
    template_name = 'base/delete.html'

def employers_create(request):
    return Create(request, EmployerForm, 'employers')


# __apartments__
def apartments(request, filter):
    apartment = Apartment.objects.order_by(filter)
    avg = 0
    if apartment:
        avg = Apartment.objects.all().aggregate(Avg('price'))
        avg = round(avg['price__avg'])
    if 'search' in request.GET:
        search = request.GET['search']
        if search:
            nord = Apartment.objects.filter(Q(address__icontains=search) | Q(status__icontains=search))
            return render(request, 'base/apartments.html', {'apartments': nord, 'search': search})
    return render(request, 'base/apartments.html', {'apartments': apartment, 'avg': avg})

class apartments_detail(DetailView):
    model = Apartment
    template_name = 'base/apartments_detail.html'
    context_object_name = 'd'

class apartments_update(UpdateView):
    model = Apartment
    template_name = 'base/create.html'
    form_class = ApartmentForm

class apartments_delete(DeleteView):
    model = Apartment
    context_object_name = 'ap'
    success_url = '/apartments_search/-price'
    template_name = 'base/delete.html'

def apartments_create(request):
    error = ''
    if request.method == 'POST':
        form = ApartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('apartments', filter='-price')
        else:
            error = 'Неверная форма'
    form = ApartmentForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'base/create.html', data)


# __invoices__
def invoices(request):
    invoice = Invoice.objects.all()
    return render(request, 'base/invoices.html', {'invoices': invoice})


class invoices_detail(DetailView):
    model = Invoice
    template_name = 'base/invoices_detail.html'
    context_object_name = 'd'

class invoices_update(UpdateView):
    model = Invoice
    template_name = 'base/create.html'
    form_class = InvoiceForm

class invoices_delete(DeleteView):
    model = Invoice
    context_object_name = 'in'
    success_url = '/invoices'
    template_name = 'base/delete.html'

def invoices_create(request):
    return Create(request, InvoiceForm, 'invoices')


# __creator__
def Create(request, myform, redirector):
    error = ''
    if request.method == 'POST':
        form = myform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(redirector)
        else:
            error = 'Неверная форма'
    form = myform()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'base/create.html', data)


def clients(request):
    return render(request, 'base/clients.html')
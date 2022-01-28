from django.contrib import admin
from .models import Deal, Apartment, Invoice, CounterAgent, Employer

admin.site.register(Deal)
admin.site.register(Apartment)
admin.site.register(Invoice)
admin.site.register(CounterAgent)
admin.site.register(Employer)


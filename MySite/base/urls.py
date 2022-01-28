"""MySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name="home"),


    path('deals', login_required(views.deals), name="deals"),
    path('deals_create', views.deals_create, name="deals_create"),
    path('deals/<int:pk>', views.deals_detail.as_view(), name="deals_detail"),
    path('deals/<int:pk>/update', views.deals_update.as_view(), name="deals_update"),
    path('deals/<int:pk>/delete/', views.deals_delete.as_view(), name="deals_delete"),

    path('counteragents', login_required(views.counteragents), name="counteragents"),
    path('counteragents_create', views.counteragents_create, name="counteragents_create"),
    path('counteragents/<int:pk>', views.counteragents_detail.as_view(), name="counteragents_detail"),
    path('counteragents/<int:pk>/update', views.counteragents_update.as_view(), name="counteragents_update"),
    path('counteragents/<int:pk>/delete/', views.counteragents_delete.as_view(), name="counteragents_delete"),

    path('employers', views.employers, name="employers"),
    path('employers_create', views.employers_create, name="employers_create"),
    path('employers/<int:pk>', views.employers_detail.as_view(), name="employers_detail"),
    path('employers/<int:pk>/update', views.employers_update.as_view(), name="employers_update"),
    path('employers/<int:pk>/delete/', views.employers_delete.as_view(), name="employers_delete"),

    path('apartments_search/<slug:filter>', views.apartments, name="apartments"),
    path('apartments_create', views.apartments_create, name="apartments_create"),
    path('apartments/<int:pk>', views.apartments_detail.as_view(), name="apartments_detail"),
    path('apartments/<int:pk>/update', views.apartments_update.as_view(), name="apartments_update"),
    path('apartments/<int:pk>/delete/', views.apartments_delete.as_view(), name="apartments_delete"),

    path('invoices', login_required(views.invoices), name="invoices"),
    path('invoices_create', views.invoices_create, name="invoices_create"),
    path('invoices/<int:pk>', views.invoices_detail.as_view(), name="invoices_detail"),
    path('invoices/<int:pk>/update', views.invoices_update.as_view(), name="invoices_update"),
    path('invoices/<int:pk>/delete/', views.invoices_delete.as_view(), name="invoices_delete"),

    path('clients', views.clients, name="clients"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

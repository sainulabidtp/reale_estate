# property_management/urls.py

from django.urls import path
from .views import (
    property_list, property_detail, add_property, add_unit, unit_detail,
    add_rental_info, add_tenant, assign_tenant, edit_tenant_profile, tenant_profile, search_properties,TenantCreateView, TenantListView
)
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('tenants/', TenantListView.as_view(), name='tenant_list'),
    path('create_profile/', TenantCreateView.as_view(), name='tenant_create'),
    path('tenants/<int:tenant_id>/edit/', edit_tenant_profile, name='edit_tenant_profile'),

    # Add other URLs as needed
    path('', property_list, name='property_list'),
    path('properties/add/', add_property, name='add_property'),
    path('properties/<int:property_id>/', property_detail, name='property_detail'),
    path('properties/<int:property_id>/add_unit/', add_unit, name='add_unit'),
    path('properties/<int:property_id>/units/<int:unit_id>/', unit_detail, name='unit_detail'),
    path('properties/<int:property_id>/units/<int:unit_id>/add_rental_info/', add_rental_info, name='add_rental_info'),
    path('properties/<int:property_id>/units/<int:unit_id>/assign_tenant/', assign_tenant, name='assign_tenant'),
    path('properties/<int:property_id>/units/<int:unit_id>/add_tenant/', add_tenant, name='add_tenant'),
    path('tenants/<int:tenant_id>/', tenant_profile, name='tenant_profile'),
    path('search/', search_properties, name='search_properties'),

]

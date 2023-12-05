from .models import Property, Unit, Tenant, RentalInformation
from .forms import PropertyForm, UnitForm, TenantForm, RentalInformationForm
from django.contrib import messages,auth
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.db.models import Q


class TenantListView(ListView):
    model = Tenant
    template_name = 'tenant_list.html'
    context_object_name = 'tenants'

class TenantCreateView(CreateView):
    model = Tenant
    form_class = TenantForm
    template_name = 'tenant_form.html'
    success_url = reverse_lazy('property_list')

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})

def property_detail(request, property_id):
    property_obj = get_object_or_404(Property, pk=property_id)
    units = Unit.objects.filter(property=property_obj)
    rental_info = RentalInformation.objects.filter(unit__property=property_obj)
    return render(request, 'property_detail.html', {'property': property_obj, 'units': units, 'rental_info': rental_info})

def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'add_property.html', {'form': form})

def add_unit(request, property_id):
    property_obj = get_object_or_404(Property, pk=property_id)
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            unit = form.save(commit=False)
            unit.property = property_obj
            unit.save()
            return redirect('property_detail', property_id=property_id)
    else:
        form = UnitForm()
    return render(request, 'add_unit.html', {'form': form, 'property': property_obj})

def unit_detail(request, property_id, unit_id):
    property_obj = get_object_or_404(Property, pk=property_id)
    unit = get_object_or_404(Unit, pk=unit_id, property=property_obj)
    rental_info = RentalInformation.objects.filter(unit=unit)
    return render(request, 'unit_detail.html', {'property': property_obj, 'unit': unit, 'rental_info': rental_info})

def add_rental_info(request, property_id, unit_id):
    property_obj = get_object_or_404(Property, pk=property_id)
    unit = get_object_or_404(Unit, pk=unit_id, property=property_obj)
    if request.method == 'POST':
        form = RentalInformationForm(request.POST)
        if form.is_valid():
            rental_info = form.save(commit=False)
            rental_info.unit = unit
            rental_info.save()
            return redirect('unit_detail', property_id=property_id, unit_id=unit_id)
    else:
        form = RentalInformationForm()
    return render(request, 'add_rental_info.html', {'form': form, 'property': property_obj, 'unit': unit})

def add_tenant(request, property_id, unit_id):
    property_obj = get_object_or_404(Property, pk=property_id)
    unit = get_object_or_404(Unit, pk=unit_id, property=property_obj)

    if request.method == 'POST':
        form = TenantForm(request.POST)
        if form.is_valid():
            tenant = form.save()
            rental_info = RentalInformation(unit=unit, tenant=tenant)
            rental_info.save()
            return redirect('unit_detail', property_id=property_id, unit_id=unit_id)
    else:
        form = TenantForm()

    return render(request, 'add_tenant.html', {'form': form, 'property': property_obj, 'unit': unit})

def tenant_profile(request, tenant_id):
    tenant = get_object_or_404(Tenant, pk=tenant_id)
    rental_info = RentalInformation.objects.filter(tenant=tenant)
    return render(request, 'tenant_profile.html', {'tenant': tenant, 'rental_info': rental_info})

def edit_tenant_profile(request, tenant_id):
    tenant = get_object_or_404(Tenant, pk=tenant_id)

    if request.method == 'POST':
        form = TenantForm(request.POST, instance=tenant)
        if form.is_valid():
            form.save()
            return redirect('tenant_profile', tenant_id=tenant.id)
    else:
        form = TenantForm(instance=tenant)

    return render(request, 'edit_tenant_profile.html', {'form': form, 'tenant': tenant})
def search_properties(request):
    query = request.GET.get('q')
    if query:
        properties = Property.objects.filter(
            Q(name__icontains=query) |
            Q(location__icontains=query) |
            Q(features__icontains=query)
        ).distinct()
    else:
        properties = Property.objects.all()
    return render(request, 'property_search.html', {'properties': properties, 'query': query})






def assign_tenant(request, property_id, unit_id):
    property_obj = get_object_or_404(Property, pk=property_id)
    unit = get_object_or_404(Unit, pk=unit_id, property=property_obj)

    if request.method == 'POST':
        form = RentalInformationForm(request.POST)
        if form.is_valid():
            rental_info = form.save(commit=False)
            rental_info.unit = unit
            rental_info.save()
            return redirect('unit_detail', property_id=property_id, unit_id=unit_id)
    else:
        form = RentalInformationForm()

    return render(request, 'assign_tenant.html', {'form': form, 'property': property_obj, 'unit': unit})


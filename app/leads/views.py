from django.shortcuts import redirect, render
from .models import *
from .forms import *
from .urls import *


def lead_list(request):

    leads = Lead.objects.all()
    context = {
        "leads": leads
    }

    return render(request, 'leads/lead_list.html', context)


def lead_detail(request, pk):

    lead = Lead.objects.get(pk=pk)
    context = {
        "lead": lead
    }
    return render(request, 'leads/lead_detail.html', context)


def lead_create(request):

    form = LeadModalForm()
    if request.method == "POST":

        form = LeadModalForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('/leads')

    context = {
        "form": form
    }
    return render(request, 'leads/lead_create.html', context)


def lead_update(request, pk):

    lead = Lead.objects.get(pk=pk)
    form = LeadModalForm(instance=lead)
    if request.method == "POST":
        form = LeadModalForm(request.POST, instance=lead)

        if form.is_valid():
            form.save()
            return redirect(f'/leads/{pk}/')

    context = {
        "lead": lead,
        "form": form,
    }
    return render(request, 'leads/lead_update.html', context)

def lead_delete(request, pk):

    lead = Lead.objects.get(pk=pk)
    lead.delete()
    return redirect('/leads')
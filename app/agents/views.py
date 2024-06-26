import random

from django.urls import reverse
from django.views import generic
from django.core.mail import send_mail

from leads.models import Agent
from .forms import AgentModelForm
from .mixins import OrganisorLoginRequiredMixin


class AgentListView(OrganisorLoginRequiredMixin, generic.ListView):
    template_name = 'agents/agent_list.html'

    def get_queryset(self):

        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
    

class AgentCreateView(OrganisorLoginRequiredMixin, generic.CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agent-list')
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organisor = False
        user.set_password(f"{random.randint(0, 1000000)}")
        user.save()
        Agent.objects.create(
            user=user,
            organisation=self.request.user.userprofile
        )
        send_mail(
            subject="You are invited to be an agent",
            message="You were added as an agent on Djsngo CRM. Please come login to start working",
            from_email="admin@admin.com",
            recipient_list=[user.email]
        )
        return super(AgentCreateView, self).form_valid(form)
    

class AgentDetailView(OrganisorLoginRequiredMixin, generic.DetailView):
    template_name = 'agents/agent_detail.html'
    context_object_name = 'agent'
    
    def get_queryset(self):

        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
    

class AgentUpdateView(OrganisorLoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent-list")

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)


class AgentDeleteView(OrganisorLoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"

    def get_success_url(self):
        return reverse("agents:agent-list")
    
    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
    
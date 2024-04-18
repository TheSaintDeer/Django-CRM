from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import *


User = get_user_model()

class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}


class LeadModelForm(forms.ModelForm):
    
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'location',
            'cell_phone',
            'age',
            'agent',
        )


class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())

    def __init__(self, *arg, **kwarg):
        request = kwarg.pop("request")
        agents = Agent.objects.filter(organisation=request.user.userprofile)
        super(AssignAgentForm, self).__init__(*arg, **kwarg)
        self.fields["agent"].queryset = agents


class LeadCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'category',
        )
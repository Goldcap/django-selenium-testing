import hashlib
import datetime

from django import forms
from django.forms.util import ErrorList
from django.contrib.auth.models import User, Group
from django.contrib.auth import logout, login, authenticate
from django.db import IntegrityError
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.forms import USStateField
from django.utils.timezone import now

from selenium_tests.models import *

class UserForm(forms.Form):
    UserName = forms.CharField(max_length=10)

    Password1 = forms.CharField(max_length=10)
    password2 = forms.EmailField(max_length=10)

    def clean(self):
        data = self.cleaned_data
        if "password1" in data and "password2" in data and data["password1"] != data["password2"]:
            raise forms.ValudationError("Passwords must be same")

class LoginForm(forms.Form):
    Email = forms.EmailField()
    Password = forms.CharField(max_length=300)

    def login(self):
        """ use awebers client lib to obtain an authorization url
            limit to one auth record...
        """
        user = authenticate(username=self.data['Email'].strip(), password=self.data['Password'].strip())
        if user:
            self._errors = ErrorList(['Successfully logged in!'])
            return True
        else:
            self._errors = ErrorList(['Login failed !'])
            return False
            
class SignupForm(forms.ModelForm):
    Email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}), required=True,)
    FirstName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}), required=True, error_messages = {'invalid': 'Your First Name is required'})
    LastName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}), required=True)
    Password = forms.CharField(max_length=300)
    user = None
    
    class Meta:
        model = Profile
        fields = ['Email', 'FirstName', 'LastName',]

    def __init__(self, *args, **kw):
        super(SignupForm, self).__init__(*args, **kw)
        self.fields['FirstName'].initial = self.instance.FirstName
        self.fields['LastName'].initial = self.instance.LastName
        
        
    def save(self):
        """
        vendor signup
        """
        try:
            
            self.user = User.objects.create_user(self.data['Email'].strip(), self.data['Email'].strip(), self.data['Password'].strip())
            #self.user.is_active = False
            self.user.save()
            
            rec = Profile()
            
            rec.user = self.user
            rec.FirstName = self.data['FirstName']
            rec.LastName = self.data['LastName']
            rec.DateSubmitted = self.user.date_joined
            #rec.Approved = 1
            
            rec.save()
            
            self._errors = ErrorList(['Successfully submitted!'])
        except:
            self._errors = ErrorList(['Whups, error!'])
            
    def is_valid(self):
        if len(Profile.objects.filter(user__email=self.data['Email'])) > 0:
            self.add_error('Email', 'Email already exists.')
            #self._errors = ErrorList(['Email already exists.'])
            valid = False
        else:
            valid = True
        
        if ((len(self.data['Password']) == 0) or (len(self.data['PasswordConfirm']) == 0) or (self.data['PasswordConfirm'] != self.data['Password'])):
            self.add_error('Password', 'There was a problem with your password, please try again.')
            #self._errors = ErrorList(['There was a problem with your password, please try again.'])
            valid = False
        
        return valid
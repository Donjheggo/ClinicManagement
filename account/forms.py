from django import forms
from .models import *


class FormSettings(forms.ModelForm):
   def __init__(self, *args, **kwargs):
      super(FormSettings, self).__init__(*args, **kwargs)
      for field in self.visible_fields():
         field.field.widget.attrs['class'] = 'form-control form-control-user'


class RegistrationForm(FormSettings):
   def __init__(self, *args, **kwargs):
      super(RegistrationForm, self).__init__(*args, **kwargs)
      if kwargs.get('instance'):
         instance = kwargs.get('instance').__dict__
         self.fields['password'].required = False
         for field in RegistrationForm.Meta.fields:
            self.fields[field].initial = instance.get(field)
         if self.instance.pk is not None:
            self.fields['password'].widget.attrs['placeholder'] = "Fill this only if you wish to update password"
         else:
            self.fields['first_name'].required = True
            self.fields['last_name'].required = True

   def clean_email(self, *args, **kwargs):
      formEmail = self.cleaned_data['email'].lower()

      # domain = formEmail.split('@')[1]
      # domain_list = ["ssct.edu.ph"]
      # if domain not in domain_list:
      #    raise forms.ValidationError("Please enter ssct gsuite email")
      if self.instance.pk is None: 
         if Account.objects.filter(email=formEmail).exists():
               raise forms.ValidationError(
                  "The given email is already registered")
      else:  # Update
         dbEmail = self.Meta.model.objects.get(
               id=self.instance.pk).email.lower()
         if dbEmail != formEmail:  # There has been changes
               if Account.objects.filter(email=formEmail).exists():
                  raise forms.ValidationError(
                     "The given email is already registered")
      return formEmail

   def clean_password(self):
      password = self.cleaned_data.get("password", None)
      if self.instance.pk is not None:
         if not password:
               # return None
               return self.instance.password
      return make_password(password)

   class Meta:
      model = Account
      fields = ['last_name', 'first_name', 'email', 'password', 'user_type', 'birthday', 'address', 'phone_number', 'specialization', 'gender']
      widgets = {
      'last_name':forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder':'Last name' }),
      'first_name':forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder':'First Name' }),
      'password': forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control', 'placeholder':'Password' }),
      'email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control', 'placeholder':'Email' }),
      'user_type': forms.Select(attrs={'class': 'form-control'}),
      'phone_number': forms.TextInput(attrs={'type': 'number', 'class': 'form-control', 'placeholder':'Contact Number' }),
      'specialization': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder':'Specialization (for doctors only)' }),
      'gender': forms.Select(attrs={'class': 'form-control'}),
      'birthday': forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}),
      'address': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder':'Street, Barangay, City' }),
   }


class UpdateProfileForm(FormSettings):
   def __init__(self, *args, **kwargs):
      super(UpdateProfileForm, self).__init__(*args, **kwargs)
      if kwargs.get('instance'):
         instance = kwargs.get('instance').__dict__
         self.fields['password'].required = True
         for field in UpdateProfileForm.Meta.fields:
            self.fields[field].initial = instance.get(field)
         if self.instance.pk is not None:
            self.fields['password'].widget.attrs['placeholder'] = "Fill this only if you wish to update password"
         else:
            self.fields['first_name'].required = True
            self.fields['last_name'].required = True

   def clean_email(self, *args, **kwargs):
      formEmail = self.cleaned_data['email'].lower()

      # domain = formEmail.split('@')[1]
      # domain_list = ["gmail.com"]
      # if domain not in domain_list:
      #    raise forms.ValidationError("Please enter ssct gsuite email")
      if self.instance.pk is None: 
         if Account.objects.filter(email=formEmail).exists():
               raise forms.ValidationError(
                  "The given email is already registered")
      else:  # Update
         dbEmail = self.Meta.model.objects.get(
               id=self.instance.pk).email.lower()
         if dbEmail != formEmail:  # There has been changes
               if Account.objects.filter(email=formEmail).exists():
                  raise forms.ValidationError(
                     "The given email is already registered")
      return formEmail

   def clean_password(self):
      password = self.cleaned_data.get("password", None)
      if self.instance.pk is not None:
         if not password:
               # return None
               return self.instance.password
      return make_password(password)

   class Meta:
      model = Account
      exclude = ['last_name', 'first_name', 'email', 'password', 'user_type', 'birthday', 'address', 'phone_number', 'specialization', 'gender', 'birthday']
      fields = ['password',]
      widgets = {
      'password': forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control', 'placeholder':'Password' }),
   }





class VerificationForm(forms.ModelForm):
   class Meta:
      model = Account
      fields = ['otp']
      exclude = ['last_name', 'first_name', 'email', 'password', 'user_type', 'birthday', 'address', 'phone_number', 'specialization', 'gender', 'birthday']
      widgets = {
         'otp':forms.TextInput(attrs={'type': 'number', 'class': 'form-control', 'placeholder':'OTP' }),
      }
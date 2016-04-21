from django import forms

class UserForm(forms.Form):
  user_name = forms.CharField(required=True,max_length=100)

from django import forms
class imageuploadForms(forms.Form):
    image = forms.ImageField()
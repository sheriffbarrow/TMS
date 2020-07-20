from django import forms
from django.contrib.auth.models import User
from graTMS.models import Complaint


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['user', 'last_modified_by', 'last_modified_by']

    def clean_author(self):
        if not self.cleaned_data['author']:
            return User()
        return self.cleaned_data['author']

    def clean_last_modified_by(self):
        if not self.cleaned_data['last_modified_by']:
            return User()
        return self.cleaned_data['last_modified_by']


class NameForm(forms.Form):
    office_name = forms.CharField(max_length=100)
    room = forms.CharField(max_length=100)
    complaint = forms.CharField(max_length=100)
    solution = forms.CharField(max_length=100)
    status = forms.CharField(max_length=100)
    additional_Info = forms.CharField(max_length=100)
    signature = forms.ImageField(max_length=100)

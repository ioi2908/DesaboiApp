from mainApp.models import UploadNotes
from django import forms


class UploadNotesModelForm(forms.ModelForm):
    class Meta:
        model = UploadNotes
        fields = '__all__'
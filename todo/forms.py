from django import forms
from .models import ToDoListModel
class ToDoforms(forms.ModelForm):
    task_uz = forms.CharField()
    task_en = forms.CharField()
    class Meta:
        model = ToDoListModel
        exclude =['task',]
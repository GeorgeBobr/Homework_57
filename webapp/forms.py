from django import forms
from django.forms import widgets

from webapp.models import Type
from webapp.models import Status

class TypeForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Название")

class StatusForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Название")

class TaskForm(forms.Form):
    summary = forms.CharField(max_length=50, required=True, label="Заголовок")
    description = forms.CharField(max_length=2000, required=False, label="Описание",
                                  widget=widgets.Textarea(attrs={"cols": 30, "rows": 5, "class": "test"}))
    types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), label="Типы")
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label="Статусы")
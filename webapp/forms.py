from django import forms
from django.forms import widgets
from django.core.validators import BaseValidator
from django.core.exceptions import ValidationError

from webapp.models import Type, Status, Project, Task

def validate_summary(value):
    if "bad_word" in value.lower():
        raise ValidationError("Заголовок содержит бранные слова")

def validate_description(value):
    if len(value) < 10:
        raise ValidationError("Описание задачи должно содержать не менее 10 символов")
    elif "bad_word" in value.lower():
        raise ValidationError("Описание не должно содержать бранных слов")

class NoSpecificCharactersValidator(BaseValidator):
    message = "Заголовок не должен содержать определенные символы"
    code = "no_specific_characters"

    def compare(self, value, initial):
        forbidden_characters = ['@', '#', '$', '^']
        return not any(char in forbidden_characters for char in str(value))

def at_least_5_summary(value):
    if len(value) < 5:
        raise ValidationError('Заголовок должен содержать не менее 5 символов')

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'types']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['start_data', 'end_data', 'title', 'description', 'users']

class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')


class TypeForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Название")

class StatusForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Название")


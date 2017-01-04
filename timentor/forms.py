from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm
from django.forms.formsets import BaseFormSet
from .models import ParentTask, ChildTask


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['sex'].widget.attrs['class'] = 'form-control'


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'



class ParentTaskForm(ModelForm):
    class Meta:
        model = ParentTask
        fields = [
            'task_date', 'task_no', 'task_name', 'time', 'time_start', 'time_end', 'time_started', 'time_ended',
        ]


class ChildTaskForm(ModelForm):
    class Meta:
        model = ChildTask
        fields = [
            'task_no', 'task_name', 'time', 'time_start', 'time_end', 'time_started', 'time_ended',
            'classification', 'parent_task'
        ]


class BaseTaskFormSet(BaseFormSet):
    def clean(self):
        """
        Adds validation to check that no two tasks with the same task name are submitted
        :return:
        """
        if any(self.errors):
            return

        task_names = []
        for form in self.forms:
            task_name = form['task_name'].value()
            if task_name in task_names:
                raise forms.ValidationError("Task Name must be unique")
            task_names.append(task_name)
        return self.forms

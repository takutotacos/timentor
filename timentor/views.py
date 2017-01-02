from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import RegisterForm, ParentTaskForm, ChildTaskForm, BaseTaskFormSet
from .models import ChildTask, ParentTask
from django.forms import formset_factory
from django.utils.timezone import datetime
from django.contrib import messages
from django.shortcuts import get_list_or_404, get_object_or_404


class MainView(generic.ListView):
    template_name = 'timentor/main.html'
    context_object_name = 'task_list_for_today'

    # def get_queryset(self):
    #     """Return the tasks for today"""
    #     return ParentTask.objects.filter(task_date__e=)


def new_todo_parent(request):
    ParentTaskFormSet = formset_factory(ParentTaskForm, formset=BaseTaskFormSet)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        formset = ParentTaskFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                cd = form.cleaned_data
                parent_task = ParentTask(task_date=cd['task_date'], task_no=cd['task_no'], task_name=cd['task_name'],
                                         time=cd['time'], time_start_hour=cd['time_start_hour'],
                                         time_start_min=cd['time_start_min'],
                                         time_end_hour=cd['time_end_hour'],
                                         time_end_min=cd['time_end_min'])
                parent_task.save()
            messages.success(request, 'You have created the tasks')
            task_date_string = "".join(parent_task.task_date.split("/"))
            return HttpResponseRedirect(reverse('timentor:list_daily_edit', args=(task_date_string,)))
        else:
            messages.error(request, "You have something wrong with the tasks you made")
            return HttpResponseRedirect(reverse('timentor:new_todo_parent'))
    else:
        formset = ParentTaskFormSet(initial=[
            {'task_date': datetime.now().strftime("%Y/%m/%d")}
        ])
    return render(request, 'timentor/new_todo_parent.html', {'formset': formset})


def new_todo_child(request, task_date, task_no):
    task_date_string = task_date[:4] + "/" + task_date[4:6] + "/" + task_date[6:]
    daily_task_with_task_no = get_object_or_404(ParentTask, task_date=task_date_string, task_no=task_no)
    ChildTaskFormSet = formset_factory(ChildTaskForm, formset=BaseTaskFormSet)
    if request.method == 'POST':
        formset = ChildTaskFormSet(request.POST)
        if formset.is_valid():
            print("The formset is valid")
            for form in formset:
                cd = form.cleaned_data
                child_task = ChildTask(task_no=cd['task_no'], task_name=cd['task_name'], time=cd['time'],
                                       time_start_hour=cd['time_start_hour'], time_start_min=cd['time_start_min'],
                                       time_end_hour=cd['time_end_hour'], time_end_min=cd['time_end_min'],
                                       classification=cd['classification'], parent_task=daily_task_with_task_no)
                child_task.save()
        else:
            print(formset.errors)
    else:
        formset = ChildTaskFormSet(initial=[
            {'parent_task': daily_task_with_task_no.id},
        ])
    return render(request, 'timentor/new_todo_child.html', {
        'formset': formset,
        'parent_task': daily_task_with_task_no,
        })


def list_daily_edit(request, task_date):
        task_date_string = task_date[:4] + "/" + task_date[4:6] + "/" + task_date[6:]
        daily_tasks = get_list_or_404(ParentTask, task_date=task_date_string)
        return render(request, 'timentor/list_daily_edit.html', {
            'daily_tasks': daily_tasks,
            'task_date': task_date
            })


def list_daily_task_edit(request, task_date, task_no):
    task_date_string = task_date[:4] + "/" + task_date[4:6] + "/" + task_date[6:]
    daily_child_task = get_list_or_404(ParentTask, task_date=task_date_string, task_no=task_no)
    return render(request, 'timentor/list_daily_task_edit.html', {'task': daily_child_task})

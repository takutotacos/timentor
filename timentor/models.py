from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.timezone import datetime


class Task(models.Model):
    TASK_NO_CHOICES = (
        (1, 1), (2, 2), (3, 3), (4, 4), (5, 5),
        (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)
    )
    task_no = models.IntegerField("No.", validators=[MaxValueValidator(10)], choices=TASK_NO_CHOICES)
    task_name = models.CharField("Task Name", max_length=256, blank=False)
    time = models.CharField("Time", max_length=3, blank=False)
    time_start_hour = models.IntegerField("From(Hour)", validators=[MaxValueValidator(24)])
    time_start_min = models.IntegerField("From(Min)", validators=[MaxValueValidator(60)])
    time_end_hour = models.IntegerField("To(Hour)", validators=[MaxValueValidator(24)])
    time_end_min = models.IntegerField("To(Min)", validators=[MaxValueValidator(60)])
    time_started_hour = models.IntegerField(validators=[MaxValueValidator(24)], blank=True, null=True)
    time_started_min = models.IntegerField(validators=[MaxValueValidator(60)], blank=True, null=True)
    time_ended_hour = models.IntegerField(validators=[MaxValueValidator(24)], blank=True, null=True)
    time_ended_min = models.IntegerField(validators=[MaxValueValidator(60)], blank=True, null=True)
    create_date = models.DateTimeField
    update_date = models.DateTimeField

    class Meta:
        abstract = True

    def __str__(self):
        return self.task_name


class ParentTask(Task):
    today = datetime.now().strftime("%Y/%m/%d")
    task_date = models.CharField("Date", max_length=10, default=today)


class ChildTask(Task):
    parent_task = models.ForeignKey(ParentTask, verbose_name="Task for", blank=True, null=True)
    classification = models.CharField(max_length=256, verbose_name="Tag")

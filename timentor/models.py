from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.timezone import datetime


class Task(models.Model):
    TASK_NO_CHOICES = (
        (1, 1), (2, 2), (3, 3), (4, 4), (5, 5),
        (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)
    )
    TIME_CHOICES = (
        ('0.5', '0.5'), ('1', '1'), ('1.5', '1.5'), ('2', '2'), ('2.5', '2.5'), ('3', '3'),
        ('3.5', '3.5'), ('4', '4'), ('4.5', '4.5'), ('5', '5'), ('6', '6'), ('7', '7')
    )
    TIME_START_AND_END_CHOICES = (
        ('3.5', '3:30'), ('4', '4:00'), ('4.5', '4:30'), ('5', '5:00'), ('5.5', '5:30'), ('6', '6:00'), ('6.5', '6:30'),
        ('7', '7:00'), ('7.5', '7:30'), ('8', '8:00'), ('8.5', '8:30'), ('9', '9:00'), ('9.5', '9:30'), ('10', '10:00'),
        ('10.5', '10:30'), ('11', '11:00'), ('11.5', '11:30'), ('12', '12:00'), ('12.5', '12:30'), ('13', '13:00'),
        ('13.5', '13:30'), ('14', '14:00'), ('14.5', '14:30'), ('15', '15:00'), ('15.5', '15:30'), ('16', '16:00'),
        ('16.5', '16:30'), ('17', '17:00'), ('17.5', '17:30'), ('18', '18:00'), ('18.5', '18:30'), ('19', '19:00'),
        ('19.5', '19:30'), ('20', '20:00'), ('20.5', '20:30'), ('21', '21:00'), ('21.5', '21:30'), ('22', '22:00'),
        ('22.5', '22:30')
    )
    task_no = models.IntegerField("No.", validators=[MaxValueValidator(10)], choices=TASK_NO_CHOICES)
    task_name = models.CharField("Task Name", max_length=256, blank=False)
    time = models.CharField("Time", blank=False, max_length=3, choices=TIME_CHOICES)
    time_start = models.CharField("From", max_length=5, choices=TIME_START_AND_END_CHOICES)
    time_end = models.CharField("To", max_length=5, choices=TIME_START_AND_END_CHOICES)
    time_started = models.IntegerField(blank=True, null=True)
    time_ended = models.IntegerField(blank=True, null=True)
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

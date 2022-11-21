from django.db import models
from django.contrib.auth.models import User

class user(models.Model):
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    employeenumber = models.CharField('Employee ID', max_length=10)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class dops(models.Model):
    dops_date = models.DateTimeField('DOPS Date')
    mentor = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    msnumber = models.IntegerField ('Milestone Number')
    comments = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.mentor}, {self.dops_date}"
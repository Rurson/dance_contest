from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Contest(models.Model):
    title = models.CharField(max_length=128)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    members = models.ManyToManyField(User, through='Membership')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['start_date']


class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    type = models.CharField(max_length=25, choices=[('C', 'Contender'), ('J', 'Jury')])

    def __str__(self):
        return str(self.user)


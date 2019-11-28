from django.db import models
from django.contrib.auth.models import User


class Contest(models.Model):
    title = models.CharField(max_length=128)
    number_of_stages = models.IntegerField(default=0)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    members = models.ManyToManyField(User, through="Membership")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["start_date"]


class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    member_type = models.CharField(max_length=25, choices=[("C", "Contender"), ("J", "Jury")])

    def __str__(self):
        return str(self.user)


class Vote(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    jury = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    contender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    stage = models.IntegerField(null=False)
    points = models.IntegerField()

    def __str__(self):
        return f"jury{self.jury}/contender_{self.contender}/stage_{self.stage}/points_{self.points}"

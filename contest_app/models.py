from django.db import models
from django.contrib.auth.models import User
import enum


class MemberTypeEnum(enum.Enum):
    CONTENDER = "Contender"
    JURY = "Jury"
    ORGANIZER = "Organizer"


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
    member_type = models.CharField(
        max_length=25, choices=[(tag, tag.value) for tag in MemberTypeEnum]
    )

    def __str__(self):
        return str(self.user)


class Stage(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    stage_no = models.IntegerField()

    def __str__(self):
        return f"{self.contest}/stage_{self.stage_no}"


class Vote(models.Model):
    jury = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    contender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)

    points = models.IntegerField(default=0)

    def __str__(self):
        return f"jury{self.jury}/contender_{self.contender}/stage_{self.stage}/points_{self.points}"

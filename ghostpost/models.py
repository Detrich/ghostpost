from django.db import models
from django.utils import timezone

# Create your models here.
class RoastsAndBoasts(models.Model):
    roastorboast = models.BooleanField()
    content = models.CharField(max_length=280)
    upVotes = models.IntegerField(default=0)
    downVotes = models.IntegerField(default=0)
    time = models.DateTimeField(default=timezone.now)
    score = models.IntegerField(default=0)
    def __str__(self):
        if self.roastorboast == True:
            return "Roast"
        if self.roastorboast == False:
            return "Boast"

# Boolean to tell whether it's a boast or a roast
# CharField to put the content of the post in
# IntegerField for up votes
# IntegerField for down votes
# DateTimeField for submission time
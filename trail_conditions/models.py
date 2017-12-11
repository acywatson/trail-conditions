from django.db import models
from django.utils import timezone


class Conditions(models.Model):
	condition_verdict = models.BooleanField()
	yes_votes = models.IntegerField(name='yes_votes', default=0)
	no_votes = models.IntegerField(name='no_votes', default=0)
	timestamp = models.DateTimeField(name='timestamp', default=timezone.now)

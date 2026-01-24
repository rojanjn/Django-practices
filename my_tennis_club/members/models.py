from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=225, null=False)
    lastname = models.CharField(max_length=225, null=False)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
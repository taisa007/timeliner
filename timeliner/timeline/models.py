from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'users'


class Tweet(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)

    class Meta:
        managed = True
        db_table = 'tweets'


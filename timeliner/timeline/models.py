from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'users'


class Tweet(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    content = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'tweets'


class Follows(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='follows_user')
    follow_user = models.ForeignKey(User, related_name='follows_follow_user')

    class Meta:
        managed = True
        db_table = 'follows'


class Followers(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='followers_user')
    follower_user = models.ForeignKey(User, related_name='followers_follower_user')

    class Meta:
        managed = True
        db_table = 'followers'

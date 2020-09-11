from django.db import models

# SuperUserInformation
# User: Jose
# Email: training@pieriandata.com
# Password: testpassword

# CREATE SOME TEST DATA WITH SOME SHELL COMMANDS:

# python manage.py shell

# from first_app.models import Topic
# print(Topic.objects.all())
# t = Topic(top_name="Social Network")
# t.save()
# print(Topic.objects.all())
# quit()

class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name

# Post Django 1.9, on_delete is a required argument

class Webpage(models.Model):
    # Add on_delete to get rid of error
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    # Add on_delete to get rid of error
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

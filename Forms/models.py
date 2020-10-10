from django.db import models

class Application(models.Model):
    Name = models.CharField(max_length = 100)
    MobileNumber = models.CharField(max_length = 20)
    Univesity = models.CharField(max_length = 30)
    Faculty = models.CharField(max_length = 30)
    Academic_year = models.CharField(max_length = 10)
    First_preference = models.CharField(max_length = 10)
    Second_preference = models.CharField(max_length = 10)
    Previous_experience = models.TextField(max_length = 2000)
    Whyapec = models.TextField(max_length = 1000)
    Hear = models.CharField(max_length = 100)
    First_second_pref = models.TextField(max_length = 1000)
    Percentage = models.CharField(max_length = 10)
    Expect = models.TextField(max_length = 1000)
    PersonalSkills = models.TextField(max_length = 1000)
    ALone_team = models.CharField(max_length = 10)
    Schedule = models.TextField(max_length = 500)
    Learn = models.TextField(max_length = 1000)
    LeaderRadio = models.CharField(max_length = 10)
    LeaderChar = models.TextField(max_length = 1000)


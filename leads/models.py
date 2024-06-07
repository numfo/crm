from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_organisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class LeadManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset()
    

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    organisation = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    agent = models.ForeignKey("Agent",null=True,blank=True,on_delete=models.SET_NULL)
    category = models.ForeignKey("Category",related_name="leads",null=True,blank=True,on_delete=models.SET_NULL)
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    converted_date = models.DateTimeField(null=True,blank=True)

    objects = LeadManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Agent(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile,on_delete=models.CASCADE)  

    def __str__(self):
        return self.user.email  

class Category(models.Model):
    name=models.CharField(max_length=30)
    organisation = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    



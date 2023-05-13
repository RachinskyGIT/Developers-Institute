from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):

   name = models.CharField( max_length=100)
   description = models.TextField( blank=True)

   def __str__(self):
       return self.name


class Employee(models.Model):

   name  = models.CharField(max_length=100)
   email  = models.EmailField()
   phone_number  = models.CharField(max_length=16)
   department  = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)

   def __str__(self):
       return f"{self.name} ({self.email}), {self.department}"
   

class Project(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField() 
    end_date = models.DateTimeField(blank=True, null=True) 

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField( blank=True)
    due_date = models.DateTimeField() 
    completed  = models.BooleanField() 
    project  = models.ForeignKey('Project', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f"{self.name}, completed: {self.completed}, project: {self.project}"
   

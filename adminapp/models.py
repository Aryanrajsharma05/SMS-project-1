from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class StudentList(models.Model):
    Register_Number = models.CharField(max_length=20, unique=True)
    Name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def str(self):
        return self.Register_Number

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=10, null=True, blank=True)
    comments = models.TextField(max_length=50)

    def _str_(self):
        return f"{self.name} ({self.email})"



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Ensures that each email is unique
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Optional field
    address = models.TextField(blank=True, null=True)  # Optional field

    def __str__(self):
        return self.name  # Returns the name when the object is printed or displayed


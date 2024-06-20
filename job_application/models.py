from django.db import models
from datetime import datetime


class Form(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    position = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    start_date = models.DateField()
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    file = models.FileField(upload_to='resumes')

    def __str__(self):
        return f"{self.first_name}"
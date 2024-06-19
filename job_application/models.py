from django.db import models


class Form(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    position = models.CharField(max_length=50)
    start_date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
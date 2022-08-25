from tabnanny import verbose
from django.db import models

class Student(models.Model):
    first_name = models.CharField("Name", max_length=50)
    last_name = models.CharField("LastName", max_length=50)
    number = models.IntegerField("Number")

    def __str__(self):
        return f"{self.number} - {self.first_name} {self.last_name}"

    class Meta:
        ordering = ["number"] #DESC --> ["-number"]
        verbose_name_plural = "Students"
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    gpa = models.FloatField()

    def str(self):
        return self.name
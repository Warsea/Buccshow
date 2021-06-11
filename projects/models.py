from django.db import models

class Project(models.Model):
    student_name = models.CharField(max_length=100, null=True)
    project_name = models.CharField(max_length=100, null=True)
    subtitle = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=10000, null=True)
    links = models.CharField(max_length=2000, null=True)
    contact = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return self.project_name
    
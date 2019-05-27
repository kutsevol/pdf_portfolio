from django.db import models

from pdf_app.models.experience import Experience


class Technology(models.Model):
    name = models.CharField(max_length=100)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE,
                                   related_name='technologies')

from django.db import models

from pdf_app.models.cv import CV


class Skill(models.Model):
    name = models.CharField(max_length=100)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='skills')

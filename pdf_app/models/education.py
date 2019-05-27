from django.db import models

from pdf_app.models.cv import CV


class Education(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    cv = models.ForeignKey(CV, on_delete=models.CASCADE,
                           related_name='educations')

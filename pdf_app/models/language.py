from django.db import models

from pdf_app.models.cv import CV


class Language(models.Model):
    name = models.CharField(max_length=50)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE,
                           related_name='languages')

from django.db import models

from pdf_app.models import PersonDetail


class Social(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    person_details = models.ForeignKey(PersonDetail, on_delete=models.CASCADE,
                                       related_name='socials')

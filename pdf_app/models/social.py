from django.db import models

from pdf_app.models import PersonDetail


class Social(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    person_detail = models.ForeignKey(PersonDetail, on_delete=models.CASCADE,
                                      related_name='socials')

    def __str__(self):
        return self.name

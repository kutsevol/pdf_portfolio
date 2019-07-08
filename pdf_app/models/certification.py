from django.db import models

from pdf_app.models.cv import CV


class Certification(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    cv = models.ForeignKey(CV, on_delete=models.CASCADE,
                           related_name='certifications')

    def __str__(self):
        return self.name

from django.db import models

from pdf_app.models.cv import CV


class Education(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE,
                           related_name='educations')

    def __str__(self):
        return self.name

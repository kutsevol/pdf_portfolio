from datetime import datetime

from django.db import models

from pdf_app.models import CV


class PersonDetail(models.Model):
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    skype = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    birth_day = models.DateField()
    cv = models.OneToOneField(CV, on_delete=models.CASCADE,
                              related_name="person_details")

    def age(self):
        return datetime.now().year - self.birth_day.year

    def __str__(self):
        return self.email

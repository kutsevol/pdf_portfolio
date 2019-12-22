from datetime import datetime

from django.db import models

from pdf_app.models import CV


class PersonDetail(models.Model):
    """
    PersonDetail model which describe typical fields for skill.

    Phone - personal mobile number
    Email - personal email
    Skype - skype login
    City - current living city
    Country - current living country
    Birth day - day of birth
    CV - foreign key on CV model
    """

    phone = models.CharField(max_length=50)
    email = models.EmailField()
    skype = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    birth_day = models.DateField()
    cv = models.OneToOneField(CV, on_delete=models.CASCADE,
                              related_name="person_details")

    @property
    def age(self):
        """Function to return total number of years."""
        return datetime.now().year - self.birth_day.year

    def __str__(self):
        """
        Function to represent each record in readable format.

        :return: personal email
        """
        return self.email

from django.db import models

from pdf_app.models import PersonDetail


class Social(models.Model):
    """
    Social model which describe typical fields for social.

    Name - name of social network
    Link - link to profile
    Person Detail - foreign key on PersonDetail model
    """

    name = models.CharField(max_length=100)
    link = models.URLField()
    person_detail = models.ForeignKey(PersonDetail, on_delete=models.CASCADE,
                                      related_name='socials')

    def __str__(self):
        """
        Function to represent each record in readable format.

        :return: name of social network
        """
        return self.name

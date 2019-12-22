from django.db import models

from pdf_app.models.cv import CV


class Certification(models.Model):
    """
    Certification model which describe typical fields for certification.

    Name - name of certification
    URL - link on document with pass date of certification
    CV - foreign key on CV model
    """

    name = models.CharField(max_length=100)
    url = models.URLField()
    cv = models.ForeignKey(CV, on_delete=models.CASCADE,
                           related_name='certifications')

    def __str__(self):
        """
        Function to represent each record in readable format.

        :return: name of certification
        """
        return self.name

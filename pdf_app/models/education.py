from django.db import models

from pdf_app.models.cv import CV


class Education(models.Model):
    """
    Education model which describe typical fields for education.

    Name - name of educational institution
    Course - name of specialization or department
    Start and End date - starting and graduating in university
    CV - foreign key on CV model
    """

    name = models.CharField(max_length=100)
    course = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE,
                           related_name='educations')

    def __str__(self):
        """
        Function to represent each record in readable format.

        :return: name of educational institution
        """
        return self.name

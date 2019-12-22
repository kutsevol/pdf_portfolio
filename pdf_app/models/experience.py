from django.db import models

from pdf_app.models.cv import CV


class Experience(models.Model):
    """
    Experience model which describe typical fields for experience.

    Company name and url - information about company
    Project name and description - information about project
    Start and End date - start and finish working on project
    Position - what does position on project
    Responsibility - immediate duties
    CV - foreign key on CV model
    """

    company_name = models.CharField(max_length=100)
    company_url = models.URLField()
    project_name = models.CharField(max_length=100)
    project_description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    position = models.CharField(max_length=100)
    responsibility = models.TextField()
    cv = models.ForeignKey(CV, on_delete=models.CASCADE,
                           related_name='experiences')

    @property
    def responsibilities_as_list(self):
        """Function to return list of responsibilities split by semicolon."""
        return self.responsibility.split(";")

    def __str__(self):
        """
        Function to represent each record in readable format.

        :return: string which included company and project name and position
        """
        return f"{self.company_name}, {self.project_name}, {self.position}"

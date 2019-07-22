from django.db import models

from pdf_app.models.cv import CV


class Experience(models.Model):
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
        return self.responsibility.split(";")

    def __str__(self):
        return f"{self.company_name}, {self.project_name}, {self.position}"

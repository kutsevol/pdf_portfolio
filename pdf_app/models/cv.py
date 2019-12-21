from django.db import models


class CV(models.Model):
    """
    CV model which describe typical fields for cv.

    First name, Last name - personal information
    Objective - short description about future place work and etc
    Summary - short introduce
    """

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    objective = models.TextField()
    summary = models.TextField()

    class Meta:
        verbose_name = 'CV'
        verbose_name_plural = 'CV'

    @property
    def full_name(self):
        """Function to return first and last names together."""
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        """
        Function to represent each record in readable format.

        :return: full name of job seeker
        """
        return self.full_name

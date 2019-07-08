from django.db import models


class CV(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    objective = models.TextField()
    summary = models.TextField()

    class Meta:
        verbose_name = 'CV'
        verbose_name_plural = 'CV'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()

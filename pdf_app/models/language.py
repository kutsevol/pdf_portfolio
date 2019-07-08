from django.db import models

from pdf_app.models.cv import CV


LANGUAGE_PROFICIENCY = [
    ('Beginner', 'Beginner'),
    ('Elementary', 'Elementary'),
    ('Intermediate', 'Intermediate'),
    ('Upper intermediate', 'Upper intermediate'),
    ('Advanced', 'Advanced'),
    ('Proficient', 'Proficient')
]


class Language(models.Model):
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=50,
                             choices=LANGUAGE_PROFICIENCY,
                             default='Beginner')
    cv = models.ForeignKey(CV, on_delete=models.CASCADE,
                           related_name='languages')

    def __str__(self):
        return self.name

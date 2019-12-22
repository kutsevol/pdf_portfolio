from django.db import models

from pdf_app.models.cv import CV

LANGUAGE_PROFICIENCY = [
    ('Beginner', 'Beginner'),
    ('Elementary', 'Elementary'),
    ('Intermediate', 'Intermediate'),
    ('Upper intermediate', 'Upper intermediate'),
    ('Advanced', 'Advanced'),
    ('Proficient', 'Proficient'),
]


class Language(models.Model):
    """
    Language model which describe typical fields for language.

    Name - name of language
    Level - knowledge of language
    CV - foreign key on CV model
    """

    name = models.CharField(max_length=50)
    level = models.CharField(max_length=50,
                             choices=LANGUAGE_PROFICIENCY,
                             default='Beginner')
    cv = models.ForeignKey(CV, on_delete=models.CASCADE,
                           related_name='languages')

    def __str__(self):
        """
        Function to represent each record in readable format.

        :return: name of language
        """
        return self.name

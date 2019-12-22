from django.db import models

from pdf_app.models import Experience

GROUP_OF_SKILLS = [
    ('Language', 'Language'),
    ('Framework', 'Framework'),
    ('CI', 'Continuous Integration'),
    ('Other', 'Other'),
    ('DB', 'Database'),
    ('Virtualization', 'Virtualization'),
]


class Skill(models.Model):
    """
    Skill model which describe typical fields for skill.

    Group - group of skills
    Name - name of skill
    Experience - foreign key on Experience model
    """

    group = models.CharField(max_length=50,
                             choices=GROUP_OF_SKILLS,
                             default='Other')
    name = models.CharField(max_length=100)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE,
                                   related_name='skills')

    def __str__(self):
        """
        Function to represent each record in readable format.

        :return: name of skill
        """
        return self.name

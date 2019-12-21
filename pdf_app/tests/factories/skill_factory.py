from factory import DjangoModelFactory, Faker, SubFactory, fuzzy

from pdf_app.models import Skill
from pdf_app.tests.factories.experience_factory import ExperienceFactory

GROUP_OF_SKILLS = [
    'Language',
    'Framework',
    'Continuous Integration',
    'Other',
    'Database',
    'Virtualization',
]


class SkillFactory(DjangoModelFactory):
    """Prepare Factory for Skill model."""

    name = Faker("word")
    group = fuzzy.FuzzyChoice(GROUP_OF_SKILLS)
    experience = SubFactory(ExperienceFactory)

    class Meta:
        model = Skill

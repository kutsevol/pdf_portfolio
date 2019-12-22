from factory import DjangoModelFactory, Faker, SubFactory, fuzzy

from pdf_app.models import Language
from pdf_app.tests.factories.cv_factory import CVFactory

LANGUAGE_PROFICIENCY = [
    'Beginner',
    'Elementary',
    'Intermediate',
    'Upper intermediate',
    'Advanced',
    'Proficient',
]


class LanguageFactory(DjangoModelFactory):
    """Prepare Factory for Language model."""

    name = Faker("word")
    level = fuzzy.FuzzyChoice(LANGUAGE_PROFICIENCY)
    cv = SubFactory(CVFactory)

    class Meta:
        model = Language

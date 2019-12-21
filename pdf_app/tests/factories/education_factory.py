from django.utils import timezone
from factory import DjangoModelFactory, Faker, SubFactory

from pdf_app.models import Education
from pdf_app.tests.factories.cv_factory import CVFactory


class EducationFactory(DjangoModelFactory):
    """Prepare Factory for Education model."""

    name = Faker("word")
    course = Faker("sentence", nb_words=4)
    start_date = Faker("date_time", tzinfo=timezone.get_current_timezone())
    end_date = Faker("date_time", tzinfo=timezone.get_current_timezone())
    cv = SubFactory(CVFactory)

    class Meta:
        model = Education

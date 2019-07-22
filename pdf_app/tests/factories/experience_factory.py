from django.utils import timezone
from factory import DjangoModelFactory, Faker, SubFactory

from pdf_app.models import Experience
from pdf_app.tests.factories.cv_factory import CVFactory


class ExperienceFactory(DjangoModelFactory):
    company_name = Faker("word")
    company_url = Faker("url")
    project_name = Faker("word")
    project_description = Faker("paragraph", nb_sentences=3)
    start_date = Faker("date_time", tzinfo=timezone.get_current_timezone())
    end_date = Faker("date_time", tzinfo=timezone.get_current_timezone())
    position = Faker("sentence", nb_words=3)
    responsibility = Faker("paragraph", nb_sentences=5)
    cv = SubFactory(CVFactory)

    class Meta:
        model = Experience

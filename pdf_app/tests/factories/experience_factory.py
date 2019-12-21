from django.utils import timezone
from factory import DjangoModelFactory, Faker, SubFactory, post_generation

from pdf_app.models import Experience
from pdf_app.tests.factories.cv_factory import CVFactory


class ExperienceFactory(DjangoModelFactory):
    """Prepare Factory for Experience model."""

    company_name = Faker("word")
    company_url = Faker("url")
    project_name = Faker("word")
    project_description = Faker("paragraph", nb_sentences=3)
    start_date = Faker("date_time", tzinfo=timezone.get_current_timezone())
    end_date = Faker("date_time", tzinfo=timezone.get_current_timezone())
    position = Faker("sentence", nb_words=3)
    responsibility = Faker("paragraph", nb_sentences=5)
    cv = SubFactory(CVFactory)

    @post_generation
    def add_skills_to_experience(self, created: bool, extracted, **kwargs):
        """
        To add experience for CV model.

        :param created: if factory calls like `ExperienceFactory.build()`
        :param extracted: if factory calls like `ExperienceFactory.create()` or
        `ExperienceFactory()`
        :param kwargs: other arguments
        """
        if not created:
            return

        if extracted:
            for skill in extracted:
                self.skills.add(skill)

    class Meta:
        model = Experience

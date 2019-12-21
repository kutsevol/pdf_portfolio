from factory import DjangoModelFactory, Faker, post_generation

from pdf_app.models import CV


class CVFactory(DjangoModelFactory):
    """Prepare Factory for CV model."""

    first_name = Faker("first_name")
    last_name = Faker("last_name")
    objective = Faker("paragraph", nb_sentences=3)
    summary = Faker("paragraph", nb_sentences=3)

    @post_generation
    def add_experiences_to_cv(self, created: bool, extracted, **kwargs):
        """
        To add experience for CV model.

        :param created: if factory calls like `CVFactory.build()`
        :param extracted: if factory calls like `CVFactory.create()` or
        `CVFactory()`
        :param kwargs: other arguments
        """
        if not created:
            return

        if extracted:
            for experience in extracted:
                self.experiences.add(experience)

    class Meta:
        model = CV

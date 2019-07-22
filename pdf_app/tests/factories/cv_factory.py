from factory import DjangoModelFactory, Faker


from pdf_app.models import CV


class CVFactory(DjangoModelFactory):

    first_name = Faker("first_name")
    last_name = Faker("last_name")
    objective = Faker("paragraph", nb_sentences=3)
    summary = Faker("paragraph", nb_sentences=3)

    class Meta:
        model = CV

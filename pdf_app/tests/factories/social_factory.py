from factory import DjangoModelFactory, Faker, SubFactory


from pdf_app.models import Social
from pdf_app.tests.factories.person_detail_factory import PersonDetailFactory


class SocialFactory(DjangoModelFactory):
    name = Faker("word")
    link = Faker("url")
    person_detail = SubFactory(PersonDetailFactory)

    class Meta:
        model = Social

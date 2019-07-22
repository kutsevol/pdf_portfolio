from factory import DjangoModelFactory, Faker, SubFactory


from pdf_app.models import Certification
from pdf_app.tests.factories.cv_factory import CVFactory


class CertificationFactory(DjangoModelFactory):

    name = Faker("word")
    url = Faker("url")
    cv = SubFactory(CVFactory)

    class Meta:
        model = Certification

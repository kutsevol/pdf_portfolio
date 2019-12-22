from factory import DjangoModelFactory, Faker, SubFactory

from pdf_app.models import PersonDetail
from pdf_app.tests.factories.cv_factory import CVFactory


class PersonDetailFactory(DjangoModelFactory):
    """Prepare Factory for PersonDetail model."""

    phone = Faker("phone_number")
    email = Faker("email")
    skype = Faker("user_name")
    city = Faker("city")
    country = Faker("country")
    birth_day = Faker("date_of_birth")
    cv = SubFactory(CVFactory)

    class Meta:
        model = PersonDetail

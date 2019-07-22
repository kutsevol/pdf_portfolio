import pytest

from pdf_app.tests.factories import (CVFactory, CertificationFactory,
                                     EducationFactory, ExperienceFactory,
                                     LanguageFactory, PersonDetailFactory,
                                     SkillFactory, SocialFactory)


@pytest.fixture
def cv():
    return CVFactory()


@pytest.fixture
def certification():
    return CertificationFactory()


@pytest.fixture
def education():
    return EducationFactory()


@pytest.fixture
def experience():
    return ExperienceFactory()


@pytest.fixture
def language():
    return LanguageFactory()


@pytest.fixture
def person_detail():
    return PersonDetailFactory()


@pytest.fixture
def skill():
    return SkillFactory()


@pytest.fixture
def social():
    return SocialFactory()

from random import randint
import pytest

from pdf_app.tests.factories import (CVFactory, CertificationFactory,
                                     EducationFactory, ExperienceFactory,
                                     LanguageFactory, PersonDetailFactory,
                                     SkillFactory, SocialFactory)


@pytest.fixture
def cv():
    return CVFactory(
        add_experiences_to_cv=[
            ExperienceFactory(
                add_skills_to_experience=[
                    SkillFactory()
                    for _ in range(randint(0, 3))
                ]
            )
            for _ in range(randint(0, 3))],

    )


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

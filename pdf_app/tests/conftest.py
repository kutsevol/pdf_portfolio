from random import randint

import pytest

from pdf_app.tests.factories import (
    CertificationFactory,
    CVFactory,
    EducationFactory,
    ExperienceFactory,
    LanguageFactory,
    PersonDetailFactory,
    SkillFactory,
    SocialFactory,
)


@pytest.fixture
def cv():
    """Fixture to prepare CV Factory."""
    return CVFactory(
        add_experiences_to_cv=[
            ExperienceFactory(
                add_skills_to_experience=[
                    SkillFactory()
                    for _ in range(randint(0, 3))
                ],
            )
            for _ in range(randint(0, 3))],

    )


@pytest.fixture
def certification():
    """Fixture to prepare Certification Factory."""
    return CertificationFactory()


@pytest.fixture
def education():
    """Fixture to prepare Education Factory."""
    return EducationFactory()


@pytest.fixture
def experience():
    """Fixture to prepare Experience Factory."""
    return ExperienceFactory()


@pytest.fixture
def language():
    """Fixture to prepare Language Factory."""
    return LanguageFactory()


@pytest.fixture
def person_detail():
    """Fixture to prepare Person Detail Factory."""
    return PersonDetailFactory()


@pytest.fixture
def skill():
    """Fixture to prepare Skill Factory."""
    return SkillFactory()


@pytest.fixture
def social():
    """Fixture to prepare Social Factory."""
    return SocialFactory()

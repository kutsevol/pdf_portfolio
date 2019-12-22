from datetime import datetime

import pytest

pytestmark = pytest.mark.django_db


def test_str_cv(cv):
    """
    Verify that __str__ function return correct value.

    :param cv: CV fixture
    """
    assert cv.__str__() == f"{cv.first_name} {cv.last_name}"


def test_full_name_cv(cv):
    """
    Verify that property full_name return correct value.

    :param cv: CV fixture
    """
    assert cv.full_name == f"{cv.first_name} {cv.last_name}"


def test_str_certification(certification):
    """
    Verify that __str__ function return correct value.

    :param certification: Certification fixture
    """
    assert certification.__str__() == certification.name


def test_str_education(education):
    """
    Verify that __str__ function return correct value.

    :param education: Education fixture
    """
    assert education.__str__() == education.name


def test_str_experience(experience):
    """
    Verify that __str__ function return correct value.

    :param experience: Experience fixture
    """
    expected_result = ", ".join((
        experience.company_name,
        experience.project_name,
        experience.position,
    ))
    assert experience.__str__() == expected_result


def test_responsibilities_as_list_experience(experience):
    """
    Verify that property responsibilities_as_list return correct value.

    :param experience: Experience fixture
    """
    expected_result = experience.responsibility.split(";")
    assert experience.responsibilities_as_list == expected_result


def test_str_language(language):
    """
    Verify that __str__ function return correct value.

    :param language: Language fixture
    """
    assert language.__str__() == language.name


def test_str_person_detail(person_detail):
    """
    Verify that __str__ function return correct value.

    :param person_detail: Person Detail fixture
    """
    assert person_detail.__str__() == person_detail.email


def test_age_person_detail(person_detail):
    """
    Verify that property age return correct value.

    :param person_detail: Person Detail fixture
    """
    expected_age = datetime.now().year - person_detail.birth_day.year
    assert person_detail.age == expected_age


def test_str_skill(skill):
    """
    Verify that __str__ function return correct value.

    :param skill: Skill fixture
    """
    assert skill.__str__() == skill.name


def test_str_social(social):
    """
    Verify that __str__ function return correct value.

    :param social: Social fixture
    """
    assert social.__str__() == social.name

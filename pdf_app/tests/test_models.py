from datetime import datetime

import pytest


pytestmark = pytest.mark.django_db


def test_str_cv(cv):
    assert cv.__str__() == f"{cv.first_name} {cv.last_name}"


def test_full_name_cv(cv):
    assert cv.full_name == f"{cv.first_name} {cv.last_name}"


def test_str_certification(certification):
    assert certification.__str__() == certification.name


def test_str_education(education):
    assert education.__str__() == education.name


def test_str_experience(experience):
    assert experience.__str__() == f"{experience.company_name}, " \
        f"{experience.project_name}, {experience.position}"


def test_responsibilities_as_list_experience(experience):
    expected_result = experience.responsibility.split(";")
    assert experience.responsibilities_as_list == expected_result


def test_str_language(language):
    assert language.__str__() == language.name


def test_str_person_detail(person_detail):
    assert person_detail.__str__() == person_detail.email


def test_age_person_detail(person_detail):
    expected_age = datetime.now().year - person_detail.birth_day.year
    assert person_detail.age == expected_age


def test_str_skill(skill):
    assert skill.__str__() == skill.name


def test_str_social(social):
    assert social.__str__() == social.name

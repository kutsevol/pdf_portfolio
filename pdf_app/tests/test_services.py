from collections import defaultdict

import pytest

from pdf_app.services.render_pdf import render
from pdf_app.services.skills import get_all_skills_for_user
from utils.constants import BASE_DIR


pytestmark = pytest.mark.django_db


def test_render_service():
    template = BASE_DIR.joinpath("templates/pdf_app/pdf.html")
    params = {}
    response = render(template, params)
    assert response.status_code == 200
    assert response["Content-Type"] == "application/pdf"

# TODO: to add test for checking wrong render pdf


def test_get_all_skills_for_user(cv):
    expected_result = defaultdict(list)

    for exp in cv.experiences.all():
        for skill in exp.skills.all():
            expected_result[skill.group].append(skill.name)

    actual_result = get_all_skills_for_user(cv)

    for key in actual_result:
        assert sorted(expected_result[key]) == sorted(actual_result[key])

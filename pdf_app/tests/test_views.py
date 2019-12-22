import pytest

from pdf_app.tests.data.data_views import (
    bulk_negative_responses,
    bulk_positive_responses,
)


@pytest.mark.parametrize("mock_response", bulk_positive_responses)
def test_positive_view(client, django_user_model, mock_response, cv):
    """
    To check positive cases for views.

    :param client: pytest fixture for django client
    :param django_user_model: pytest fixture for django user model
    :param mock_response: mock data with positive responses
    :param cv: fixture to check CV factory data
    """
    username = "admin"
    password = "pass"
    django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)

    urls = {
        "index": "/",
        "pdf": "/pdf/",
    }

    response = client.get(urls[mock_response.path])

    assert mock_response.code == response.status_code
    assert mock_response.view_class == response.resolver_match.func.view_class
    if mock_response.check_template:
        assert mock_response.template_name in response.template_name
    response_content = response.content.decode(mock_response.content_encoding)
    assert mock_response.content_body in response_content
    assert mock_response.content_title in response_content


@pytest.mark.parametrize("mock_response", bulk_negative_responses)
def test_negative_view(client, mock_response):
    """
    To check negative cases for views.

    :param client: pytest fixture for django client
    :param mock_response: mock data with negative responses
    """
    urls = {
        "index": "testing",
    }

    response = client.get(urls[mock_response.path])
    assert mock_response.code == response.status_code
    response_content = response.content.decode(mock_response.content_encoding)
    assert mock_response.content_body in response_content
    assert mock_response.content_title in response_content

import pytest
from django.urls import resolve, reverse

from pdf_app.tests.data.data_urls import valid_resolvers


@pytest.mark.parametrize("mock_resolver", valid_resolvers)
def test_reverse_func(mock_resolver):
    """
    Verify reverse function for all path which defined in urls.py
    :param mock_resolver: prepared data with all necessary fields
    """
    assert reverse(
        mock_resolver.name,
        kwargs=mock_resolver.kwargs
    ) == mock_resolver.path


@pytest.mark.parametrize("mock_resolver", valid_resolvers)
def test_resolve_func(mock_resolver):
    """
    Verify resolve function for all path which defined in urls.py
    :param mock_resolver: prepared data with all necessary fields
    """
    assert resolve(mock_resolver.path).view_name == mock_resolver.name

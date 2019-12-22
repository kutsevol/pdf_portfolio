from pathlib import PurePath

from pdf_app.apps import PdfAppConfig


def test_check_app_name():
    """To check compliance folder name with config name."""
    assert PdfAppConfig.name == PurePath(__file__).parent.parent.name

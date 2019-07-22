from collections import namedtuple

from pdf_app.views import CVView, PdfView

Response = namedtuple(
    "Response",
    [
        "path", "code", "view_class", "check_template", "template_name",
        "content_encoding", "content_body", "content_title"
    ]
)

Response.__doc__ = """
path - name that is used to retrieve data in tests (analogue setUp)
from the dictionary;
code - expected status code;
view_class - view resolver;
check_template - some cases don't generate template, need to skip checking
template name;
template_name - template name resolver;
content_encoding - parameter to choose correctly encoding in each case;
content_body - expected part in body;
content_title - expected part in title;
"""

bulk_positive_responses = [
    Response(
        path="index",
        code=200,
        view_class=CVView,
        check_template=True,
        template_name=CVView.template_name,
        content_encoding="utf-8",
        content_body="""Email:""",
        content_title="""Artur Kutsevol""",
    ),
    Response(
        path="pdf",
        code=200,
        view_class=PdfView,
        check_template=False,
        template_name=PdfView.template_name,
        content_encoding="windows-1252",
        content_body="",
        content_title="",
    ),
]


bulk_negative_responses = [
    Response(
        path="index",
        code=404,
        view_class="",
        check_template=False,
        template_name="",
        content_encoding="utf-8",
        content_body="Not Found",
        content_title="Not Found",
    )
]

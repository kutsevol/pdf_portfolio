from io import BytesIO

import xhtml2pdf.pisa as pisa
from django.http import HttpResponse
from django.template.loader import get_template


def render(path, params):
    """
    Function to render PDF file.

    :param path: to get template
    :param params: all required params to render template
    :return: Response with pdf file or Response with error
    """
    template = get_template(path)
    html = template.render(params)

    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)

    if pdf.err:
        return HttpResponse("Error Rendering PDF", status=400)

    return HttpResponse(result.getvalue(),
                        content_type='application/pdf')

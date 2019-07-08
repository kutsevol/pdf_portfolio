from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa


def render(path, params):
    template = get_template(path)
    html = template.render(params)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if pdf.err:
        return HttpResponse("Error Rendering PDF", status=400)
    return HttpResponse(result.getvalue(),
                        content_type='application/pdf')

from django.views.generic import TemplateView

from pdf_app.models import CV


class CVView(TemplateView):
    template_name = "pdf_app/cv.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cv"] = CV.objects.get(id=1)
        return context


cv_view = CVView.as_view()

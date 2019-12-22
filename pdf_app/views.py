from django.views.generic import TemplateView

from pdf_app.models import CV
from pdf_app.services.render_pdf import render
from pdf_app.services.skills import get_all_skills_for_user


class CVView(TemplateView):
    """View to represent information on frontend part like a web-site."""

    template_name = "pdf_app/cv.html"

    def get_context_data(self, **kwargs):
        """Add extra context."""
        context = super().get_context_data(**kwargs)
        if CV.objects.exists():
            cv = CV.objects.get(id=1)
            experiences = cv.experiences.all().prefetch_related("skills")
            context.update({
                "cv": cv,
                "experiences": experiences,
            })
        return context


class PdfView(TemplateView):
    """View to represent information in PDF format."""

    template_name = "pdf_app/pdf.html"

    def get(self, *args, **kwargs):
        """Provide additional data when called url /pdf."""
        if CV.objects.exists():
            # TODO need to check this condition
            cv = CV.objects.get(id=1) if CV.objects.exists() else []
            experiences = cv.experiences.all().prefetch_related("skills")
            params = {
                "cv": cv,
                "experiences": experiences,
                "skills": get_all_skills_for_user(cv, value_as_str=True),
            }
            return render(self.template_name, params)


cv_view = CVView.as_view()
pdf_view = PdfView.as_view()

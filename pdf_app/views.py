from django.views.generic import TemplateView

from pdf_app.models import CV
from pdf_app.services.render_pdf import render
from pdf_app.services.skills import get_all_skills_for_user


class CVView(TemplateView):
    template_name = "pdf_app/cv.html"

    def get_context_data(self, **kwargs):
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
    template_name = "pdf_app/pdf.html"

    def get(self, *args, **kwargs):
        if CV.objects.exists():
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

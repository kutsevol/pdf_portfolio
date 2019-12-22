from django.contrib import admin

from nested_inline.admin import NestedModelAdmin, NestedStackedInline
from pdf_app.models import (
    CV,
    Certification,
    Education,
    Experience,
    Language,
    PersonDetail,
    Skill,
    Social,
)


class SkillInline(NestedStackedInline):
    """Inline class for Skill."""

    model = Skill
    extra = 0
    min_num = 1
    fk_name = 'experience'


class SocialInline(NestedStackedInline):
    """Inline class for Social."""

    model = Social
    extra = 0
    min_num = 1
    fk_name = 'person_detail'


class CertificationInline(NestedStackedInline):
    """Inline class for Certification."""

    model = Certification
    extra = 0
    min_num = 1
    fk_name = 'cv'


class EducationInline(NestedStackedInline):
    """Inline class for Education."""

    model = Education
    extra = 0
    min_num = 1
    fk_name = 'cv'


class ExperienceInline(NestedStackedInline):
    """Inline class for Experience."""

    model = Experience
    extra = 0
    min_num = 1
    fk_name = 'cv'
    inlines = [SkillInline]


class LanguageInline(NestedStackedInline):
    """Inline class for Language."""

    model = Language
    extra = 0
    min_num = 1
    fk_name = 'cv'


class PersonDetailInline(NestedStackedInline):
    """Inline class for Person Detail."""

    model = PersonDetail
    extra = 0
    min_num = 1
    fk_name = 'cv'
    inlines = [SocialInline]


@admin.register(CV)
class CVAdmin(NestedModelAdmin):
    """CV class which collected all inline classes."""

    inlines = [PersonDetailInline, ExperienceInline, EducationInline,
               CertificationInline, LanguageInline]

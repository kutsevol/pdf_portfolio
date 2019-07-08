from django.contrib import admin
from nested_inline.admin import NestedModelAdmin, NestedStackedInline

from pdf_app.models import (CV, Certification, Education, Experience, Language,
                            PersonDetail, Skill, Social)


class SkillInline(NestedStackedInline):
    model = Skill
    extra = 0
    min_num = 1
    fk_name = 'experience'


class SocialInline(NestedStackedInline):
    model = Social
    extra = 0
    min_num = 1
    fk_name = 'person_detail'


class CertificationInline(NestedStackedInline):
    model = Certification
    extra = 0
    min_num = 1
    fk_name = 'cv'


class EducationInline(NestedStackedInline):
    model = Education
    extra = 0
    min_num = 1
    fk_name = 'cv'


class ExperienceInline(NestedStackedInline):
    model = Experience
    extra = 0
    min_num = 1
    fk_name = 'cv'
    inlines = [SkillInline]


class LanguageInline(NestedStackedInline):
    model = Language
    extra = 0
    min_num = 1
    fk_name = 'cv'


class PersonDetailInline(NestedStackedInline):
    model = PersonDetail
    extra = 0
    min_num = 1
    fk_name = 'cv'
    inlines = [SocialInline]


@admin.register(CV)
class CVAdmin(NestedModelAdmin):
    inlines = [PersonDetailInline, ExperienceInline, EducationInline,
               CertificationInline, LanguageInline]

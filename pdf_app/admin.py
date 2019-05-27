from django.contrib import admin
from nested_inline.admin import NestedModelAdmin, NestedStackedInline

from pdf_app.models import (CV, Certification, Education, Experience, Language,
                            PersonDetail, Skill, Social, Technology)


class TechnologyInline(NestedStackedInline):
    model = Technology
    extra = 0
    min_num = 1
    fk_name = 'experience'


class ExperienceInline(NestedStackedInline):
    model = Experience
    extra = 0
    min_num = 1
    fk_name = 'cv'
    inlines = [TechnologyInline]


class PersonDetailInline(NestedStackedInline):
    model = PersonDetail
    extra = 0
    min_num = 1
    fk_name = 'cv'


@admin.register(CV)
class CVAdmin(NestedModelAdmin):
    inlines = [ExperienceInline, PersonDetailInline]


admin.site.register(Certification)
admin.site.register(Education)
admin.site.register(Language)
admin.site.register(Skill)
admin.site.register(Social)
admin.site.register(Technology)

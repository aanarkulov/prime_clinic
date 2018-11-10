from django.conf import settings
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from modeltranslation.admin import TabbedTranslationAdmin

from webapp import models


class FaqAdmin(TabbedTranslationAdmin):
    pass


class AnnouncementAdmin(TabbedTranslationAdmin):
    pass


class SpecializationAdmin(TabbedTranslationAdmin):
    prepopulated_fields = {'slug': ('icon_name',)}


class AboutClinicAdmin(TabbedTranslationAdmin):
    pass


class SpecialityDoctorAdmin(TabbedTranslationAdmin):
    pass


class DoctorAdmin(TabbedTranslationAdmin):
    prepopulated_fields = {'slug': ('full_name',)}
    fieldsets = [
        (None, {
            'fields': ['full_name', 'speciality', 'photo', 'slug', ]}),
        (_('Дополнительная информация'), {
            'fields': ['about_doctor_ru', 'about_doctor_en', 'about_doctor_kg', 'education_ru', 'education_en',
                       'education_kg', 'experience_ru', 'experience_en', 'experience_kg']}),
    ]


class AdvantageAdmin(TabbedTranslationAdmin):
    prepopulated_fields = {'slug': ('title',)}


class DiagnosticAdmin(TabbedTranslationAdmin):
    prepopulated_fields = {'slug': ('title',)}


class DiagnosticTypeAdmin(TabbedTranslationAdmin):
    list_display = ('type', 'diagnostic')


class TreatmentAndRehabilationAdmin(TabbedTranslationAdmin):
    prepopulated_fields = {'slug': ('title',)}


class GuaranteeAdmin(TabbedTranslationAdmin):
    pass


class NewsAndBlogAdmin(TabbedTranslationAdmin):
    prepopulated_fields = {'slug': ('title',)}


class BlockNameAdmin(TabbedTranslationAdmin):
    pass


class CategoryServiceAdmin(TabbedTranslationAdmin):
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = [
        (None, {
            'fields': ['title_ru', 'title_en', 'title_kg', 'description_ru', 'description_en', 'description_kg',
                       'image', 'slug']}),
        # (_('Режим работы'), {
        #     'fields': ['working_day_ru', 'working_day_en', 'working_day_kg', 'day_off_ru', 'day_off_en', 'day_off_kg',
        #                'work_time_start', 'work_time_stop', 'lunch_time_start', 'lunch_time_stop']}),
    ]


class ServiceAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'category', 'cost', 'duration')
    prepopulated_fields = {'slug': ('title',)}


class CategoryPriceAdmin(TabbedTranslationAdmin):
    prepopulated_fields = {'slug': ('title',)}


class PriceAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'cost', 'duration', 'speciality', 'category')
    ordering = ('category',)
    list_filter = ('category',)

    class Media:
        js = [
            'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js',
            settings.STATIC_URL + 'admin/js/export_to_xls.js'
        ]


class InfoOnPricePageAdmin(TabbedTranslationAdmin):
    pass


class ContactInformationAdmin(TabbedTranslationAdmin):
    fieldsets = [
        (None, {'fields': ['address', 'phone', 'megacom', 'o', 'beeline', 'support_service']}),
        (_('Социальные сети'), {'fields': ['email', 'facebook', 'instagram', 'youtube']}),
        (_('Режим работы'), {
            'fields': ['working_day_ru', 'working_day_en', 'working_day_kg', 'day_off_ru', 'day_off_en', 'day_off_kg',
                       'work_time_start', 'work_time_stop', 'lunch_time_start', 'lunch_time_stop']}),
    ]


admin.site.register(models.Faq, FaqAdmin)
admin.site.register(models.Slider)
admin.site.register(models.Announcement, AnnouncementAdmin)
admin.site.register(models.Specialization, SpecializationAdmin)
admin.site.register(models.AboutClinic, AboutClinicAdmin)
admin.site.register(models.SpecialityDoctor, SpecialityDoctorAdmin)
admin.site.register(models.Doctor, DoctorAdmin)
admin.site.register(models.Advantage, AdvantageAdmin)
admin.site.register(models.Diagnostic, DiagnosticAdmin)
admin.site.register(models.DiagnosticType, DiagnosticTypeAdmin)
admin.site.register(models.TreatmentAndRehabilation, TreatmentAndRehabilationAdmin)
admin.site.register(models.Guarantee, GuaranteeAdmin)
admin.site.register(models.NewsAndBlog, NewsAndBlogAdmin)
admin.site.register(models.BlockName, BlockNameAdmin)
admin.site.register(models.CategoryService, CategoryServiceAdmin)
admin.site.register(models.Service, ServiceAdmin)
admin.site.register(models.CategoryPrice, CategoryPriceAdmin)
admin.site.register(models.Price, PriceAdmin)
admin.site.register(models.InfoOnPricePage, InfoOnPricePageAdmin)
admin.site.register(models.ContactInformation, ContactInformationAdmin)
admin.site.register(models.DownloadPriceList)
admin.site.register(models.Feedback)

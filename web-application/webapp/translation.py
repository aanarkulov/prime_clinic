from modeltranslation.translator import TranslationOptions, translator

from webapp import models


class FaqTranslation(TranslationOptions):
    fields = ('title', 'description',)


class AnnouncementTranslation(TranslationOptions):
    fields = ('title', 'description',)


class SpecializationTranslation(TranslationOptions):
    fields = ('icon_name', 'text')


class AboutClinicTranslation(TranslationOptions):
    fields = ('title', 'text', 'systematic', 'tasks', 'mission', 'vision', 'philosophy')


class SpecialityDoctorTranslation(TranslationOptions):
    fields = ('speciality',)


class DoctorTranslation(TranslationOptions):
    fields = ('about_doctor', 'education', 'experience')


class AdvantageTranslation(TranslationOptions):
    fields = ('title', 'text')


class DiagnosticTranslation(TranslationOptions):
    fields = ('title', 'text')


class DiagnosticTypeTranslation(TranslationOptions):
    fields = ('type', 'description')


class TreatmentAndRehabilationTranslation(TranslationOptions):
    fields = ('title', 'text')


class GuaranteeTranslation(TranslationOptions):
    fields = ('text',)


class NewsAndBlogTranslation(TranslationOptions):
    fields = ('title', 'description')


class BlockNameTranslation(TranslationOptions):
    fields = (
        'specialization', 'doctor', 'advantage', 'diagnostic', 'treatment_and_rehabilation', 'guarantee',
        'news_and_blog'
    )


class CategoryServiceTranslation(TranslationOptions):
    fields = ('title', 'description')


class ServiceTranslation(TranslationOptions):
    fields = ('title', 'description', 'cost', 'duration')


class CategoryPriceTranslation(TranslationOptions):
    fields = ('title',)


class PriceTranslation(TranslationOptions):
    fields = ('title', 'duration')


class InfoOnPricePageTranslation(TranslationOptions):
    fields = ('text',)


class ContactInformationTranslatiion(TranslationOptions):
    fields = ('address', 'working_day', 'day_off')


translator.register(models.Faq, FaqTranslation)
translator.register(models.Announcement, AnnouncementTranslation)
translator.register(models.Specialization, SpecializationTranslation)
translator.register(models.AboutClinic, AboutClinicTranslation)
translator.register(models.SpecialityDoctor, SpecialityDoctorTranslation)
translator.register(models.Doctor, DoctorTranslation)
translator.register(models.Advantage, AdvantageTranslation)
translator.register(models.Diagnostic, DiagnosticTranslation)
translator.register(models.DiagnosticType, DiagnosticTypeTranslation)
translator.register(models.TreatmentAndRehabilation, TreatmentAndRehabilationTranslation)
translator.register(models.Guarantee, GuaranteeTranslation)
translator.register(models.NewsAndBlog, NewsAndBlogTranslation)
translator.register(models.BlockName, BlockNameTranslation)
translator.register(models.CategoryService, CategoryServiceTranslation)
translator.register(models.Service, ServiceTranslation)
translator.register(models.CategoryPrice, CategoryPriceTranslation)
translator.register(models.Price, PriceTranslation)
translator.register(models.InfoOnPricePage, InfoOnPricePageTranslation)
translator.register(models.ContactInformation, ContactInformationTranslatiion)

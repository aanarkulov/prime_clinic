from django.db import models
from django.db.models import Q
from django.utils.text import Truncator
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from sorl.thumbnail import ImageField


class SearchQueryset(models.QuerySet):
    def parse_fields(self, model, query):
        exclude_fields = [
            'DateField', 'DateTimeField', 'ForeignKey', 'ManyToManyField', 'AutoField', 'FileField', 'ImageField',
            'ManyToOneRel', 'BooleanField', 'URLField'
        ]
        params = []

        for field in model._meta.get_fields():
            if field.__class__.__name__ not in exclude_fields:
                params.append(('' + field.name + '__icontains', query))

        return [Q(p) for p in params]

    def search(self, model, query=None):
        qs = self
        queries = self.parse_fields(model, query)
        or_lookup = queries.pop()
        for item in queries:
            or_lookup |= item

        if query is not None:
            qs = qs.filter(or_lookup).distinct()
        return qs


class SearchManager(models.Manager):
    def get_queryset(self):
        return SearchQueryset(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(self.model, query=query)


class Faq(models.Model):
    title = models.CharField(_('Заголовок'), max_length=255, blank=True)
    description = RichTextUploadingField(_('Описание'), blank=True)

    objects = SearchManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос-Ответ'
        verbose_name_plural = 'Вопросы-Ответы'


class Slider(models.Model):
    image = ImageField(_('Изображение'), upload_to='images/slider')

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайдер'


class Announcement(models.Model):
    title = models.CharField(_('Заголовок'), max_length=255)
    description = RichTextUploadingField(_('Описание'))
    more_info_link = models.URLField(_('Подробнее'), help_text=_('Вставьте ссылку для кнопки подробнее'))
    active = models.BooleanField(_('Активность'), default=True, help_text=_('Включить/Выключить показ'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Блок анонс')
        verbose_name_plural = _('Блок анонс')


class Specialization(models.Model):
    icon = models.ImageField(_('Иконка'), upload_to='icons/specializtion')
    icon_name = models.CharField(_('Название иконки'), max_length=255)
    text = models.TextField(_('Текст'), max_length=500, help_text=_('Максимальная длина текста - 500 символов.'),
                            blank=True)
    # image = ImageField(_('Изображение'), upload_to='images/diagnostics', default='')
    slug = models.SlugField(_('Ярлык'), unique=True)

    def __str__(self):
        return self.icon_name

    class Meta:
        verbose_name = _('Специализация')
        verbose_name_plural = _('Специализации')


class AboutClinic(models.Model):
    title = models.CharField(_('Заголовок'), max_length=255)
    background_image = ImageField(_('Фоновое изображение'), upload_to='images/different', blank=True)
    youtube_link = models.URLField(_('Youtube ссылка'), blank=True)
    text = RichTextField(_('Текст'))

    systematic = models.TextField(_('Системность'))
    tasks = models.TextField(_('Задачи'))
    mission = models.TextField(_('Миссия'))
    vision = models.TextField(_('Видение'))
    philosophy = models.TextField(_('Философия'))

    objects = SearchManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('О клинике')
        verbose_name_plural = _('О клинике')


class SpecialityDoctor(models.Model):
    speciality = models.CharField(_('Специальность'), max_length=255)
    icon = models.ImageField(_('Иконка'), upload_to='icons/specialitity_doctor', blank=True)

    def __str__(self):
        return self.speciality

    class Meta:
        verbose_name = _('Специальность врача')
        verbose_name_plural = _('Специальности врача')


class Doctor(models.Model):
    full_name = models.CharField('Имя и фамилия', max_length=255)
    speciality = models.ForeignKey(SpecialityDoctor, verbose_name=_('Специальность'))
    photo = ImageField(_('Фотография'), upload_to='images/doctors', blank=True)

    about_doctor = models.TextField(_('О враче'), blank=True)
    education = RichTextUploadingField(_('Образование'), blank=True)
    experience = RichTextUploadingField(_('Опыт работы'), blank=True)

    slug = models.SlugField(_('Ярлык'), unique=True)

    objects = SearchManager()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('Врач')
        verbose_name_plural = _('Врачи')


class Advantage(models.Model):
    title = models.CharField(_('Название преимущества'), max_length=255, blank=True)
    text = models.TextField(_('Текст'), max_length=255, help_text=_('Максимальная длина текста - 255 символов.'),
                            blank=True)
    icon = models.ImageField(_('Иконка'), upload_to='icons/advantages', blank=True)
    image = ImageField(_('Изображение'), upload_to='images/advantages', blank=True)
    slug = models.SlugField(_('Ярлык'), unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Преимущество клиники')
        verbose_name_plural = _('Преимущества клиники')


class Diagnostic(models.Model):
    title = models.CharField(_('Название диагностики'), max_length=255, blank=True)
    text = RichTextUploadingField(_('Текст'), blank=True)
    icon = models.ImageField(_('Иконка'), upload_to='icons/diagnostics', blank=True)
    image = ImageField(_('Изображение'), upload_to='images/diagnostics')
    slug = models.SlugField(_('Ярлык'), unique=True)

    objects = SearchManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Диагностика')
        verbose_name_plural = _('Диагностика')


class DiagnosticType(models.Model):
    diagnostic = models.ForeignKey(Diagnostic, verbose_name=_('Диагностика'), related_name='types')
    type = models.CharField(_('Название'), max_length=255, blank=True)
    description = RichTextUploadingField(_('Описание'), blank=True)

    objects = SearchManager()

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = _('Тип Диагностики')
        verbose_name_plural = _('Типы Диагностики')

    @property
    def filter_type(self):
        types = DiagnosticType.objects.filter(diagnostic__slug=self.diagnostic.slug)
        for i, obj in enumerate(types):
            if obj.type == self.type:
                return i
        return None


class TreatmentAndRehabilation(models.Model):
    title = models.CharField(_('Название методов лечения и реабилитации'), max_length=255, blank=True)
    text = RichTextUploadingField(_('Текст'), blank=True)
    icon = models.ImageField(_('Иконка'), upload_to='icons/treatment_and_rehabilation', blank=True)
    image = ImageField(_('Изображение'), upload_to='images/treatment_and_rehabilation')
    slug = models.SlugField(_('Ярлык'), unique=True)

    objects = SearchManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Лечение и реабилитация')
        verbose_name_plural = _('Лечение и реабилитация')


class Guarantee(models.Model):
    image = models.ImageField(_('Иконка или Изображение'), upload_to='images/guarantees', blank=True)
    text = models.CharField(_('Текст'), max_length=255, blank=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _('Гарантия')
        verbose_name_plural = _('Гарантии')


class NewsAndBlog(models.Model):
    title = models.CharField(_('Заголовок'), max_length=255, blank=True)
    description = RichTextUploadingField(_('Описание'), blank=True)
    image = ImageField(_('Изображение'), upload_to='images/news_and_blog')
    slug = models.SlugField(_('Ярлык'), unique=True)
    added_to = models.DateField(auto_now_add=True)

    objects = SearchManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Новость и блог')
        verbose_name_plural = _('Новости и блоги')


class BlockName(models.Model):
    specialization = models.CharField(_('Мы специализируемся на лечении заболеваний'), max_length=255, blank=True)
    doctor = models.CharField(_('Наши врачи'), max_length=255, blank=True)
    advantage = models.CharField(_('Преимущества клиники'), max_length=255, blank=True)
    diagnostic = models.CharField(_('Диагностика'), max_length=255, blank=True)
    treatment_and_rehabilation = models.CharField(_('Лечение и реабилитация'), max_length=255, blank=True)
    guarantee = models.CharField(_('Наши гарантии'), max_length=255, blank=True)
    news_and_blog = models.CharField(_('Новости и блог'), max_length=255, blank=True)

    def __str__(self):
        return 'Название блоков'

    class Meta:
        verbose_name = _('Название блока')
        verbose_name_plural = _('Название блоков')


class CategoryService(models.Model):
    title = models.CharField(_('Услуга'), max_length=255, blank=True)
    description = RichTextUploadingField(_('Описание'), blank=True)
    image = ImageField(_('Изображение'), upload_to='images/services')

    # working_day = models.CharField(_('Рабочие дни'), max_length=255, blank=True)
    # day_off = models.CharField(_('Выходные дни'), max_length=255, blank=True)
    # work_time_start = models.TimeField(_('Робочее время с:'), default='9:00')
    # work_time_stop = models.TimeField(_('до:'), default='18:00')
    # lunch_time_start = models.TimeField(_('Обед с:'), default='12:00')
    # lunch_time_stop = models.TimeField(_('до:'), default='13:00')

    slug = models.SlugField(_('Ярлык'), unique=True)

    objects = SearchManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Категория Услуг')
        verbose_name_plural = _('Категории Услуг')


class Service(models.Model):
    category = models.ForeignKey(CategoryService, verbose_name=_('Категория'), related_name='services')
    title = models.CharField(_('Название подкатегория'), max_length=255, blank=True)
    description = RichTextUploadingField(_('Описание'), blank=True)
    cost = models.CharField(_('Стоимость'), max_length=255, blank=True)
    duration = models.CharField(_('Продолжительность'), max_length=255, blank=True)
    slug = models.SlugField(_('Ярлык'), unique=True)

    objects = SearchManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Услуга')
        verbose_name_plural = _('Услуги')


class CategoryPrice(models.Model):
    title = models.CharField(_('Название категория'), max_length=255, blank=True)
    slug = models.SlugField(_('Ярлык'), unique=True)

    objects = SearchManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Категория Цен')
        verbose_name_plural = _('Категории Цен')


class Price(models.Model):
    category = models.ForeignKey(CategoryPrice, verbose_name=_('Категория'), related_name='price_category')
    speciality = models.ForeignKey(SpecialityDoctor, verbose_name=_('Специальности'), related_name='price_speciality',
                                   null=True, blank=True)
    title = models.CharField(_('Название услуги'), max_length=255, blank=True)
    cost = models.PositiveIntegerField(_('Стоимость (сом)'))
    duration = models.CharField(_('Длительность'), max_length=255, blank=True)

    objects = SearchManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Цена')
        verbose_name_plural = _('Цены')


class DownloadPriceList(models.Model):
    file = models.FileField(_('Файл'), upload_to='files')

    def __str__(self):
        return str(self.file).split("files/")[1]

    class Meta:
        verbose_name = _('Прайслист для загрузки')
        verbose_name_plural = _('Прайслист для загрузки')


class InfoOnPricePage(models.Model):
    text = RichTextUploadingField(_('Текст'), blank=True)

    objects = SearchManager()

    def __str__(self):
        truncated_text = Truncator(self.text)
        return truncated_text.chars(30)[3:]

    class Meta:
        verbose_name = _('Инфо на странице цены')
        verbose_name_plural = _('Инфо на странице цены')


class ContactInformation(models.Model):
    phone = models.CharField(_('Телефон'), max_length=255, blank=True)
    megacom = models.CharField('MegaCom', max_length=255, blank=True)
    o = models.CharField('O!', max_length=255, blank=True)
    beeline = models.CharField('Beeline', max_length=255, blank=True)
    support_service = models.CharField(_('Круглосуточная служба поддержки:'), max_length=255, blank=True)

    email = models.EmailField(_('Email адрес'), default='office@prime.kg', blank=True)
    facebook = models.URLField(default='https://www.facebook.com/')
    instagram = models.URLField(default='https://www.instagram.com/')
    youtube = models.URLField(default='https://www.youtube.com/')

    address = models.CharField(_('Адрес'), max_length=255, blank=True)

    working_day = models.CharField(_('Рабочие дни'), max_length=255, blank=True)
    day_off = models.CharField(_('Выходные дни'), max_length=255, blank=True)
    work_time_start = models.TimeField(_('Робочее время с:'), default='9:00')
    work_time_stop = models.TimeField(_('до:'), default='18:00')
    lunch_time_start = models.TimeField(_('Обед с:'), default='12:00')
    lunch_time_stop = models.TimeField(_('до:'), default='13:00')

    def __str__(self):
        return str(_('Контактная информация'))

    class Meta:
        verbose_name = _('Контактная информация')
        verbose_name_plural = _('Контактная информация')


class Feedback(models.Model):
    name = models.CharField(_('Имя'), max_length=300)
    subject = models.CharField(_('Тема'), max_length=255, blank=True)
    phone = models.CharField(_('Телефон'), max_length=255)
    email = models.CharField('E-mail', max_length=255)
    message = models.TextField(_('Сообщение'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Обратная связь')
        verbose_name_plural = _('Обратные связи')

# class CallToActionButton(models.Model):
#     class Meta:
#         verbose_name = _('СТА кнопка')
#         verbose_name_plural = _('СТА кнопки')
#
#     name = models.CharField(_('Название СТА кнопки'), max_length=255)
#
#     def __str__(self):
#         return self.name


# call_to_action = models.ForeignKey(CallToActionButton, verbose_name=_('СТА кнопка'))
# call_to_action_link = models.URLField(_('Ссылка СТА кнопки'), blank=True)

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-02 05:29
from __future__ import unicode_literals

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutClinic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Заголовок')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Заголовок')),
                ('title_kg', models.CharField(max_length=255, null=True, verbose_name='Заголовок')),
                ('background_image', sorl.thumbnail.fields.ImageField(blank=True, upload_to='images/different', verbose_name='Фоновое изображение')),
                ('youtube_link', models.URLField(blank=True, verbose_name='Youtube ссылка')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Текст')),
                ('text_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Текст')),
                ('text_en', ckeditor.fields.RichTextField(null=True, verbose_name='Текст')),
                ('text_kg', ckeditor.fields.RichTextField(null=True, verbose_name='Текст')),
                ('systematic', models.TextField(verbose_name='Системность')),
                ('systematic_ru', models.TextField(null=True, verbose_name='Системность')),
                ('systematic_en', models.TextField(null=True, verbose_name='Системность')),
                ('systematic_kg', models.TextField(null=True, verbose_name='Системность')),
                ('tasks', models.TextField(verbose_name='Задачи')),
                ('tasks_ru', models.TextField(null=True, verbose_name='Задачи')),
                ('tasks_en', models.TextField(null=True, verbose_name='Задачи')),
                ('tasks_kg', models.TextField(null=True, verbose_name='Задачи')),
                ('mission', models.TextField(verbose_name='Миссия')),
                ('mission_ru', models.TextField(null=True, verbose_name='Миссия')),
                ('mission_en', models.TextField(null=True, verbose_name='Миссия')),
                ('mission_kg', models.TextField(null=True, verbose_name='Миссия')),
                ('vision', models.TextField(verbose_name='Видение')),
                ('vision_ru', models.TextField(null=True, verbose_name='Видение')),
                ('vision_en', models.TextField(null=True, verbose_name='Видение')),
                ('vision_kg', models.TextField(null=True, verbose_name='Видение')),
                ('philosophy', models.TextField(verbose_name='Философия')),
                ('philosophy_ru', models.TextField(null=True, verbose_name='Философия')),
                ('philosophy_en', models.TextField(null=True, verbose_name='Философия')),
                ('philosophy_kg', models.TextField(null=True, verbose_name='Философия')),
            ],
            options={
                'verbose_name': 'О клинике',
                'verbose_name_plural': 'О клинике',
            },
        ),
        migrations.CreateModel(
            name='Advantage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Название преимущества')),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название преимущества')),
                ('title_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название преимущества')),
                ('title_kg', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название преимущества')),
                ('text', models.TextField(blank=True, help_text='Максимальная длина текста - 255 символов.', max_length=255, verbose_name='Текст')),
                ('text_ru', models.TextField(blank=True, help_text='Максимальная длина текста - 255 символов.', max_length=255, null=True, verbose_name='Текст')),
                ('text_en', models.TextField(blank=True, help_text='Максимальная длина текста - 255 символов.', max_length=255, null=True, verbose_name='Текст')),
                ('text_kg', models.TextField(blank=True, help_text='Максимальная длина текста - 255 символов.', max_length=255, null=True, verbose_name='Текст')),
                ('icon', models.ImageField(blank=True, upload_to='icons/advantages', verbose_name='Иконка')),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, upload_to='images/advantages', verbose_name='Изображение')),
                ('slug', models.SlugField(unique=True, verbose_name='Ярлык')),
            ],
            options={
                'verbose_name': 'Преимущество клиники',
                'verbose_name_plural': 'Преимущества клиники',
            },
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Заголовок')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Заголовок')),
                ('title_kg', models.CharField(max_length=255, null=True, verbose_name='Заголовок')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Описание')),
                ('description_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Описание')),
                ('description_kg', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Описание')),
                ('more_info_link', models.URLField(help_text='Вставьте ссылку для кнопки подробнее', verbose_name='Подробнее')),
                ('active', models.BooleanField(default=True, help_text='Включить/Выключить показ', verbose_name='Активность')),
            ],
            options={
                'verbose_name': 'Блок анонс',
                'verbose_name_plural': 'Блок анонс',
            },
        ),
        migrations.CreateModel(
            name='BlockName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.CharField(blank=True, max_length=255, verbose_name='Мы специализируемся на лечении заболеваний')),
                ('specialization_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Мы специализируемся на лечении заболеваний')),
                ('specialization_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Мы специализируемся на лечении заболеваний')),
                ('specialization_kg', models.CharField(blank=True, max_length=255, null=True, verbose_name='Мы специализируемся на лечении заболеваний')),
                ('doctor', models.CharField(blank=True, max_length=255, verbose_name='Наши врачи')),
                ('doctor_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наши врачи')),
                ('doctor_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наши врачи')),
                ('doctor_kg', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наши врачи')),
                ('advantage', models.CharField(blank=True, max_length=255, verbose_name='Преимущества клиники')),
                ('advantage_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Преимущества клиники')),
                ('advantage_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Преимущества клиники')),
                ('advantage_kg', models.CharField(blank=True, max_length=255, null=True, verbose_name='Преимущества клиники')),
                ('diagnostic', models.CharField(blank=True, max_length=255, verbose_name='Диагностика')),
                ('diagnostic_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Диагностика')),
                ('diagnostic_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Диагностика')),
                ('diagnostic_kg', models.CharField(blank=True, max_length=255, null=True, verbose_name='Диагностика')),
                ('treatment_and_rehabilation', models.CharField(blank=True, max_length=255, verbose_name='Лечение и реабилитация')),
                ('treatment_and_rehabilation_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Лечение и реабилитация')),
                ('treatment_and_rehabilation_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Лечение и реабилитация')),
                ('treatment_and_rehabilation_kg', models.CharField(blank=True, max_length=255, null=True, verbose_name='Лечение и реабилитация')),
                ('guarantee', models.CharField(blank=True, max_length=255, verbose_name='Наши гарантии')),
                ('guarantee_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наши гарантии')),
                ('guarantee_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наши гарантии')),
                ('guarantee_kg', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наши гарантии')),
                ('news_and_blog', models.CharField(blank=True, max_length=255, verbose_name='Новости и блог')),
                ('news_and_blog_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Новости и блог')),
                ('news_and_blog_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Новости и блог')),
                ('news_and_blog_kg', models.CharField(blank=True, max_length=255, null=True, verbose_name='Новости и блог')),
            ],
            options={
                'verbose_name': 'Название блока',
                'verbose_name_plural': 'Название блоков',
            },
        ),
        migrations.CreateModel(
            name='CategoryPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Название категория')),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название категория')),
                ('title_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название категория')),
                ('title_kg', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название категория')),
                ('slug', models.SlugField(unique=True, verbose_name='Ярлык')),
            ],
            options={
                'verbose_name': 'Категория Цен',
                'verbose_name_plural': 'Категории Цен',
            },
        ),
        migrations.CreateModel(
            name='CategoryService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Услуга')),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Услуга')),
                ('title_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Услуга')),
                ('title_kg', models.CharField(blank=True, max_length=255, null=True, verbose_name='Услуга')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Описание')),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('description_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('description_kg', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='images/services', verbose_name='Изображение')),
                ('slug', models.SlugField(unique=True, verbose_name='Ярлык')),
            ],
            options={
                'verbose_name': 'Категория Услуг',
                'verbose_name_plural': 'Категории Услуг',
            },
        ),
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=255, verbose_name='Телефон')),
                ('megacom', models.CharField(blank=True, max_length=255, verbose_name='MegaCom')),
                ('o', models.CharField(blank=True, max_length=255, verbose_name='O!')),
                ('beeline', models.CharField(blank=True, max_length=255, verbose_name='Beeline')),
                ('support_service', models.CharField(blank=True, max_length=255, verbose_name='Круглосуточная служба поддержки:')),
                ('email', models.EmailField(blank=True, default='office@prime.kg', max_length=254, verbose_name='Email адрес')),
                ('facebook', models.URLField(default='https://www.facebook.com/')),
                ('instagram', models.URLField(default='https://www.instagram.com/')),
                ('youtube', models.URLField(default='https://www.youtube.com/')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Адрес')),
                ('address_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('address_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('address_kg', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('working_day', models.CharField(blank=True, max_length=255, verbose_name='Рабочие дни')),
                ('working_day_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Рабочие дни')),
                ('working_day_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Рабочие дни')),
                ('working_day_kg', models.CharField(blank=True, max_length=255, null=True, verbose_name='Рабочие дни')),
                ('day_off', models.CharField(blank=True, max_length=255, verbose_name='Выходные дни')),
                ('day_off_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Выходные дни')),
                ('day_off_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Выходные дни')),
                ('day_off_kg', models.CharField(blank=True, max_length=255, null=True, verbose_name='Выходные дни')),
                ('work_time_start', models.TimeField(default='9:00', verbose_name='Робочее время с:')),
                ('work_time_stop', models.TimeField(default='18:00', verbose_name='до:')),
                ('lunch_time_start', models.TimeField(default='12:00', verbose_name='Обед с:')),
                ('lunch_time_stop', models.TimeField(default='13:00', verbose_name='до:')),
            ],
            options={
                'verbose_name': 'Контактная информация',
                'verbose_name_plural': 'Контактная информация',
            },
        ),
        migrations.CreateModel(
            name='Diagnostic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Название диагностики')),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название диагностики')),
                ('title_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название диагностики')),
                ('title_kg', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название диагностики')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Текст')),
                ('text_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст')),
                ('text_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст')),
                ('text_kg', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст')),
                ('icon', models.ImageField(blank=True, upload_to='icons/diagnostics', verbose_name='Иконка')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='images/diagnostics', verbose_name='Изображение')),
                ('slug', models.SlugField(unique=True, verbose_name='Ярлык')),
            ],
            options={
                'verbose_name': 'Диагностика',
                'verbose_name_plural': 'Диагностика',
            },
        ),
        migrations.CreateModel(
            name='DiagnosticType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=255, verbose_name='Название')),
                ('type_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('type_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('type_kg', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Описание')),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('description_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('description_kg', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('diagnostic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='types', to='webapp.Diagnostic', verbose_name='Диагностика')),
            ],
            options={
                'verbose_name': 'Тип Диагностики',
                'verbose_name_plural': 'Типы Диагностики',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='Имя и фамилия')),
                ('photo', sorl.thumbnail.fields.ImageField(blank=True, upload_to='images/doctors', verbose_name='Фотография')),
                ('about_doctor', models.TextField(blank=True, verbose_name='О враче')),
                ('about_doctor_ru', models.TextField(blank=True, null=True, verbose_name='О враче')),
                ('about_doctor_en', models.TextField(blank=True, null=True, verbose_name='О враче')),
                ('about_doctor_kg', models.TextField(blank=True, null=True, verbose_name='О враче')),
                ('education', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Образование')),
                ('education_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Образование')),
                ('education_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Образование')),
                ('education_kg', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Образование')),
                ('experience', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Опыт работы')),
                ('experience_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Опыт работы')),
                ('experience_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Опыт работы')),
                ('experience_kg', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Опыт работы')),
                ('slug', models.SlugField(unique=True, verbose_name='Ярлык')),
            ],
            options={
                'verbose_name': 'Врач',
                'verbose_name_plural': 'Врачи',
            },
        ),
        migrations.CreateModel(
            name='DownloadPriceList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files', verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Прайслист для загрузки',
                'verbose_name_plural': 'Прайслист для загрузки',
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Заголовок')),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('title_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('title_kg', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Описание')),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('description_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('description_kg', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Вопрос-Ответ',
                'verbose_name_plural': 'Вопросы-Ответы',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Имя')),
                ('subject', models.CharField(blank=True, max_length=255, verbose_name='Тема')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефон')),
                ('email', models.CharField(max_length=255, verbose_name='E-mail')),
                ('message', models.TextField(verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратные связи',
            },
        ),
        migrations.CreateModel(
            name='Guarantee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/guarantees', verbose_name='Иконка или Изображение')),
                ('text', models.CharField(blank=True, max_length=255, verbose_name='Текст')),
                ('text_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст')),
                ('text_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст')),
                ('text_kg', models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Гарантия',
                'verbose_name_plural': 'Гарантии',
            },
        ),
        migrations.CreateModel(
            name='InfoOnPricePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Текст')),
                ('text_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст')),
                ('text_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст')),
                ('text_kg', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Инфо на странице цены',
                'verbose_name_plural': 'Инфо на странице цены',
            },
        ),
        migrations.CreateModel(
            name='NewsAndBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Заголовок')),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('title_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('title_kg', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Описание')),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('description_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('description_kg', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='images/news_and_blog', verbose_name='Изображение')),
                ('slug', models.SlugField(unique=True, verbose_name='Ярлык')),
                ('added_to', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Новость и блог',
                'verbose_name_plural': 'Новости и блоги',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Название услуги')),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название услуги')),
                ('title_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название услуги')),
                ('title_kg', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название услуги')),
                ('cost', models.PositiveIntegerField(verbose_name='Стоимость (сом)')),
                ('duration', models.CharField(blank=True, max_length=255, verbose_name='Длительность')),
                ('duration_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Длительность')),
                ('duration_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Длительность')),
                ('duration_kg', models.CharField(blank=True, max_length=255, null=True, verbose_name='Длительность')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price_category', to='webapp.CategoryPrice', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Цена',
                'verbose_name_plural': 'Цены',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Название подкатегория')),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название подкатегория')),
                ('title_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название подкатегория')),
                ('title_kg', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название подкатегория')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Описание')),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('description_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('description_kg', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('cost', models.CharField(blank=True, max_length=255, verbose_name='Стоимость')),
                ('cost_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Стоимость')),
                ('cost_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Стоимость')),
                ('cost_kg', models.CharField(blank=True, max_length=255, null=True, verbose_name='Стоимость')),
                ('duration', models.CharField(blank=True, max_length=255, verbose_name='Продолжительность')),
                ('duration_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Продолжительность')),
                ('duration_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Продолжительность')),
                ('duration_kg', models.CharField(blank=True, max_length=255, null=True, verbose_name='Продолжительность')),
                ('slug', models.SlugField(unique=True, verbose_name='Ярлык')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='webapp.CategoryService', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='images/slider', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайдер',
            },
        ),
        migrations.CreateModel(
            name='SpecialityDoctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speciality', models.CharField(max_length=255, verbose_name='Специальность')),
                ('speciality_ru', models.CharField(max_length=255, null=True, verbose_name='Специальность')),
                ('speciality_en', models.CharField(max_length=255, null=True, verbose_name='Специальность')),
                ('speciality_kg', models.CharField(max_length=255, null=True, verbose_name='Специальность')),
                ('icon', models.ImageField(blank=True, upload_to='icons/specialitity_doctor', verbose_name='Иконка')),
            ],
            options={
                'verbose_name': 'Специальность врача',
                'verbose_name_plural': 'Специальности врача',
            },
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='icons/specializtion', verbose_name='Иконка')),
                ('icon_name', models.CharField(max_length=255, verbose_name='Название иконки')),
                ('icon_name_ru', models.CharField(max_length=255, null=True, verbose_name='Название иконки')),
                ('icon_name_en', models.CharField(max_length=255, null=True, verbose_name='Название иконки')),
                ('icon_name_kg', models.CharField(max_length=255, null=True, verbose_name='Название иконки')),
                ('text', models.TextField(blank=True, help_text='Максимальная длина текста - 500 символов.', max_length=500, verbose_name='Текст')),
                ('text_ru', models.TextField(blank=True, help_text='Максимальная длина текста - 500 символов.', max_length=500, null=True, verbose_name='Текст')),
                ('text_en', models.TextField(blank=True, help_text='Максимальная длина текста - 500 символов.', max_length=500, null=True, verbose_name='Текст')),
                ('text_kg', models.TextField(blank=True, help_text='Максимальная длина текста - 500 символов.', max_length=500, null=True, verbose_name='Текст')),
                ('slug', models.SlugField(unique=True, verbose_name='Ярлык')),
            ],
            options={
                'verbose_name': 'Специализация',
                'verbose_name_plural': 'Специализации',
            },
        ),
        migrations.CreateModel(
            name='TreatmentAndRehabilation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Название методов лечения и реабилитации')),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название методов лечения и реабилитации')),
                ('title_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название методов лечения и реабилитации')),
                ('title_kg', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название методов лечения и реабилитации')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Текст')),
                ('text_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст')),
                ('text_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст')),
                ('text_kg', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст')),
                ('icon', models.ImageField(blank=True, upload_to='icons/treatment_and_rehabilation', verbose_name='Иконка')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='images/treatment_and_rehabilation', verbose_name='Изображение')),
                ('slug', models.SlugField(unique=True, verbose_name='Ярлык')),
            ],
            options={
                'verbose_name': 'Лечение и реабилитация',
                'verbose_name_plural': 'Лечение и реабилитация',
            },
        ),
        migrations.AddField(
            model_name='price',
            name='speciality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='price_speciality', to='webapp.SpecialityDoctor', verbose_name='Специальности'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='speciality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.SpecialityDoctor', verbose_name='Специальность'),
        ),
    ]

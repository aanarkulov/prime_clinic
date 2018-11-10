from itertools import chain

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.utils.translation import ugettext_lazy as _

from webapp import models
from webapp.filters import DoctorFilter, DiagnosticTypeFilter
from webapp.forms import FeedbackForm


class IndexListView(ListView):
    template_name = 'webapp/index.html'
    context_object_name = 'results'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if 'search' in dict(self.request.GET):
            self.template_name = 'webapp/search.html'
            query = self.request.GET.get('search')
            title = _('Поиск')
            if query:
                title += ': ' + query
            context['title'] = title
        else:
            context['title'] = _('Главная')
            context['announcement'] = models.Announcement.objects.first()
            context['slides'] = models.Slider.objects.all()
            context['specializations'] = models.Specialization.objects.all()
            about_clinic = models.AboutClinic.objects.first()
            youtube_key = about_clinic.youtube_link.split("?v=")[1]
            context['about_clinic'] = about_clinic
            context['youtube_key'] = youtube_key
            context['doctors'] = models.Doctor.objects.all()
            context['advantages'] = models.Advantage.objects.all()
            context['treatment_and_rehabilation'] = models.TreatmentAndRehabilation.objects.all()
            context['guarantees'] = models.Guarantee.objects.all()
            context['news_and_blog'] = models.NewsAndBlog.objects.all()
            context['block_name'] = models.BlockName.objects.first()
        return context

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            faq_result = models.Faq.objects.search(query)
            about_clinic_result = models.AboutClinic.objects.search(query)
            doctor_result = models.Doctor.objects.search(query)
            diagnostic_result = models.Diagnostic.objects.search(query)
            diagnostic_type_result = models.DiagnosticType.objects.search(query)
            treatment_and_rehabilation = models.TreatmentAndRehabilation.objects.search(query)
            news_and_blog_result = models.NewsAndBlog.objects.search(query)
            category_service_result = models.CategoryService.objects.search(query)
            service_result = models.Service.objects.search(query)
            category_price_result = models.CategoryPrice.objects.search(query)
            price_result = models.Price.objects.search(query)
            info_on_price_page_result = models.InfoOnPricePage.objects.search(query)
            queryset_chain = chain(
                faq_result,
                about_clinic_result,
                doctor_result,
                diagnostic_result,
                diagnostic_type_result,
                treatment_and_rehabilation,
                news_and_blog_result,
                category_service_result,
                service_result,
                category_price_result,
                price_result,
                info_on_price_page_result,

            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            return qs

        return None


class FaqListView(ListView):
    template_name = 'webapp/faq.html'
    model = models.Faq
    context_object_name = 'faqs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Вопросы-Ответы')
        return context


class AboutClinicListView(ListView):
    template_name = 'webapp/about-us.html'
    model = models.Doctor
    context_object_name = 'doctors'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('О клинике')
        about_clinic = models.AboutClinic.objects.first()
        youtube_key = about_clinic.youtube_link.split("?v=")[1]
        context['about_clinic'] = about_clinic
        context['youtube_key'] = youtube_key
        return context


class ServicesTemplateView(TemplateView):
    template_name = 'webapp/services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Услуги')
        return context


class CategoryServiceDetailView(DetailView):
    template_name = 'webapp/services-inner.html'
    model = models.CategoryService
    context_object_name = 'category_service'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = get_object_or_404(self.model, slug=self.kwargs['slug']).title
        return context


class ServiceDetailView(DetailView):
    template_name = 'webapp/service.html'
    model = models.Service
    context_object_name = 'service'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = get_object_or_404(self.model, slug=self.kwargs['slug']).title
        return context


class DoctorListView(ListView):
    template_name = 'webapp/doctors.html'
    model = models.Doctor
    filterset_class = DoctorFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Врачи')
        context['doctor_form'] = self.filterset_class(self.request.GET, queryset=self.model.objects.all())
        return context


class DoctorDetailView(DetailView):
    template_name = 'webapp/doctor.html'
    model = models.Doctor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = get_object_or_404(self.model, slug=self.kwargs['slug']).full_name
        return context


class TreatmentListtView(ListView):
    template_name = 'webapp/treatment.html'
    model = models.TreatmentAndRehabilation
    context_object_name = 'treatment_and_rehabilation'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Лечение')
        return context


class TreatmentDetailView(DetailView):
    template_name = 'webapp/treatment-inner.html'
    model = models.TreatmentAndRehabilation
    context_object_name = 'treatment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = get_object_or_404(self.model, slug=self.kwargs['slug']).title
        context['treatment_and_rehabilation'] = self.model.objects.all()
        return context


class DiagnosticsTemplateView(TemplateView):
    template_name = 'webapp/diagnostics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Диагностика')
        return context


class DiagnosticDetailView(DetailView):
    template_name = 'webapp/diagnostic.html'
    model = models.Diagnostic
    filterset_class = DiagnosticTypeFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        context['title'] = get_object_or_404(self.model, slug=slug).title
        first_type = models.Diagnostic.objects.get(slug=slug).types.first()
        context['filter_type'] = self.filterset_class(self.request.GET,
                                                      queryset=models.DiagnosticType.objects.filter(pk=first_type.pk))
        return context


class PricePageView(TemplateView):
    template_name = 'webapp/prices.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = models.CategoryPrice.objects.first()
        context['title'] = queryset.title
        context['info'] = models.InfoOnPricePage.objects.first()
        context['price_categories'] = models.CategoryPrice.objects.all()
        context['first'] = models.Price.objects.filter(category=queryset, speciality=None)
        exist = models.Price.objects.filter(category=queryset, speciality=True)
        if exist:
            context['second'] = models.SpecialityDoctor.objects.all()
        context['download'] = models.DownloadPriceList.objects.first()
        context['slug'] = queryset.slug
        return context


class PricesView(DetailView):
    template_name = 'webapp/prices.html'
    model = models.CategoryPrice
    context_object_name = 'price_category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.request.resolver_match.kwargs.get('slug')
        queryset = self.model.objects.get(slug=slug)
        context['title'] = queryset.title
        context['info'] = models.InfoOnPricePage.objects.first()
        context['price_categories'] = self.model.objects.all()
        context['first'] = models.Price.objects.filter(category=queryset, speciality=None)
        exist = models.Price.objects.filter(category=queryset, speciality=True)
        if exist:
            context['second'] = models.SpecialityDoctor.objects.all()
        context['download'] = models.DownloadPriceList.objects.first()
        return context


class ContactsFormView(FormView):
    template_name = 'webapp/contacts.html'
    form_class = FeedbackForm

    def get_success_url(self):
        return self.request.META['HTTP_REFERER']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Контакты')
        return context

    def form_valid(self, form):
        form.save()
        if self.request.is_ajax():
            return JsonResponse(dict(success=True,
                                     message=_('Форма успешно отправлено')))
        return super().form_valid(form)


class NewsAndBlogDetailView(DetailView):
    template_name = 'webapp/news-inner.html'
    model = models.NewsAndBlog
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        context['title'] = get_object_or_404(self.model, slug=slug).title
        context['news_and_blog'] = self.model.objects.all()
        return context

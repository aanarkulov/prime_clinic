from django.conf.urls import url

from webapp import views

app_name = 'webapp'
urlpatterns = [
    url(r'^$', views.IndexListView.as_view(), name='index'),
    url(r'^faq/$', views.FaqListView.as_view(), name='faq'),
    url(r'^about-clinic/$', views.AboutClinicListView.as_view(), name='about_clinic'),
    url(r'^services/$', views.ServicesTemplateView.as_view(), name='services'),
    url(r'^services/category/(?P<slug>[\w-]+)/$', views.CategoryServiceDetailView.as_view(), name='category_service'),
    url(r'^services/service/(?P<slug>[\w-]+)/$', views.ServiceDetailView.as_view(), name='service'),
    url(r'^doctors/$', views.DoctorListView.as_view(), name='doctors'),
    url(r'^doctors/(?P<slug>[\w-]+)/$', views.DoctorDetailView.as_view(), name='doctor'),
    url(r'^treatment/$', views.TreatmentListtView.as_view(), name='treatment'),
    url(r'^treatment/(?P<slug>[\w-]+)/$', views.TreatmentDetailView.as_view(), name='treatment_inner'),
    url(r'^diagnostics/$', views.DiagnosticsTemplateView.as_view(), name='diagnostics'),
    url(r'^diagnostics/(?P<slug>[\w-]+)/', views.DiagnosticDetailView.as_view(), name='diagnostic'),
    url(r'^prices/$', views.PricePageView.as_view(), name='prices_page'),
    url(r'^prices/(?P<slug>[\w-]+)/$', views.PricesView.as_view(), name='prices'),
    url(r'^contacts/$', views.ContactsFormView.as_view(), name='contacts'),
    url(r'^news-and-blog/(?P<slug>[\w-]+)/$', views.NewsAndBlogDetailView.as_view(), name='news_and_blog'),
]

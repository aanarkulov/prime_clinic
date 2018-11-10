import django_filters

from webapp.models import Doctor, DiagnosticType


class DoctorFilter(django_filters.FilterSet):
    class Meta:
        model = Doctor
        fields = ('speciality', 'full_name')


class DiagnosticTypeFilter(django_filters.FilterSet):
    type = django_filters.CharFilter(method='filter_type')

    def filter_type(self, queryset, name, value):
        if value:
            slug = ''
            for i in queryset:
                slug = i.diagnostic.slug
            value = int(value)
            types = DiagnosticType.objects.filter(diagnostic__slug=slug)
            for i, type in enumerate(types):
                if i == value:
                    return DiagnosticType.objects.filter(pk=type.pk)
            return DiagnosticType.objects.filter(pk=value)

    class Meta:
        model = DiagnosticType
        fields = ('type',)

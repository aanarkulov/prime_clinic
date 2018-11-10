from webapp.models import Diagnostic, CategoryService, ContactInformation


def getting_different_info(request):
    services = CategoryService.objects.all()
    diagnostics = Diagnostic.objects.all()
    contact_info = ContactInformation.objects.first()
    return locals()

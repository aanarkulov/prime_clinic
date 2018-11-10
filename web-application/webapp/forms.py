from django import forms
from django.utils.translation import ugettext_lazy as _

from webapp.models import Feedback


class FeedbackForm(forms.ModelForm):
    phone = forms.CharField(
        label=_('Телефон'),
        widget=forms.TextInput(
            attrs={'class': 'phone_us', 'placeholder': '(996) ___-__-__-__'}
        )
    )

    message = forms.CharField(
        label=_('Сообщение'),
        widget=forms.Textarea(
            attrs={'rows': 5},
        ),
        max_length=4000,
        help_text=_('Максимальная длина текста - 4000.'),

    )

    class Meta:
        model = Feedback
        fields = ('name', 'subject', 'phone', 'email', 'message')

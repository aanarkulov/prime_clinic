from django import template
from django.utils.safestring import SafeText

register = template.Library()


@register.filter
def field_type(bound_field):
    return bound_field.field.widget.__class__.__name__


@register.filter
def input_class(bound_field):
    css_class = ''
    if bound_field.form.is_bound:
        if bound_field.errors:
            css_class = 'is-invalid'
        elif field_type(bound_field) != 'PasswordInput':
            css_class = 'is-valid'

    if field_type(bound_field) == 'Textarea':
        result = 'uk-textarea {}'.format(css_class)
    else:
        result = 'uk-input {}'.format(css_class)
    return result


@register.filter
def add_require_symbol(bound_field):
    if bound_field.field.required:
        str_label = bound_field.label_tag()
        s = ''
        for i in str_label:
            if i == (str_label[len(str_label) - 9]):
                s += ': <span>*</span>'
            else:
                s += i
        result = SafeText(s)
        return result
    return bound_field.label_tag()


@register.filter
def get_class(bound_field):
    result = ''
    if field_type(bound_field) == 'Textarea':
        result = 'uk-width-1-1@m'
    return result

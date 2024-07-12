from django import template

register = template.Library()

@register.filter(name='first_n_words')
def first_n_words(value, num_words):
    words = value.split()[:num_words]
    return ' '.join(words) + '...'
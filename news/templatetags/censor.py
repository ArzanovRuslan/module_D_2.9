from django import template

register = template.Library()  # если мы не зарегистрируем наши фильтры, то Django никогда не узнает, где именно их искать и фильтры потеряются

@register.filter(name='censor_mat')  # регистрируем наш фильтр под именем censor_mat, чтоб django понимал, что это именно фильтр, а не простая функция
def censor_mat(value):
    words = ['матерное слово 1', 'матерное слово 2', 'матерное слово 3']
    for index in words:
        if index in value:
            value = value.replase(index, '***')
    return (value)

from django import template
register = template.Library()

"""여러 템플릿에서 재사용하기 위한 커스텀 템플릿 태그 모음"""

# 사용법
"""
{% load common_tags %}

{% get_model_fields my_instance as fields %}
{% for field, value in fields %}
    <p>{{ field }}: {{ value }}</p>
{% endfor %}
"""


@register.simple_tag
def get_model_fields(instance):
    """pk를 제외한 필드 목록을 템플릿에서 동적으로 불러오는 기능"""
    """
    {% load common_tags %}

    {% get_model_fields <my_instance> as fields %}
    {% for field, value in fields %}
        <p>{{ field }}: {{ value }}</p>
    {% endfor %}
    """
    return [(field.name, field.value_to_string(instance)) for field in instance._meta.fields[1:]]

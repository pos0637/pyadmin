# -*- coding: UTF-8 -*-

from django.db import models


class {{entity.name}}(models.Model):
{% for field in entity.fields %}
    {{field.name}} = models.{{field.getType()}}({{field.getOptions()}})
{% endfor %}

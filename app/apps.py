from django.apps import AppConfig
from material.frontend.templatetags.material_frontend import verbose_name


class AppConfig(AppConfig):
    name = 'app'
    verbose_name = 'Aplicações'

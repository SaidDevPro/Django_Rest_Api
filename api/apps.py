"""Импортируем джанго конфиги"""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """_summary_

    Args:
        AppConfig (_type_): _description_
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "api"

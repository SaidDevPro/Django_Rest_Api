"""Импорт моделей из Django"""

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Пользовательская модель, расширяющая стандартную модель пользователя Django
    # Определение типов пользователей: поставщик или потребитель"""

    USER_TYPE_CHOICES = [
        ("supplier", "Supplier"),  # Значение для поставщика
        ("consumer", "Consumer"),  # Значение для потребителя
    ]
    # Поле для хранения типа пользователя
    user_type = models.CharField(
        max_length=10, choices=USER_TYPE_CHOICES
    )  # Поле выбора типа пользователя


class Warehouse(models.Model):
    """# Модель для представления склада
    # Название склада"""

    name = models.CharField(max_length=100)  # Поле для названия склада
    # Адрес склада
    address = models.CharField(
        max_length=255, default="Unknown"
    )  # Поле для адреса склада


class Product(models.Model):
    """# Модель для представления товара
    # Название товара"""

    name = models.CharField(max_length=100)  # Поле для названия товара
    # Количество товара на складе
    quantity = models.PositiveIntegerField()  # Поле для количества товара
    # Связь с моделью склада, где хранится товар
    warehouse = models.ForeignKey(
        Warehouse, related_name="products", on_delete=models.CASCADE
    )  # Внешний ключ на склад


class Supply(models.Model):
    """# Модель для представления поставок товара
    # Поставщик, осуществляющий поставку"""

    supplier = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE
    )  # Внешний ключ на пользователя (поставщика)
    # Товар, который поставляется
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )  # Внешний ключ на товар
    # Количество поставляемого товара
    # Поле для количества поставляемого товара
    quantity = models.PositiveIntegerField()


class Consumption(models.Model):
    """# Модель для представления потребления товара
    # Потребитель, забирающий товар"""

    consumer = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE
    )  # Внешний ключ на пользователя (потребителя)
    # Товар, который потребляется
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )  # Внешний ключ на товар
    # Количество забираемого товара
    # Поле для количества потребляемого товара
    quantity = models.PositiveIntegerField()

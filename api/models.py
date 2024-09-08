from django.db import models  # Импорт моделей из Django
from django.contrib.auth.models import AbstractUser  # Импорт стандартной модели пользователя

# Пользовательская модель, расширяющая стандартную модель пользователя Django
class CustomUser(AbstractUser):
    # Определение типов пользователей: поставщик или потребитель
    USER_TYPE_CHOICES = [
        ('supplier', 'Supplier'),  # Значение для поставщика
        ('consumer', 'Consumer'),  # Значение для потребителя
    ]
    # Поле для хранения типа пользователя
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)  # Поле выбора типа пользователя

# Модель для представления склада
class Warehouse(models.Model):
    # Название склада
    name = models.CharField(max_length=100)  # Поле для названия склада
    # Адрес склада
    address = models.CharField(max_length=255, default="Unknown")  # Поле для адреса склада

# Модель для представления товара
class Product(models.Model):
    # Название товара
    name = models.CharField(max_length=100)  # Поле для названия товара
    # Количество товара на складе
    quantity = models.PositiveIntegerField()  # Поле для количества товара
    # Связь с моделью склада, где хранится товар
    warehouse = models.ForeignKey(Warehouse, related_name='products', on_delete=models.CASCADE)  # Внешний ключ на склад

# Модель для представления поставок товара
class Supply(models.Model):
    # Поставщик, осуществляющий поставку
    supplier = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Внешний ключ на пользователя (поставщика)
    # Товар, который поставляется
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Внешний ключ на товар
    # Количество поставляемого товара
    quantity = models.PositiveIntegerField()  # Поле для количества поставляемого товара

# Модель для представления потребления товара
class Consumption(models.Model):
    # Потребитель, забирающий товар
    consumer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Внешний ключ на пользователя (потребителя)
    # Товар, который потребляется
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Внешний ключ на товар
    # Количество забираемого товара
    quantity = models.PositiveIntegerField()  # Поле для количества потребляемого товара


         

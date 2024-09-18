"""_summary_

    Raises:
        permissions.PermissionDenided: _description_
        permissions.PermissionDenided: _description_
        serializer.ValidationError: _description_
    """

from rest_framework import viewsets, permissions
from .models import CustomUser, Product, Warehouse, Supply, Consumption
from .serializers import (
    CustomUserSerializer,
    WarehouseSerializer,
    ProductSerializer,
    SupplySerializer,
    ConsumptionSerializer,
)


class CustomerUserViewSet(viewsets.ModelViewSet):
    """# Представление для модели CustomUser"""

    serializer_class = CustomUserSerializer  # Используемый сериализатор
    queryset = CustomUser.objects.all()  # Запрос для получения всех пользователей
    permissions_classes = [permissions.AllowAny]  # Доступ разрешен всем


class ProductUserViewSet(viewsets.ModelViewSet):
    """# Представление для модели Product"""

    serializer_class = ProductSerializer  # Используемый сериализатор
    queryset = Product.objects.all()  # Запрос для получения всех товаров
    permissions_classes = [
        permissions.IsAuthenticated
    ]  # Доступ разрешен только аутентифицированным пользователям


class WarehouseViewSet(viewsets.ModelViewSet):
    """# Представление для модели Warehouse"""

    serializer_class = WarehouseSerializer  # Используемый сериализатор
    queryset = Warehouse.objects.all()  # Запрос для получения всех складов
    permissions_classes = [
        permissions.IsAuthenticated
    ]  # Доступ разрешен только аутентифицированным пользователям


class SupplyViewSet(viewsets.ModelViewSet):
    """# Представление для модели Supply"""

    serializer_class = SupplySerializer  # Используемый сериализатор
    queryset = Supply.objects.all()  # Запрос для получения всех поставок
    permissions_classes = [
        permissions.IsAuthenticated
    ]  # Доступ разрешен только аутентифицированным пользователям

    # Переопределение метода сохранения
    def perform_create(self, serializer):
        user = self.request.user  # Получение текущего пользователя
        # Проверка, что пользователь является поставщиком
        if user.user_type != "supplier":  # Если пользователь не поставщик
            raise permissions.PermissionDenided(
                "Only suppliers can supply products."
            )  # Возбуждение исключения
        serializer.save(supplier=user)  # Сохранение объекта с указанием поставщика


class ConsumptionViewSet(viewsets.ModelViewSet):
    """# Представление для модели Consumption"""

    serializer_class = ConsumptionSerializer  # Используемый сериализатор
    queryset = Warehouse.objects.all()  # Запрос для получения всех товаров
    permissions_classes = [
        permissions.IsAuthenticated
    ]  # Доступ разрешен только аутентифицированным пользователям

    def perform_create(self, serializer):
        user = self.request.user  # Получение текущего пользователя
        # Проверка, что пользователь является поставщиком
        if user.user_type != "consumer":  # Если пользователь не поставщик
            raise permissions.PermissionDenided(
                "Only consumers can consume products."
            )  # Вывод исключения
        product = serializer.validated_data[
            "product"
        ]  # Получение товара из валидированных данных

        # Проверка наличия достаточного количества товара
        if serializer.validated_data[
            "quantity"
        ]:  # Если запрашиваемое количество больше доступного
            raise serializer.ValidationError(
                "Not enough product in stock."
            )  # Вывод исключения
        serializer.save(consumer=user)  # Сохранение объекта с указанием потребителя
        product.quantity -= (
            serializer.validated_data
        )  # Уменьшение количества товара на складе
        product.save()  # Сохранение обновленного товара

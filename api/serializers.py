from rest_framework import serializers  # Импортируем модуль serializers из Django REST Framework
from .models import CustomUser, Product, Warehouse, Supply, Consumption # Импортируем модели, которые будем сериализировать

# Сериализатор для модели CustomUser (кастомного пользователя)
class CustomUserSerializer(serializers.ModelSerializer):  # Определяем класс сериализатора для модели CustomUser
    class Meta:  # Внутренний класс Meta используется для указания метаинформации
        model = CustomUser  # Указываем модель, для которой создаем сериализатор (CustomUser)
        fields = ['email', 'password', 'first_name', 'last_name']  # Перечисляем поля, которые будут сериализоваться
        extra_kwargs = {'password': {'write_only': True, 'required': False}} # Чтобы пароль не возвращался в ответе
        
   
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)  # Создание пользователя с паролем
        return user
    
    
    def update(self, instance, validated_data):
         # Обновляем email, если он передан
        email = validated_data.get('email')
        if email:
            instance.email = email
          # Обновляем пароль, если он передан  
        password = validated_data.get('password')
        if password:
            instance.set_password = password# Хэшируем новый пароль
            
        instance.save()  # Сохраняем изменения
        return instance
            
            

# Сериализатор для модели Warehouse (склада)
class WarehouseSerializer(serializers.ModelSerializer):  # Определяем класс сериализатора для модели Warehouse
    class Meta:  # Внутренний класс Meta содержит метаинформацию для сериализатора
        model = Warehouse  # Указываем модель Warehouse
        fields = ['id', 'name']  # Определяем поля модели, которые будут сериализоваться

# Сериализатор для модели Product (товара)
class ProductSerializer(serializers.ModelSerializer):  # Определяем класс сериализатора для модели Product
    class Meta:  # Внутренний класс Meta для указания метаинформации
        model = Product  # Указываем модель Product
        fields = ['id', 'name', 'stock', 'warehouse']  # Указываем поля для сериализации (id, имя товара, количество на складе, склад)


# Сериализатор для модели Supply
class SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply  # Модель для сериализации
        fields = ('id', 'supplier', 'product', 'quantity')  # Поля для сериализации

# Сериализатор для модели Consumption
class ConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumption  # Модель для сериализации
        fields = ('id', 'consumer', 'product', 'quantity')  # Поля для сериализации
        
        

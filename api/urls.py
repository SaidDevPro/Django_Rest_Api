from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CustomerUserViewSet, ProductUserViewSet, WarehouseViewSet, SupplyViewSet, ConsumptionViewSet

# Создание маршрутизатора и регистрация представлений
router = DefaultRouter() # Создание маршрутизатора

router.register(r'users', CustomerUserViewSet)  # Регистрация представления для пользователей
router.register(r'products', ProductUserViewSet) # Регистрация представления для складов
router.register(r'warehouses', WarehouseViewSet) # Регистрация представления для товаров
router.register(r'supplies', SupplyViewSet)  # Регистрация представления для поставок
router.register(r'consumptions', ConsumptionViewSet, basename='consumption') # Регистрация представления для потреблений



# Определение URL-адресов для маршрутов
urlpatterns = [
    path('', include(router.urls))  # Включение маршрутов маршрутизатора
]

urlpatterns.extend(router.urls)
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CustomerUserViewSet, ProductUserViewSet, WarehouseViewSet, SupplyViewSet, ConsumptionViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  # Импорт представлений для работы с токенами
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
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Маршрут для получения токенов
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Маршрут для обновления токенов
    
]

urlpatterns.extend(router.urls)
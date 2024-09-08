
# Django REST API для управления складом

## Описание

Этот проект представляет собой API для управления складами и товарами с функционалом регистрации и аутентификации пользователей. В проекте реализованы два типа пользователей: **поставщики** и **потребители**. Поставщики могут добавлять товары на склады, а потребители — забирать товары.

## Установленные пакеты

- Python 3.12
- Django 5.1.1
- Django REST Framework
- Django REST Framework SimpleJWT (для аутентификации на основе JWT)

## Функционал

1. **Регистрация пользователей** (поставщик/потребитель).
2. **Аутентификация через JWT**.
3. **Создание складов**.
4. **Добавление товаров** на склады.
5. **Поставщики** могут добавлять товары на склады.
6. **Потребители** могут забирать товары со складов, но не больше доступного количества.

## Установка

1. Клонируйте репозиторий на ваш локальный компьютер:
    ```bash
    git clone https://github.com/username/repository.git
    cd repository
    ```

2. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv venv
    source venv/bin/activate  # для Linux/macOS
    venv\Scripts\activate  # для Windows
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Выполните миграции базы данных:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Запустите сервер разработки:
    ```bash
    python manage.py runserver
    ```

6. API будет доступно по адресу:
    ```
    http://127.0.0.1:8000/
    ```

## API Endpoints

### Аутентификация и регистрация

- **POST** `/api/register/` — регистрация нового пользователя (поставщик или потребитель).
- **POST** `/api/token/` — получение JWT токенов (access и refresh).
- **POST** `/api/token/refresh/` — обновление токена доступа.

### Склады

- **GET** `/api/warehouses/` — список складов.
- **POST** `/api/warehouses/` — создание нового склада.

### Товары

- **GET** `/api/products/` — список товаров.
- **POST** `/api/products/` — добавление нового товара.

### Поставки

- **POST** `/api/supplies/` — добавление товара на склад (доступно только для поставщиков).

### Потребление

- **POST** `/api/consumptions/` — получение товара со склада (доступно только для потребителей).

## Настройки JWT

В файле `settings.py` добавлены настройки для JWT-аутентификации. Срок действия токена доступа составляет 15 минут, токена обновления — 1 день.

Пример настроек:
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}
```

## Примеры запросов

### Регистрация

```bash
POST /api/register/
Content-Type: application/json

{
    "username": "supplier1",
    "password": "password123",
    "user_type": "supplier"
}
```

### Получение токена

```bash
POST /api/token/
Content-Type: application/json

{
    "username": "supplier1",
    "password": "password123"
}
```

Ответ:
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGci...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGci..."
}
```

### Создание склада

```bash
POST /api/warehouses/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "name": "Склад №1",
    "address": "ул. Примерная, 1"
}
```

### Поставка товара

```bash
POST /api/supplies/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "product": 1,
    "quantity": 100
}
```

### Потребление товара

```bash
POST /api/consumptions/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "product": 1,
    "quantity": 10
}
```

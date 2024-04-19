# Сервис для хранения и редактирования ссылок

# Документация API
- http://127.0.0.1:8000/swagger/

## Как установить
Для работы сервиса требуются:
- Python версии не ниже 3.10.
- установленное ПО для контейнеризации DockerCompose - [Docker](https://docs.docker.com/engine/install/).
- Инструмент Virtualenv для управления зависимостями и сборкой пакетов в Python.

Настройка переменных окружения
1.Заполните .env файл. Пример:
```
DATABASE_URL = "postgresql://django_admin:test1234@localhost:5432/api_link"

EMAIL_HOST = "smtp.yandex.ru"
EMAIL_PORT = 465
EMAIL_HOST_USER = "meganoshops@yandex.ru"
EMAIL_HOST_PASSWORD = "lmxgiyelbswrujgz"
```

Запуск СУБД Postgresql
```shell
docker-compose -f docker-compose.dev.yml up -d
```

Установка и активация виртуального окружения
```shell
pip install  ; установка пакетов
.\venv\Scripts\activate  ; активация виртуального окружения
pip install -r requirements.txt  ; установка pre-commit для проверки форматирования кода, см. .pre-commit-config.yaml
```


## Как запустить web-сервер
Запуск сервера производится в активированном локальном окружение из папки `market/`
```shell
python manage.py runserver
```


## Логин и пароль для суперпользователя
login: admin
password: test1234

# Цели проекта

Код написан в учебных целях.

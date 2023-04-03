## Яндекс Практикум. Спринт 3.

[![CI](https://github.com/yandex-praktikum/hw02_community/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/yandex-praktikum/hw02_community/actions/workflows/python-app.yml)
[![Python](https://img.shields.io/badge/-Python-464641?style=flat-square&logo=Python)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/-pytest-464646?style=flat-square&logo=pytest)](https://docs.pytest.org/en/6.2.x/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![HTML5](https://img.shields.io/badge/-HTML5-464646?style=flat-square&logo=html5)](https://en.wikipedia.org/wiki/HTML5)
[![CSS](https://img.shields.io/badge/-CSS-464646?style=flat-square&logo=css3)](https://en.wikipedia.org/wiki/CSS)

## Описание

Yatube - социальная сеть с авторизацией, персональными лентами, комментариями и подписками на авторов статей.

## Функционал:

- создано и зарегистрировано приложение Posts;
- подключена база данных;
- десять последних записей выводятся на главную страницу;
- в админ-зоне доступно управление объектами модели ```Post```, можно публиковать новые записи, редактировать и удалять существующие;
- пользователь может перейти на страницу любого сообщества, где отображаются десять последних публикаций из этой группы.

## Установка

1. Клонировать репозиторий:

    ```
    git clone https://github.com/IrinaSMR/hw02_community.git
    ```

2. Перейти в папку с проектом:

    ```
    cd hw02_community
    ```

3. Установить и активировать виртуальное окружение для проекта:

    ```
    python -m venv venv
    source venv/Scripts/activate
    ```

4. Обновить pip и установить зависимости:

    ```
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

5. Выполнить миграции на уровне проекта:

    ```
    cd yatube
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

6. Запустить проект локально:

    ```
    python3 manage.py runserver

    # проект появляется по адресу
    http://127.0.0.1:8000
    ```

7. Зарегистирировать суперпользователя Django:

    ```
    python3 manage.py createsuperuser

    # адрес панели администратора
    http://127.0.0.1:8000/admin
    ```
### Автор:
IrinaSMR

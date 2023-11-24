<h1> app_drf </h1>

<h2> Инструкция по запуску </h2>

<h3>1. Клонируем репозиторий </h3>
&nbsp &nbsp &nbsp git clone https://github.com/Gektor918/app_drf

<h3>2. Создаем виртуальное окружение </h3>
&nbsp &nbsp &nbsp python3 -m venv name_venv

<h3>3. Запускаем виртуальное окружение </h3>
&nbsp &nbsp &nbsp source name_venv/bin/activate

<h3>4. Устанавливаем зависимости </h3>
&nbsp &nbsp &nbsp pip install -r requirements.txt

<h3>5. Настраиваем бд в settings.py </h3>
DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql',
        'NAME':'You name',
        'USER':'You user',
        'PASSWORD':'You password',
    }
}

<h3>6. Миграции </h3>
&nbsp &nbsp &nbsp python3 manage.py makemigrations
&nbsp &nbsp &nbsp python3 manage.py migrate

<h3>7. Создаём superuser </h3>
&nbsp &nbsp &nbsp python3 manage.py createsuperuser

<h3>8. Выполните команду для установки переменной окружения </h3>
&nbsp &nbsp &nbsp set DJANGO_SETTINGS_MODULE=app_drf.settings

<h3>9. Запускаем сервер </h3>
&nbsp &nbsp &nbsp python3 manage.py runserver

<h3>10. Запуск сидов </h3>
&nbsp &nbsp &nbsp python3 feed.py

<h3>11. Создание заметки, рекламного объявления и выдачу ачивки пользователю можно сделать
через Django Admin. </h3>


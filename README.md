<h1> app_drf </h1>

<h2> Инструкция по запуску </h2>

<h3>1. Создаем виртуальное окружение </h3>
&nbsp &nbsp &nbsp python3 -m venv name_venv

<h3>2. Запускаем виртуальное окружение </h3>
&nbsp &nbsp &nbsp source name_venv/bin/activate

<h3>3. Устанавливаем зависимости </h3>
&nbsp &nbsp &nbsp pip install -r requirements.txt

<h3>4. Настраиваем бд в settings.py </h3>
<br>DATABASES = {
    <br>'default': {
        <br>'ENGINE':'django.db.backends.postgresql',
        <br>'NAME':'You name',
        <br>'USER':'You user',
        <br>'PASSWORD':'You password',} <br>
    }

<h3>5. Миграции </h3>
&nbsp &nbsp &nbsp python3 manage.py makemigrations <br>
&nbsp &nbsp &nbsp python3 manage.py migrate

<h3>6. Создаём superuser </h3>
&nbsp &nbsp &nbsp python3 manage.py createsuperuser

<h3>7. Выполните команду для установки переменной окружения </h3>
&nbsp &nbsp &nbsp set DJANGO_SETTINGS_MODULE=app_drf.settings

<h3>8. Запускаем сервер </h3>
&nbsp &nbsp &nbsp python3 manage.py runserver

<h3>9. Запуск сидов </h3>
&nbsp &nbsp &nbsp python3 feed.py

<h3>10. Создание заметки, рекламного объявления и выдачу ачивки пользователю можно сделать
через Django Admin. </h3>


### Приложение ToDo и заметки (на английском)

# Под капотом:
- [Python]
- [Django]
- [SqlAlchemy]
- [Bootstrap]
- [Pillow]

# Возможности:
- Ругистраиця пользователей
- создавать/просматривать/изменять/удалять Заметки и действия;

Установить все зависимости 

```bash
$ pip install -r requirements.txt
```

Создать суперпользователя

```bash
$ python manage.py createsuperuser
```
Миграции уже сделаны для созданных моделей, если производить изменения сделать миграции заново

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

Запуск приложения на локальном хосте 

```bash
$ python manage.py runserver
```


[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=20074901&assignment_repo_type=AssignmentRepo)
# Работа с шаблонами и ORM

Этот сервис служит для создания заметок и пользователей.

## 🚀 Возможности

- Добавление Пользователя. Для этого кликните на кнопку "Панель администратора"(логин: admin, пароль: adminpass) где найдите кнопку "Пользователи" и кнопку "Добавить"
- Добавление Заметки. Для этого кликните на кнопку "Панель администратора"(логин: admin, пароль: adminpass) где найдите кнопку "Заметки" и кнопку "Добавить", но перед
  этим вам следует добавить аналогическим способом категории и статус
- Просмотр всех заметок по клику в верхнем меню на Лого или "Все заметки".
- Просмотр всех пользователей по клику в верхнем меню "Пользователи".
- Просмотр отдельной заметки по клику на "Подробнее" в списке заметок.
- Просмотр отдельного пользователя по клику на "Подробнее" в списке пользователей
---

## 📦 Стек технологий

- **Python** 3.13
- **Django** 5.2.5
- **PostgreSQL**
- **Docker + Docker Compose**

---

## 🔧 Установка и запуск

### 1. Клонируем репозиторий
```bash
git clone git@github.com:Solva-technology/django-notes-orm-ChikaEJ.git
cd django-notes-orm-ChikaEJ
```
### 2. Настройка .env
    
####    - Создай файл .env в корне проекта и укажите:
```
DJANGO_DEBUG=True
DJANGO_SECRET_KEY=
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
DJANGO_CSRF_TRUSTED_ORIGINS=http://localhost

DJANGO_LANGUAGE_CODE=ru-RU
DJANGO_TIME_ZONE=Asia/Almaty

POSTGRES_DB=notes_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432

```

### 3. Docker Compose запуск
```bash
docker-compose up --build
```
 ####   Это поднимет:

####  * Django backend (web)

####    * PostgreSQL (db)

####    * Применит миграции и создаст суперпользователя (admin and pass: adminpass)

### 4. Переходим на [localhost:8000](http://localhost:8000) и нарождаемся жизнью! :-)

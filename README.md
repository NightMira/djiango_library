# АИС Библиотеки

Автоматизированная информационная система библиотеки.  
Курсовая работа по дисциплине «Проектирование информационных систем».

## Технологический стек

- Python 3.11+
- Django 5.0
- PostgreSQL 16
- HTML5 / CSS3 / Bootstrap 5

## Быстрый старт

### 1. Клонирование репозитория

```bash
git clone https://github.com/NightMira/djiango_library.git
cd djiango_library
```

### 2. Создание виртуального окружения

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```
### 4. Настройка базы данных
Создайте базу данных PostgreSQL:

```sql
CREATE DATABASE library_db;
CREATE USER library_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE library_db TO library_user;
```

Настройте подключение в файле **settings.py**.

### 5. Применение миграций

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Загрузка тестовых данных

```bash
python manage.py dbshell < database/init.sql
```

### 7. Создание администратора

```bash
python manage.py createsuperuser
```

### 8. Запуск сервера

```bash
python manage.py runserver
```

После запуска система будет доступна по адресу: http://127.0.0.1:8000


# Pomidor 4.2.2 🍅

Автотесты для API Pomidor Stage. Используется `pytest`, `requests`, `faker`.

## 📦 Установка

```bash
poetry install
```
## ⚙️ Настройка переменных окружения

Перед запуском тестов создайте `.env` или отредактируйте файл в корне проекта:

```env
USERNAME=your_email@gmail.com
PASSWORD=your_password
```

##  Запуск тестов

```bash
poetry run pytest -v
```

## Структура проекта

```
project/
├── tests/
│   ├── test_items.py
│   ├── test_auth.py
│   ├── conftest.py
├── config/
│   └── constants.py
├── .env
├── pyproject.toml

```

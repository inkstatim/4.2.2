# Pomidor 4.2.2 🍅

Автотесты для API Pomidor Stage. Используется `pytest`, `requests`, `faker`.

## 📦 Установка

```bash
poetry install
```

##  🚀 Запуск тестов
Без отчётности
```bash
poetry run pytest -v
```
С генерацией Allure-отчёта
```bash
poetry run pytest --alluredir=allure-results
```
Затем:
```bash
allure serve allure-results
```
❗ Убедитесь, что у вас установлен Allure CLI. Установка:

macOS - [официальная инструкция](https://docs.qameta.io/allure/#_installing_a_commandline)

Windows - [установка для Windows](https://docs.qameta.io/allure/#_installing_a_commandline)


## Структура проекта

```
project/
├── tests/
│   ├── test_items.py
│   ├── test_auth.py
│   ├── conftest.py
├── config/
│   └── constants.py
```
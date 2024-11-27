# Library Management System

## Описание

Это консольное приложение для управления библиотекой книг. Приложение позволяет добавлять, удалять, искать и отображать книги, а также изменять статус книг (например, "в наличии" или "выдана").

## Установка

1. Клонируйте репозиторий или скачайте исходный код.
2. Убедитесь, что у вас установлен Python 3.6 или выше.

## Использование

### Добавление книги

```Windows PowerShell или Command Line
python library.py add "Название книги" "Автор книги" "Год издания"


### Удаление книги

```Windows PowerShell или Command Line
python library.py remove "ID"


### Поиск книг

```Windows PowerShell или Command Line
python library.py search "Запрос"


### Отображение всех книг

```Windows PowerShell или Command Line
python library.py display


### Изменение статуса

```Windows PowerShell или Command Line
python library.py change_status "ID" "в наличии"  # или "выдана"
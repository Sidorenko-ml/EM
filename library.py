import argparse
import json
import os
import random


class Library:
    books_file = 'books.json'

    def __init__(self):
        self.books = self.load_books()

    @staticmethod
    def load_books():
        """Открываем JSON"""
        if os.path.exists(Library.books_file):
            with open(Library.books_file, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        return []

    def save_books(self):
        """Сохраняем JSON."""
        with open(Library.books_file, 'w') as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, title, author, year):
        """Добавление новой книги"""
        unique_id = str(random.randint(0, 9999)).zfill(4)
        book = {'id': unique_id, 'title': title, 'author': author, 'year': year, 'status': 'в наличии'}
        self.books.append(book)
        self.save_books()
        print(f"Книга '{title}' успешно добавлена!")

    def remove_book(self, id):
        """Удаление книги"""
        new_books = [book for book in self.books if book['id'] != id]
        if len(new_books) == len(self.books):
            print(f"Книга с уникальным номером '{id}' не найдена.")
            return
        self.books = new_books
        self.save_books()
        print(f"Книга с уникальным номером '{id}' удалена.")

    def search_books(self, query):
        """Поиск книг"""
        result = [book for book in self.books if query.lower() in book['title'].lower() or query.lower() in book['author'].lower() or query in str(book['year'])]
        return result

    def display_books(self):
        """Отображение всех книг"""
        if not self.books:
            print("В библиотеке нет книг на данный момент.")
        for book in self.books:
            print(f"{book['title']}, автор {book['author']}, Год издания: {book['year']}, Уникальный номер: {book['id']}, Статус: {book['status']}")

    def change_status(self, id, status):
        """Изменение статуса"""
        for book in self.books:
            if book['id'] == id:
                book['status'] = status
                self.save_books()
                print(f"Статус книги {id} изменен на '{status}'.")
                return
        print(f"Книга с уникальным номером '{id}' не найдена.")


def main():
    library = Library()

    parser = argparse.ArgumentParser(description="Library Management System")
    subparsers = parser.add_subparsers(dest='command')

    # Add book
    add_parser = subparsers.add_parser('add', help='Добавление новой книги')
    add_parser.add_argument('title', type=str, help='Название книги')
    add_parser.add_argument('author', type=str, help='Автор')
    add_parser.add_argument('year', type=int, help='Год издания')

    # Remove book
    remove_parser = subparsers.add_parser('remove', help='Удаление книги по ID')
    remove_parser.add_argument('id', type=str, help='ID книги для удаления')

    # Search books
    search_parser = subparsers.add_parser('search', help='Поиск книг по названию или автору')
    search_parser.add_argument('query', type=str, help='Поисковый запрос')

    # Display books
    subparsers.add_parser('display', help='Отображение всех книг')

    # Change status
    change_status_parser = subparsers.add_parser('change_status', help='Изменение статуса книги по ID')
    change_status_parser.add_argument('id', type=str, help='ID книги для изменения')
    change_status_parser.add_argument('status', type=str, choices=['в наличии', 'выдана'], help='Статус книги')

    args = parser.parse_args()

    if args.command == 'add':
        library.add_book(args.title, args.author, args.year)
    elif args.command == 'remove':
        library.remove_book(args.id)
    elif args.command == 'search':
        results = library.search_books(args.query)
        if not results:
            print("Книг не найдено.")
        for book in results:
            print(f"{book['title']}, автор {book['author']}, Год издания: {book['year']}, Уникальный номер: {book['id']}, Статус: {book['status']}")
    elif args.command == 'display':
        library.display_books()
    elif args.command == 'change_status':
        library.change_status(args.id, args.status)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
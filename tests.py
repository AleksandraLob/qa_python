import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Тесты для метода add_new_book

    # Проверяем, что книга добавляется корректно
    def test_add_new_book_success(self):
        collector = BooksCollector()
        collector.add_new_book("Book1")
        assert "Book1" in collector.get_books_genre()

    # Тесты параметризованные
    # Проверяем, что книга не добавляется, если её имя слишком длинное
    @pytest.mark.parametrize('name', ['книга не добавляется, имя слишком длинное', ''])
    def test_add_new_book_name_too_long_short(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.books_genre

    @pytest.mark.parametrize('name', ['книга добавляется имя длиной длинное 40', '1'])
    def test_add_new_book_name_long_short(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.books_genre

    # Проверяем, что книга не добавляется, если её имя уже существует
    def test_add_new_book_name_already_exists(self):
        collector = BooksCollector()
        collector.add_new_book("Book1")
        collector.add_new_book("Book1")
        assert len(collector.get_books_genre()) == 1

    # Тесты для метода set_book_genre

    # Проверяем, что жанр книги устанавливается корректно
    def test_set_book_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book("Book1")
        collector.set_book_genre("Book1", "Фантастика")
        assert collector.get_book_genre("Book1") == "Фантастика"

    # Проверяем, что жанр книги не устанавливается, если книга не существует
    def test_set_book_genre_book_not_exists(self):
        collector = BooksCollector()
        collector.set_book_genre("Book_not_exist", "Фантастика")
        assert collector.get_book_genre("Book_not_exist") is None

    # Проверяем, что жанр книги не устанавливается, если жанр не существует
    def test_set_book_genre_genre_not_exists(self):
        collector = BooksCollector()
        collector.add_new_book("Book1")
        collector.set_book_genre("Book1", "Фэнтези")
        assert collector.get_book_genre("Book1") == ''

    # Тесты для метода get_books_with_specific_genre

    # Проверяем, что получаем список книг с определённым жанром корректно
    def test_get_books_with_specific_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book("Book1")
        collector.add_new_book("Book2")
        collector.set_book_genre("Book1", "Фантастика")
        collector.set_book_genre("Book2", "Фантастика")
        assert collector.get_books_with_specific_genre("Фантастика") == ["Book1", "Book2"]

    # Проверяем, что получаем пустой список, если жанр не существует
    def test_get_books_with_specific_genre_genre_not_exists(self):
        collector = BooksCollector()
        collector.add_new_book("Book1")
        collector.add_new_book("Book2")
        collector.set_book_genre("Book1", "Фантастика")
        collector.set_book_genre("Book2", "Ужасы")
        assert collector.get_books_with_specific_genre("Комедии") == []

    # Тесты для метода get_books_genre
    def test_get_books_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book("Book1")
        collector.set_book_genre("Book1", "Фантастика")
        assert collector.get_books_genre() == {"Book1": "Фантастика"}

    # Тесты для метода get_books_for_children

    # Проверяем, что получаем список книг, подходящих детям, корректно
    def test_get_books_for_children_success(self):
        collector = BooksCollector()
        collector.add_new_book("Book1")
        collector.add_new_book("Book2")
        collector.add_new_book("Book3")
        collector.set_book_genre("Book1", "Фантастика")
        collector.set_book_genre("Book2", "Ужасы")
        collector.set_book_genre("Book3", "Комедии")
        assert collector.get_books_for_children() == ['Book1', 'Book3']

    # Тесты для метода add_book_in_favorites

    # Проверяем, что книга добавляется в избранное корректно
    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book("Book1")
        collector.add_book_in_favorites("Book1")
        assert collector.get_list_of_favorites_books() == ["Book1"]

    # Проверяем, что книга не добавляется в избранное, если она не существует
    def test_add_book_in_favorites_book_not_exists(self):
        collector = BooksCollector()
        collector.add_book_in_favorites("Book1")
        assert collector.get_list_of_favorites_books() == []

    # Проверяем, что книга не добавляется в избранное, если она уже там есть
    def test_add_book_in_favorites_already_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Book1")
        collector.add_book_in_favorites("Book1")
        collector.add_book_in_favorites("Book1")
        assert len(collector.get_list_of_favorites_books()) == 1

    # Тесты для метода delete_book_from_favorites

    # Проверяем, что книга удаляется из избранного корректно
    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book("Book1")
        collector.add_book_in_favorites("Book1")
        collector.delete_book_from_favorites("Book1")
        assert collector.get_list_of_favorites_books() == []

    # Тесты для метода get_list_of_favorites_books
    # Проверяем список избранного
    def test_get_list_of_favorites_books_success(self):
        collector = BooksCollector()
        collector.add_new_book("Book1")
        collector.add_book_in_favorites("Book1")
        assert collector.get_list_of_favorites_books() == ["Book1"]
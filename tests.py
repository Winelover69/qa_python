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
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_get_books_for_children_age_rated_books_excluded(self):
        #Проверяет, что книги с возрастным рейтингом отсутствуют в списке книг для детей.
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        assert 'Что делать, если ваш кот хочет вас убить' not in collector.get_books_for_children()
        assert 'Гордость и предубеждение и зомби' in collector.get_books_for_children()

    @pytest.mark.parametrize("name, genre", [
            ("Гордость и предубеждение и зомби", "Фантастика"),
            ("Что делать, если ваш кот хочет вас убить", "Ужасы"),
            ("Двенадцать стульев", "Комедии"),
        ])
    def test_set_book_genre_success(self, name, genre):
            collector = BooksCollector()
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
            assert collector.get_book_genre(name) == genre

    def test_add_new_book_long_name(self):
        collector = BooksCollector()
        collector.add_new_book('Очень длинное название книги, которое превышает 41 символов')
        assert 'Очень длинное название книги, которое превышает 41 символов' not in collector.get_books_genre()

    def test_add_new_book_duplicate(self):
        #Проверяет, что книгу нельзя добавить дважды.
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize("name, genre", [
        ("Гордость и предубеждение и зомби", "Фантастика"),
        ("Что делать, если ваш кот хочет вас убить", "Ужасы"),
        ("Двенадцать стульев", "Комедии"),
    ])
    def test_set_book_genre_success(self, name, genre):
        #Проверяет, что жанр книги устанавливается успешно.
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize("name, genre", [
        ("Гордость и предубеждение и зомби", "Фантастика"),
        ("Что делать, если ваш кот хочет вас убить", "Ужасы"),
    ])
    def test_get_books_with_specific_genre(self, name, genre):
        #Проверяет, что метод возвращает список книг с заданным жанром.
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre) == [name]

    def test_add_book_in_favorites_success(self):
        #Проверяет, что книга успешно добавляется в избранное.
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    def test_delete_book_from_favorites(self):
        #Проверяет, что книга успешно удаляется из избранного.
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == []


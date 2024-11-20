from main import BooksCollector
import pytest



class TestBooksCollector:

    @pytest.fixture
    def books_collector(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        return collector

    def test_add_new_book_add_two_books(self, books_collector):
        assert len(books_collector.books_genre) == 2

    def test_add_new_book_add_same_book_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.books_genre) == 1

    def test_add_new_book_add_book_with_empty_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert len(collector.books_genre) == 0

    def test_set_book_genre_add_two_books(self, books_collector):
        assert len(books_collector.books_genre) == 2

    def test_set_book_genre_add_genre_without_adding_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Гордость и предубеждение и зомби 2', 'Комедии')
        assert len(collector.books_genre) == 0

    def test_get_book_genre_get_existed_book(self, books_collector):
        assert books_collector.get_book_genre('Гордость и предубеждение и зомби') == 'Комедии'

    def test_get_books_with_specific_genre_get_two_comedies(self, books_collector):
        books_collector.add_new_book('Гордость и предубеждение и зомби 2')
        books_collector.set_book_genre('Гордость и предубеждение и зомби 2', 'Комедии')
        assert books_collector.get_books_with_specific_genre('Комедии') == ['Гордость и предубеждение и зомби', 'Гордость и предубеждение и зомби 2']

    def test_get_books_genre_get_dict_with_two_books(self, books_collector):
        assert len(books_collector.books_genre) == 2

    def test_get_book_genre_get_book_genre(self, books_collector):
        assert books_collector.get_book_genre('Гордость и предубеждение и зомби') == 'Комедии'

    def test_get_books_for_children_get_comedy(self, books_collector):
        assert books_collector.get_books_for_children() == ['Гордость и предубеждение и зомби']

    def test_add_book_in_favorites_add_two_books(self, books_collector):
        books_collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        books_collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert len(books_collector.favorites) == 2

    def test_delete_book_from_favorites_add_two_books_and_delete_one(self, books_collector):
        books_collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        books_collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        books_collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert len(books_collector.favorites) == 1

    def test_delete_book_from_favorites_add_book_and_delete_book_twice(self, books_collector):
        books_collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        books_collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert len(books_collector.favorites) == 0

    def test_get_list_of_favorites_books(self, books_collector):
        books_collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert books_collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']
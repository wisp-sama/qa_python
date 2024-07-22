import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
class TestBooksCollector:

    @pytest.mark.parametrize(
        'book_name',
        ["Гордость и предубеждение и зомби", "Что делать, если ваш кот хочет вас убить"]
    )
    def test_add_new_book_two_books_added(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    def test_add_new_book_exceeds_length_book_not_added(self):
        collector = BooksCollector()
        long_name = 'a' * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    def test_add_new_book_duplicate_book_not_added(self):
        collector = BooksCollector()
        book_name = "Гордость и предубеждение и зомби"
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize(
        "book_name, genre",
        [("Дюна", "Фантастика"), ("Чужой", "Ужасы")]
    )
    def test_set_book_genre_existent_genre_setted(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_set_book_genre_nonexistent_genre_not_setted(self):
        collector = BooksCollector()
        collector.add_new_book("Дюна")
        nonexistent_genre = "Неизвестный жанр"
        collector.set_book_genre("Дюна", nonexistent_genre)
        assert collector.get_book_genre("Дюна") == ''

    def test_get_book_genre_setted_genre_getted(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        assert collector.get_book_genre("Гарри Поттер") == "Фантастика"

    def test_get_books_genre_two_books_with_genre_dict_getted(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        collector.add_new_book("1984")
        collector.set_book_genre("1984", "Детективы")
        expected_genre_dict = {
            "Гарри Поттер": "Фантастика",
            "1984": "Детективы"
        }
        assert collector.get_books_genre() == expected_genre_dict

    def test_get_books_with_specific_genre_two_books_with_different_genre_book_getted(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_new_book("Стивен Кинг. Оно")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        collector.set_book_genre("Стивен Кинг. Оно", "Ужасы")
        assert collector.get_books_with_specific_genre("Фантастика") == ["Гарри Поттер"]

    def test_get_books_for_children_two_books_with_different_genre_book_getted(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_new_book("Стивен Кинг. Оно")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        collector.set_book_genre("Стивен Кинг. Оно", "Ужасы")
        assert collector.get_books_for_children() == ["Гарри Поттер"]

    def test_add_book_in_favorites_one_book_book_added(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        assert "Гарри Поттер" in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_one_book_book_deleted(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        collector.delete_book_from_favorites("Гарри Поттер")
        assert "Гарри Поттер" not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_no_books_list_empty(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []

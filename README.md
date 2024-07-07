# Описание юнит-тестов для класса <u>BooksCollector</u>
## По методам:
### add_new_book
- <u>**test_add_new_book_two_books_added**</u> <br>
Тест добавляет две книги и проверяет их наличие в словаре `books_genre`.
- <u>**test_add_new_book_exceeds_length_book_not_added**</u> <br>
Тест пробует добавить книгу названием длиною 41 символ и проверяет ее отсутствие в словаре `books_genre`.
- <u>**test_add_new_book_duplicate_book_not_added**</u> <br>
Тест пробует добавить одну и ту же книгу дважды и проверяет количество записей в словаре `books_genre`.
### set_book_genre
- <u>**test_set_book_genre_existent_genre_setted**</u> <br>
Тест пробует добавить жанр из списка для книги и проверяет его наличие у этой записи.
- <u>**test_set_book_genre_nonexistent_genre_not_setted**</u> <br>
Тест пробует добавить несуществующий жанр для книги и проверяет его отсутствие у этой записи.
### get_book_genre
- <u>**test_get_book_genre_setted_genre_getted**</u> <br>
Тест добавляет жанр для книги и проверяет его получение у этой записи.
### get_books_genre
- <u>**test_get_books_genre_two_books_with_genre_dict_getted**</u> <br>
Тест добавляет 2 книги и проверяет наполнение словаря `books_genre`.
### get_books_with_specific_genre
- <u>**test_get_books_with_specific_genre_two_books_with_different_genre_book_getted**</u> <br>
Тест добавляет 2 книги разных жанров и проверяет получение одной книги указанного в методе жанра.
### get_books_for_children
- <u>**test_get_books_for_children_two_books_with_different_genre_book_getted**</u> <br>
Тест добавляет 2 книги разных жанров и проверяет получение одной книги без возврастного ограничения.
### add_book_in_favorites
- <u>**test_add_book_in_favorites_one_book_book_added**</u> <br>
Тест добавляет 1 книгу в список избранного `favorites` и проверяет ее наличие там.
### delete_book_from_favorites
- <u>**test_delete_book_from_favorites_one_book_book_deleted**</u> <br>
Тест убирает 1 книгу из списка избранного в `favorites` и проверяет ее отсутствие там.
### get_list_of_favorites_books
- <u>**test_get_list_of_favorites_books_no_books_list_empty**</u> <br>
Тест проверяет получение списка избранного при отсутствии записей в нем. 


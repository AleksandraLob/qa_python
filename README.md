# qa_python

# пример теста
test_add_new_book_add_two_books - добавление двух книг

# Тесты для метода add_new_book
test_add_new_book_success - Проверяем, что книга добавляется корректно
test_add_new_book_name_already_exists - Проверяем, что книга не добавляется, если её имя уже существует
# Тесты для метода add_new_book параметризованные
test_add_new_book_name_too_long_short - Проверяем, что книга не добавляется, если её имя слишком длинное, либо 0
test_add_new_book_name_long_short - Проверяем, что книга добавляется, если её имя слишком длинное, либо 1


# Тесты для метода set_book_genre
test_set_book_genre_success - Проверяем, что жанр книги устанавливается корректно
test_set_book_genre_book_not_exists - Проверяем, что жанр книги не устанавливается, если книга не существует
test_set_book_genre_genre_not_exists - Проверяем, что жанр книги не устанавливается, если жанр не существует

# Тесты для метода get_books_with_specific_genre
test_get_books_with_specific_genre_success - Проверяем, что получаем список книг с определённым жанром корректно
test_get_books_with_specific_genre_genre_not_exists - Проверяем, что получаем пустой список, если жанр не существует

# Тесты для метода get_books_genre
test_get_books_genre_success - Проверяем словрь книг, имена и жанры

# Тесты для метода get_books_for_children
test_get_books_for_children_success - Проверяем, что получаем список книг, подходящих детям, корректно

# Тесты для метода add_book_in_favorites
test_add_book_in_favorites_success - Проверяем, что книга добавляется в избранное корректно
test_add_book_in_favorites_book_not_exists - Проверяем, что книга не добавляется в избранное, если она не существует
test_add_book_in_favorites_already_in_favorites - Проверяем, что книга не добавляется в избранное, если она уже там есть

# Тесты для метода delete_book_from_favorites
test_delete_book_from_favorites_success - Проверяем, что книга удаляется из избранного корректно

# Тесты для метода get_list_of_favorites_books
test_get_list_of_favorites_books_success - Проверяем список избранного
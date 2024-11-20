# qa_python
test_add_new_book_add_same_book_twice - добавление одной и той же книги дважды, второй раз книга в словарь books_genre не добавляется

test_add_new_book_add_book_with_empty_name - добавление книги с пустым именем, книга не добавляется в словарь books_genre

test_set_book_genre_add_two_books - добавляем две книги и к ним же указываем жанр, обе книги добавлены в словарь books_genre

test_get_book_genre_get_book_genre - проверяем работу метода, с одной книгой

test_get_books_for_children_get_comedy - получаем комедию после добавления двух книг

test_set_book_genre_add_genre_without_adding_book - жанр для недобавленной книги, книга не добавляется в словарь books_genre

test_get_book_genre_get_existed_book - получаем жанр существующей книги, он соответствует ожидаемому

test_get_books_with_specific_genre_get_two_comedies - добавляем 2 комедии и 1 фильм ужасов, вызываем метод с параметром "комедия", получаем оба фильма жанра "комедия" 

test_get_books_genre_get_dict_with_two_books - добавляем две книги, проверяем, что добавилось именно две

test_add_book_in_favorites_add_two_books - добавляем две книги в избранное, проверяем, что в список favorites добавилось именно две 

test_delete_book_from_favorites_add_two_books_and_delete_one - в избранное добавляем две книги и удаляем одну, проверяем, что список favorites содержит одну книгу

test_delete_book_from_favorites_add_book_and_delete_book_twice - в избранное добавляем книгу и удаляем ее дважды, длинна списка равна 0, метод отработал без ошибок при попытке удалить отсутствующую в списке книгу

test_get_list_of_favorites_books - добавляем в список избранного книгу и получаем ее
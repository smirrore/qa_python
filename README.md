# qa_python


1) test_add_new_book_add_two_books
- создаем экземпляр (объект) класса BooksCollector
- добавляем книгу
- проверяем, что книгидобавилось
- проверяем словарь books_rating, который нам возвращает длину 2 при использовании метода get_books_rating

2) test_add_new_book_twice_same_books_only_one_added
- создаем экземпляр (объект) класса BooksCollector
добавляем книгу дважды
Проверяем, что в словаре books_rating находится один элемент

3) test_set_book_rating_missing_book_get_zero
- создаем экземпляр (объект) класса BooksCollector
присваиваем рейтинг книге, которой нет в словаре books_rating
проверяем, что метод get_books_with_specific_rating(рейтинг книги)
 Возвращает нам пустой список

4) test_get_book_rating_true_book_name_positiv_result
- создаем экземпляр (объект) класса BooksCollector
добавлеяем книгу в словарь books_rating
присваиваем книге рейтинг
проверяем, что при использовании метода get_book_rating(Имя книги) получаем тот рейтинг, что ранее ей присвоили

5) test_get_books_with_specific_rating_valid_rating_get_no_empty_list
- создаем экземпляр (объект) класса BooksCollector
добавляем пять книг
присваиваем им рейтинг
проверяем, что метод get_books_with_specific_rating возвращает книги с тем рейтингом, что указан в аргументе

6) test_get_books_rating_get_two_books_no_empty_list
- создаем экземпляр (объект) класса BooksCollector
- добавляем 2 книги 
присваиваем этим двум книгам рейтинг 
проверяем, что метод get_books_rating возвращает нам словарь с ранее добавленными книгами и их рейтингом

7) test_add_book_in_favorites_book_not_listed_not_added
создаем экземпляр (объект) класса BooksCollector
добавляем в избранное книгу, которая отсутствует в словаре books_rating
проверяем, что метод get_list_of_favorites_books возвращает пустой список

8) test_delete_book_from_favorites_delete_twice_not_added_in_list
- создаем экземпляр (объект) класса BooksCollector
добавляем в избранное книгу
присваиваем добавленной книге рейтинг
добавляем книгу в избранное
удаляем книгу из избранного 
повторно удаляем книгу из избранного 
проверяем, что метод get_list_of_favorites_books возвращает пустой список
9) test_get_list_of_favorites_books_add_two_books_get_two_books
- создаем экземпляр (объект) класса BooksCollector
добавляем книгу в список books_rating
добавляем книгу в избранное 
проверяем, что метод get_list_of_favorites_books возвращает список с добавленной книгой
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
        # добавляем книгу
        collector.add_new_book('Гордость, предубеждение и зомби')
        collector.add_new_book('Как достать соседа')
        # проверяем, что книгидобавилось
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2
    def test_add_new_book_twice_same_books_only_one_added(self):
        collector = BooksCollector()
        collector.add_new_book('Тестирование для чайников')
        collector.add_new_book('Тестирование для чайников')
        assert len(collector.get_books_rating()) == 1

# Нельзя выставить рейтинг книге, которой нет в списке
    def test_set_book_rating_missing_book_get_zero(self):
        collector = BooksCollector()
        collector.set_book_rating('Тестовая книга',6)
        assert collector.get_books_with_specific_rating(6) == []

# Получения рейтинга книги по ее имени
    def test_get_book_rating_true_book_name_positiv_result(self):
        collector = BooksCollector()
        book_name = 'Теория плоской земли'
        book_rating = 6
        collector.add_new_book(book_name)
        collector.set_book_rating(book_name, book_rating)
        assert collector.get_book_rating(book_name) == book_rating

# выводим список книг по определенному рейтингу
    def test_get_books_with_specific_rating_valid_rating_get_no_empty_list(self):
        collector = BooksCollector()
        collector.add_new_book('Теория плоской земли')
        collector.set_book_rating('Теория плоской земли', 3)
        collector.add_new_book('Мамин Криптоинвестор')
        collector.set_book_rating('Мамин Криптоинвестор', 6)
        collector.add_new_book('Основы эксплуатации PyCharm')
        collector.set_book_rating('Основы эксплуатации PyCharm', 9)
        collector.add_new_book('Хроники нейроманаха Феофана')
        collector.set_book_rating('Хроники нейроманаха Феофана', 9)
        collector.add_new_book('Новая книга')
        collector.set_book_rating('Новая книга', 9)
        rating = 9
        assert collector.get_books_with_specific_rating(rating) == ['Основы эксплуатации PyCharm', 'Хроники нейроманаха Феофана', 'Новая книга']

#Получение словаря  book_rating
    def test_get_books_rating_get_two_books_no_empty_list(self):
        collector = BooksCollector()
        collector.add_new_book('Мамин Криптоинвестор')
        collector.set_book_rating('Мамин Криптоинвестор', 6)
        collector.add_new_book('Основы эксплуатации PyCharm')
        collector.set_book_rating('Основы эксплуатации PyCharm', 9)
        assert collector.get_books_rating() == {'Мамин Криптоинвестор': 6, 'Основы эксплуатации PyCharm': 9}

#Добавление несуществующей книги в избранное
    def test_add_book_in_favorites_book_not_listed_not_added(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Новая книга')
        assert collector.get_list_of_favorites_books() == []

# Повторное удаление книги из избранного
    def test_delete_book_from_favorites_delete_twice_not_added_in_list(self):
        collector = BooksCollector()
        collector.add_new_book('Книга для избранного')
        collector.set_book_rating('Книга Книгадля избранного', 10)
        collector.add_book_in_favorites('Книга для избранного')
        collector.delete_book_from_favorites('Книга для избранного')
        collector.delete_book_from_favorites('Книга для избранного')
        assert collector.get_list_of_favorites_books() == []

#Получение списка избранных книг
    def test_get_list_of_favorites_books_add_two_books_get_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Мамин Криптоинвестор')
        collector.add_book_in_favorites('Мамин Криптоинвестор')
        assert collector.get_list_of_favorites_books() == ['Мамин Криптоинвестор']


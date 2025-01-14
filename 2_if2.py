"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""

def is_string(str1, str2):
    if type(str1) != str or type(str2) != str:
        result = 0
    elif str1 == str2:
        result = 1
    elif len(str1) > len(str2):
        result = 2
    elif str2 == 'learn':
        result = 3
    return result

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(is_string(1, 'asdfg'))
    print(is_string('asdfg', 'asdfg'))
    print(is_string('asdfgh', 'asdfg'))
    print(is_string('agh', 'learn'))


if __name__ == "__main__":
    main()

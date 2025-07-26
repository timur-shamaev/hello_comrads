def test_function(func, argument, expected_result):
    try:
        # Вызываем переданную функцию с аргументом
        result = func(argument)

        # Сравниваем полученный результат с ожидаемым
        return result == expected_result
    except Exception as e:
        # Если произошла ошибка при выполнении функции
        print(f"Ошибка при выполнении функции: {e}")
        return False


# Пример функции для тестирования
def square(n):
    return n ** 2
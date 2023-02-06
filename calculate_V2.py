from tools import сhecking_expression


def calculate(expression):
    """
    Эта функция вычисляет выражение, переданное в качестве аргумента. Выражение должно быть строкой, состоящей из цифр и следующих знаков: "+", "-", "*", "/".
    
    Аргументы:
    expression (str): Выражение для вычисления.
    
    Возвращает:
    result (int/float): Результат вычисления. Если выражение недопустимо, возвращает None.
    
    Пример:
    >>> calculate("2+2")
    4
    >>> calculate("2/0")
    Ошибка при вычислении выражения: division by zero
    None
    """
    сhecking_expression(expression)
    try:
        result = eval(expression)
        return result
    except Exception as error:
        print("Ошибка при вычислении выражения:", error)
        return None



from tools import сhecking_expression


def calculate(expression):
    сhecking_expression(expression)
    try:
        result = eval(expression)
        return result
    except Exception as error:
        print("Ошибка при вычислении выражения:", error)
        return None

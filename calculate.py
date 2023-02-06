from tools import сhecking_expression

def calculate():
    """
    Эта функция принимает выражение в виде строки и вычисляет его результат, если это возможно. 
    Если выражение содержит недопустимые символы или некорректно составлено, функция выдает сообщение об ошибке.

    Автотесты:
    >>> вычисление("1+1")
    Результат: 2
    >>> вычисление("1+a")
    Ошибка при вычислении выражения: invalid literal for int() with base 10: 'a'
    >>> вычисление("*1+1")
    Выражение не может начинаться с '*' или '/'
    """
    while True:
        expression = input("Введите строку, состоящую из цифр и следующих знаков: +, -, *, / или 'exit' для выхода: ")       
        if expression == "exit":
            break     
        if not сhecking_expression(expression):
            continue
        try:
            result = eval(expression)
            print("Результат:", result)
        except Exception as error:
            print("Ошибка при вычислении выражения:", error)

if __name__ == "__main__":
    calculate()


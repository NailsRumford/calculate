def calculate(value):
    if not isinstance(value, str) or not all(c in "0123456789+-*/" for c in value):
        print ("На вход должна приходить строка, состоящая из цифр и следующих знаков: +, -, *, /")
    try:
        result = eval(value)
        return result
    except Exception as error:
        print("Ошибка при вычислении выражения:", error)

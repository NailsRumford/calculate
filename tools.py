def сhecking_expression(expression):
    if not isinstance(expression, str) or not all(c in "0123456789+-*/" for c in expression):
        print ("На вход должна приходить строка, состоящая из цифр и следующих знаков: +, -, *, /")
        return False
    elif expression[0] in '*/':
        print("Выражение не может начинаться с '*' или '/'")
        return False
    elif expression[-1] in '+-*/':
        print("Выражение не может заканчиваться на '+', '-', '*' или '/'")
        return False
    else:
        return True
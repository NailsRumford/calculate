def calculate():
    while True:
        value = input("Введите строку, состоящую из цифр и следующих знаков: +, -, *, / или 'exit' для выхода: ")       
        if value == "exit":
            break     
        if not all(c in "0123456789+-*/" for c in value):
            print("На вход должна приходить строка, состоящая из цифр и следующих знаков: +, -, *, /")
            continue
        try:
            result = eval(value)
            print("Результат:", result)
        except Exception as error:
            print("Ошибка при вычислении выражения:", error)

if __name__ == "__main__":
    calculate()
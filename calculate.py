from tools import сhecking_expression

def calculate():
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
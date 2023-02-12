from excep import *
from mod_calc import *
from logg import logging

type_dict = {"1": "rational", "2": "complex"}
operator = {"1": "+", "2": "-", "3": "*", "4": "/", "5": "^", "6": "sqrt"}

def menu():
    while True:
        num_tipe = input("Введите тип переменной:\n"
                            "1 - Рациональные числа\n"
                            "2 - Комплексные числа\n"
                            "0 - Выход\n")
        match num_tipe:
            case "1":
                menu_calc(num_tipe)
                logging.info("Rational nambers")
                pass
            case "2":
                menu_calc(num_tipe)
                logging.info("Complex nambers")
                pass
            case "0":
                logging.info("Stop program.")
                print("Работа завершена")
                break
            case _:
                logging.warning("Ошибка ввода типа числа")
                print("Ошибка ввода")

def menu_calc(data_type):
    global operator
    logging.info(f"Запускаем калькулятор для {type_dict[data_type]}")
    first, second = 0, 0 
    result = "q"
    sign = "/"
    while True:
        op = input("Operations:"
                   "\n1 - Сумма"
                   "\n2 - Разница"
                   "\n3 - Умножение"
                   "\n4 - Деление"
                   "\n5 - Степень"
                   "\n6 - Извлечение квадрата"
                   "\n7 - Вернуться\n")

        if op.isdigit() and int(op) in range(1, 6):
            if data_type == "1":
                first, second = check_in([input(f"Введите {i + 1} число: ") for i in range(2)], data_type)
            elif data_type == "2":
                first, second = [complex(*check_in([input(f"Enter {i + 1} real part: "),
                                                    input(f"Enter {i + 1} imaginary number: ")], data_type, i))
                                 for i in range(2)]
        match op:
            case "1":
                result = sum_use(first, second)
                logging.info(f"Сумма: {first} + {second} = {result}")
            case "2":
                result = sub_use(first, second)
                logging.info(f"Разница: {first} - {second} = {result}")
            case "3":
                result = mult_use(first, second)
                logging.info(f"Произведение: {first} * {second} = {result}")
            case "4":
                if data_type == "1":
                    second = check_zero_real(str(second))
                    sign = menu_divisions()
                    operator[op] = sign
                else:
                    second = check_zero_comp(first, second)
                    operator[op] = "/"
                if sign:
                    result = div_use(first, second)
                    logging.info(f"Частное: {first} {sign} {second} = {result}")
            case "5":
                result = pow_use(first, second)
                logging.info(f"Число {first} в степени {second} = {result}")
            case "6":
                second = ""
                if data_type == "1":
                    first = check_in_one([input(f"Enter a number: ")], data_type)
                else:
                    first = complex(*check_in_one([input(f"Enter real part: "),
                                                   input(f"Enter imaginary number: ")], data_type))
                result = sqr_use(first)
                logging.info(f"Корень из {first} = {result}")
            case "7":
                logging.info('Прекращение работы')
                print()
                break
            case _:
                logging.warning(f"Main menu, wrong item selected.")
                print("Ошибка вычислений, попробуйте еще")
                continue
        if result != "q":
            print(f"Res: {first} {operator[op]} {second} = {result}", end="\n\n")

def menu_divisions():
    logging.info(f"Start menu divisions.")
    while True:
        op = input("Operations:\n"
                   "1 - '/'\n"
                   "2 - '//'\n"
                   "3 - '%'\n"
                   "4 - previous menu\n")
        match op:
            case "1":
                return "/"
            case "2":
                return "//"
            case "3":
                return "%"
            case "4":
                logging.info('Stop divisions menu')
                print()
                return 0
            case _:
                logging.warning(f"Main menu, wrong item selected.")
                print("Ошибка вычислений, попробуйте еще")

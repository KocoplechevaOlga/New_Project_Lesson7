def menu():
    while True:
        num_tipe = input("Enter:\n"
                            "1 - Рациональные числа\n"
                            "2 - Комплексные числа\n"
                            "0 - Выход\n")
        match num_tipe:
            case "1":
                pass
            case "2":
                pass
            case "0":
                break
            case _:
                print("Ошибка ввода")
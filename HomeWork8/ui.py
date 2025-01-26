from logger import input_data, print_data, delete_data, edit_data

def interface():
    print("Добрый день! Вы попали на специальный бот справочник от GeekBrains! \n"
          "1 - запись данных \n"
          "2 - вывод данных \n"
          "3 - удаление данных \n"
          "4 - изменение данных")
    command = int(input("Введите число: "))
    
    while command < 1 or command > 4:
        print("Неправильный ввод")
        command = int(input("Введите число: "))
        
    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        delete_data()
    elif command == 4:
        edit_data()
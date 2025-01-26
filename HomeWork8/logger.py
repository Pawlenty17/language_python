from data_create import name_data, surname_data, phone_data, address_data

# Функция для ввода данных
def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные: \n\n"
                    f"1: Вариант: \n"
                    f"{name}\n{surname}\n{phone}\n{address}\n\n"
                    f"2: Вариант: \n"
                    f"{name}; {surname}; {phone}; {address}\n\n"
                    f"Выберите вариант: "))
    
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input("Введите число: "))
    
    if var == 1:
        with open('first.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('second.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}; {surname}; {phone}; {address}\n\n")

# Функция для вывода данных
def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('first.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i + 1]))
                j = i
        print(''.join(data_first_list))
    
    print('Вывожу данные из 2 файла: \n')
    with open('second.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)

# Функция для поиска данных
def search_data(filename, search_term):
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.readlines()
        results = []
        current_record = []
        for line in data:
            if line.strip() == '':
                if current_record and any(search_term.lower() in field.lower() for field in current_record):
                    results.append(current_record)
                current_record = []
            else:
                current_record.append(line.strip())
        if current_record and any(search_term.lower() in field.lower() for field in current_record):
            results.append(current_record)
        return results

# Функция для удаления данных
def delete_data():
    search_term = input("Введите имя, фамилию или телефон для поиска записи: ").strip()
    
    # Удаление из первого файла
    with open('first.csv', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    skip = False
    for line in lines:
        if search_term.lower() in line.lower():
            skip = True  # Пропустить запись, если найдено совпадение
        if line.strip() == '':
            if not skip:
                new_lines.append(line)
            skip = False
        elif not skip:
            new_lines.append(line)
    
    with open('first.csv', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    # Удаление из второго файла
    with open('second.csv', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    skip = False
    for line in lines:
        if search_term.lower() in line.lower():
            skip = True  # Пропустить запись, если найдено совпадение
        if line.strip() == '':
            if not skip:
                new_lines.append(line)
            skip = False
        elif not skip:
            new_lines.append(line)
    
    with open('second.csv', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print("Запись удалена.")

# Функция для изменения данных
def edit_data():
    search_term = input("Введите имя, фамилию или телефон для поиска записи: ").strip()
    
    # Поиск в первом файле
    results = search_data('first.csv', search_term)
    if results:
        print("Найденные записи в первом файле:")
        for i, record in enumerate(results, 1):
            print(f"{i}. {record}")
        choice = int(input("Выберите номер записи для изменения: ")) - 1
        if 0 <= choice < len(results):
            print("Введите новые данные:")
            name = name_data()
            surname = surname_data()
            phone = phone_data()
            address = address_data()
            new_record = [name, surname, phone, address]
            
            # Удаление старой записи
            delete_data()
            
            # Добавление новой записи
            input_data()
            print("Запись изменена.")
        else:
            print("Неверный номер записи.")
    else:
        print("Записи не найдены.")

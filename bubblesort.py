
userChoice = 0
values = [23, 55, 4, 0, 2]



print('Меню:')
print('1. Вывести на экран все значения')
print('2. Добавить значение')
print('3. Удалить значение')
print('4. Найти значение')
print('5. Отсортировать значения')
print('6. Выйти')
print('Введите опцию:')

# Считываем ввод пользователя с клавиатуры
userChoice = int(input())


while userChoice != 6:
    if (userChoice < 1) | (userChoice > 6):
        print('Такой опции нет, выберите существующую опцию.')
        userChoice = int(input())
    else:

        if userChoice == 1:
            print(values)

        elif userChoice == 2:
            print('Введите новое число:')
            newValue = int(input())
            values.append(newValue)

        elif userChoice == 3:
            if len(values) != 0:
                print('Введите число для удаления:')
                searchValue = int(input())
                counter = 0
                deleted = False
                for count in range(0, len(values)):
                    if (values[count] == searchValue) & (count < len(values)):
                        deleted = True
                        while count+1 < len(values):
                            values[count] = values[count+1]
                            count = count+1
                if deleted is True:
                    del values[count]
                elif deleted is False:
                    print('Значения нет в базе данных.')
            else:
                print('База пустая! Добавте значения!')

        elif userChoice == 4:
            if len(values) != 0:
                print('Введите число для поиска его индекса:')
                searchValue = int(input())
                found = False
                for count in range(0, len(values)):
                    if values[count] == searchValue:
                        found = True
                        print('Индекс значения "', searchValue, '":', count)
                if found is False:
                    print('Значение не найдено!')
            else:
                print('База пустая! Не можем искать!')

        elif userChoice == 5:
            def sort(array):
                if len(array) != 0:
                    print('Список до:', array)
                    swapped = False

                    while swapped is False:
                        for index in range(len(array)-1, 0, -1):
                            for i in range(index):
                                # если values[i] > values[i+1], поменять их местами
                                if array[i] > array[i+1]:
                                    array[i], array[i+1] = array[i+1], array[i]
                        return array



                else:
                    print('База пуста!')

            result = sort(values)
            print('Список после:' + str(result))



        print('\n Меню:')
        print('1. Вывести на экран все значения')
        print('2. Добавить значение')
        print('3. Удалить значение')
        print('4. Найти значение')
        print('5. Отсортировать значения')
        print('6. Выйти')
        print('Введите опцию:')
        userChoice = int(input())
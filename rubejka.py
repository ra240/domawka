def function2(array):
    total = 0
    for element in range(len(array)):
        total += array[element]

    return total

d = []
i = 0
while i < 5:
    k = int(input("Введите значение: "))
    d.append(k)
    i += 1


print(function2(d))
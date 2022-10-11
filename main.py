n = int(input())
mas = []
for i in range (n):
    mas.append(i)
    mas[i] = int(input())
t = input("Введите направление: по возрастанию, по убыванию\n")
if (t == "по возрастанию"):
    for i in range (n):
        for j in range (n - 1):
            if (mas[j] > mas[j + 1]):
                mas[j], mas[j+1] = mas[j+1], mas[j]
    print(mas)
else:
    if (t == "по убыванию"):
        for i in range (n):
            for j in range (n - 1):
                if (mas[j] < mas[j + 1]):
                    mas[j], mas[j+1] = mas[j+1], mas[j]
        print (mas)
    else:
        print("ошибка")
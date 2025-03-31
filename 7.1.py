arr = [1, 2, 3, 4, 5]
num = int(input("Введите число: "))

if num in arr:
    print("Исходный список: ", arr)
    print("Число пользователя: ", num)
    print("Вы угадали число!")
else:
    print("Исходный список: ", arr)
    print("Число пользователя: ", num)
    print("Такого числа нет")
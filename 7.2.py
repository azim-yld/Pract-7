import random

arr = [0,0,0,0,0,0,0,0,0,0]
for i in range(len(arr)):
    arr[i] = random.randint(1,10)

dup = []

for num in arr:
    if arr.count(num) > 1 and num not in dup:
        dup.append(num)

if dup:
    print ("Все числа: ", arr)
    print ("Повторяются числа: ", dup)
else:
    print ("Все числа: ", arr)
    print ("Числа не повторяются")
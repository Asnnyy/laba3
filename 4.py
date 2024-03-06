import random
schet1 = 0
schet2 = 0
kx = 3
<<<<<<< HEAD
=======
v = ["a", "b"]
>>>>>>> laba3/main
while schet2 != 3:
    a = random.randint(1, 100)
    b = random.randint(1,100)
    print(a, "+", b, "=")
    sum = a + b
    otv = int(input("Введите Ваш ответ"))
    if sum != otv:
        print("Ответ неверный")
        schet2 += 1
    else:
        print("Правильно")
        schet1 += 1
print("Игра окончена. Правильных ответов:", schet1)


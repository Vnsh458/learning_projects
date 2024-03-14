import random

print("Я загадал число от 1 до 10, твоя задача отгадать. Игра началась.")
x = random.randint(1, 10)
tr = 1
jo = 0

while True:
    y = input("Введи число: ")

    while True:
        try:
            y = int(y)
            break
        except:
            tr += 1
            if jo <= 5:
                jo += 1
                y = input("Ты не ввел число, но я все равно это посчитал за попытку: ")
            elif jo <= 10:
                jo += 1
                y = input("Мое терпение на исходе, кожаный мешок >:( : ")
            elif jo == 11:
                jo += 1
                print(f"Я вижу, ты не настроен играть\nПопыток разбить мое сердечко: {jo}(")
                break


    if jo >= 11: break
    elif y < x: print("Неверно. Число больше")
    elif y > x: print ("Неверно. Число меньше")
    elif y == x:
        print(f"Поздравляю, ты угадал.\nКоличество попыток: {tr}")
        break
    tr += 1

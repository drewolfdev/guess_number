import random

number = random.randint(1, 100)


while True:
    user_number = int(input('Введите число: '))
    if number > user_number:
        print('Ваше число меньше того, что загадано')
    elif number < user_number:
        print('Ваше число больше того, что загадано')
    else:
        print('Отличная интуиция! Вы угадали число :)')
        break
    
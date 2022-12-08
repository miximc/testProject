time = 25
while time > 24:

    time = int(input('Сколько сейчас часов? '))
    if time > 24:
        print('Вы ввели неправильный час, повторите.')
if 6 < time < 12:
    print('Доброе утро!')
elif 11 < time < 17:
    print('Добрый день!')
elif 16 < time < 24:
    print('Добрый вечер!')
else:
    print('Доброй ночи!')

print('priverka')
while True:
    days = 1
    start = float(input('Старт (km)'))
    finish = float(input('Желаемый результат (km)'))
    if start <= 0 and finish <= 0:
        print('Err')
        print('Числа должны быть положительными и стартовый показатель != 0')
    else:
        while start < finish:
            start = start + start * 0.1
            days = days + 1

        print(f'Вы добьетесь результата за {days} дней')
        break
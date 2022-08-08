revenue = float(input('Выручка равняется:'))
costs = float(input('Издержки равняются:'))
result = revenue - costs
if result > 0:
    print('Прибыль составляет {0}'.format(result))
    print(f'Рентабильность составляет {100 * (result / costs):.1f}%')
    staff = int(input('Количество сотрудников:'))
    print(f'Каждый сотрудник получит {result / staff:.2f}')
else:
    result <= 0
    print('Убыток')
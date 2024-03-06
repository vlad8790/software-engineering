from datetime import datetime
from math import sqrt

def main(**kwargs):
    """
        result - Возвращает квадратный корень суммы квадратов двух элементов кортежей

        :param kwargs: Принимаемые кортежи

        :rtype: float
        :return: Печатает result в консоли
    """
    for key in kwargs.items():
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)
        print(result)

if __name__ == '__main__': #точка входа
    start_time = datetime.now() #фиксируем время перед запуском main
    #Запуск функции main
    main(
        one = [10,3],
        two = [5,4],
        three = [15,13],
        four = [93,53],
        five = [133,15]
    )
    time_costs = datetime.now() - start_time #Подсчет затраченного времени на выполнение main

    print(f"Время выполнения программы - {time_costs}") #вывод затраченного на исполнение программы времени
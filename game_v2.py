"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число методом половинного деления по интервалу

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Инициируем начальные условия выполнения поиска:
    count = 0 #Количество попыток
    values = [0,101]

    while True: #Запускаем цикл поиска заданного числа
        count += 1
        predict_number = (values[0] + values[1])//2  # предполагаемое число
        difference = number - predict_number #Определяем разницу между заданными число и предполагаемым
        if difference == 0:
            break #Выход из цикла
        if difference < 0:
            values[1] = predict_number #Корректируем верхнюю границу интервала поиска
        else:
            values[0] = predict_number #Корректируем нижнюю границу интервала поиска
    return count
            
   


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)

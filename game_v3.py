"""Игра угадай число
компьютер сам загадывает и сам отгадывает число"""

import numpy as np

def random_predict(number: int = 1) -> int:
    """Угадываем число последовательными приближениями

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Количество попыток
    """

    count = 0
    left_num = 0
    right_num = 101
    
    while True:
        count += 1
        mean_num = (right_num + left_num) // 2 
        if number == mean_num:
            break  # выход из цикла, если число угадано
        elif number > mean_num:
            left_num = mean_num # смещаем левую границу диапозона
        else:
            right_num = mean_num # смещаем правую границу диапозона
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает алгоритм

    Args:
        random_predict (func): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(5) # фиксируем сид для вопроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    # RUN
    score_game(random_predict)
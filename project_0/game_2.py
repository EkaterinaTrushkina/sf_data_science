"""Игра угадай число.
Компьютер сам загадывает и угадывает число.
Компьютер угадает число меньше чем за 20 попыток
"""
import numpy as np

def random_predict(number:int=1) -> int:
    """Компьютер угадывает число меньше чем за 20 попыток
    корректируется значение, если загаданное число больше или меньше.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    min = 1
    max = 100
    predict_number = np.random.randint(1, 101) # загадываем рандомное число, используя генератор рандомных чисел
    while True:
        count += 1
        if predict_number > number:
            max = predict_number - 1 #максимум диапазона угадывания
            predict_number = (min + max) // 2
        elif predict_number < number:
            min = predict_number + 1 # минимум диапазона
            predict_number = (min + max) // 2
        else:
            break
    return(count)
        
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    score_game(random_predict)
# ПРАКТИЧЕСКОЕ ЗАДАНИЕ №1
# Задача №1. Реализовать функционал: Вывод средней цены за период
# Реализовать функционал: Вывод средней цены за период
#
# Ваша задача:
#
# 1. Вывод средней цены за период:
#
# Цель:
# Реализовать функцию calculate_and_display_average_price(data), которая вычисляет и выводит среднюю цену закрытия акций за заданный период.
#
# Реализация:
# Функция будет принимать DataFrame и вычислять среднее значение колонки 'Close'. Результат будет выводиться в консоль.

import pandas as pd


def calculate_and_display_average_price(data):
    all_period = len(data)
    average_period = data['Close'].sum() / all_period
    return average_period


# Задача №2. Реализовать функционал: Уведомление о сильных колебаниях
#
# Реализовать функционал: Уведомление о сильных колебаниях
#
# Ваша задача:
# 1. Уведомление о сильных колебаниях
#
# Цель:
#  Разработать функцию notify_if_strong_fluctuations(data, threshold), которая анализирует данные
#  и уведомляет пользователя, если цена акций колебалась более чем на заданный процент за период.
#
# Реализация:
# Функция будет вычислять максимальное и минимальное значения цены закрытия и сравнивать разницу с заданным порогом.
# Если разница превышает порог, пользователь получает уведомление.

def notify_if_strong_fluctuations(data, threshold):
    # for i in range(len(data['Close'][1]), len(data['Close'])+1):
    #     print(i, i-1, i+1)
    min_value = data['Close'].min()
    max_value = data['Close'].max()
    actual_differential = round(((max_value - min_value)/min_value * 100), 2)
    if actual_differential <= threshold:
        print(f'Максимальные колебания за выбранный период составило: {actual_differential}%,'
              f'что меньше проверочного - {threshold}%. '
              'Всё нормально, парни, продолжаем работать!')
    else:
        print('Тревога! Тревога! Волк унёс зайчат!'
              f'Максимальные колебания за выбранный период - {actual_differential}%, превышают проверочные - {threshold}%. '
              'Вы выбрали волнительный период...')


def export_data_to_csv(ticker, period, data_average, filename=None):
    average_round = round(float(data_average), 2)
    data = {'Name': [ticker], 'Selected period': [period], 'Average value': [average_round]}
    frame = pd.DataFrame(data)
    if filename is None:
        filename = f"Average_value_{ticker}_for_{period}"
    frame.to_csv(f'{filename}.csv', index=False)
# ПРАКТИЧЕСКОЕ ЗАДАНИЕ
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
import yfinance as yf
import data_download as dd
import matplotlib.pyplot as plt
import pandas as pd

def calculate_and_display_average_price(data):
    all_period = len(data)
    average_period = data['Close'].sum() / all_period
    return average_period

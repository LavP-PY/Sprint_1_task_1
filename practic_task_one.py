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

ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):")
period = input("Введите период для данных (например, '1mo' для одного месяца): ")

stock_data = dd.fetch_stock_data(ticker, period)
stock_data = dd.add_moving_average(stock_data)

def calculate_and_display_average_price(data, ticker, period, filename=None):
    plt.figure(figsize=(10, 6)) # размеры (ширина и высота) диаграммы

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
            plt.plot(dates, data['Average_period'].values, label='Average all period')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')
        plt.plot(data['Date'], data['Average_period'], label='Average all period')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")

averenge = calculate_and_display_average_price(data=stock_data, ticker=ticker, period=period)
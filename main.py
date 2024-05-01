"""
О проекте.
Этот проект предназначен для загрузки исторических данных об акциях и их визуализации.
Он использует библиотеку yfinance для получения данных и matplotlib с plotly для создания графиков.
Пользователи могут выбирать различные тикеры и временные периоды для анализа,
а также просматривать движение цен и скользящие средние на графике.

Структура и модули проекта:
1. main.py:
- Является точкой входа в программу.
- Запрашивает у пользователя следующие данные:
    тикер акции, временной период (общий или точные даты (начала и окончания)), выбор стиля отображения графиков,
    данные о максимальном допустимом значении колебания цены, а также название csv-файла, куда будут записаны данные.
- загружает данные из источника https://finance.yahoo.com/, обрабатывает их и выводит результаты в виде графика:
    * данные о ценах закрытия за указанный период;
    * скользящая средняя на основе цен закрытия;
    * индикаторы RSI (индекс относительной силы): простая (SMA) и экспоненциальная (EMA) скользящие средние;
    * индикатор схождения-расхождения скользящих средних MACD (Moving Average Convergence/Divergence)
    * стандартные отклонения цены закрытия;
    * также на консоль выводит среднюю цену закрытия акций за заданный период;
- уведомляет о сильных колебаниях, сравнивая с введёнными данными;
- экспортирует данные в csv-файл

2. Модуль data_download.py:
- отправляет запроc на https://finance.yahoo.com/ по выбранным тикеру и периоду;
- загружает данные по акции в виде таблицы;
- извлекает данные из полученной таблицы и рассчитывает необходимые индикаторы;

3. Модуль data_plotting.py:
- отвечает за визуализацию данных;
- с помощью библиотеки matplotlib выстраиваются все графики перечисленные в main.py;
- с помощью библиотеки plotly строится интерактивный график данных цен закрытия выбранной акции.

4. Модуль
"""
import data_download as dd
import data_plotting as dplt
import practical_tasks as prt
from datetime import datetime
import logging
from test_data_csv import test_data
import csv


logger_info = logging.getLogger('Users_requests')
logger_warning = logging.getLogger('wtf')

logger_info.setLevel(logging.DEBUG)
logger_warning.setLevel(logging.WARNING)

userReq_info = logging.FileHandler('users_requests.log', 'w', 'utf-8')
wtf_warn = logging.FileHandler('WhatTheHappen.log', 'w', 'utf-8')

formatter = logging.Formatter('%(asctime)s _ %(levelname)s: %(message)s')


def main():
    # logger_info.debug('Начало сеанса')
    logger_info.addHandler(userReq_info)
    logger_info.debug('Начало сеанса')
    userReq_info.setFormatter(formatter)
    logger_warning.addHandler(wtf_warn)
    wtf_warn.setFormatter(formatter)

    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print(
        "Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print(
        "Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):")
    logger_info.info(f"Введенный тикер - {ticker}")

    date = input("Вы хотите указать общий период или точные даты? Введите '0'-общий или '1'-точные даты:")
    magic_words = ['0', '1']
    while date not in magic_words:
        date = input("ОШИБКА! Введите '0' или '1':")
        logger_warning.warning(f"Введены НЕВЕРНЫЕ данные даты - {date}")

    if date == '0':
        period = input("Введите период для данных (например, '1mo' для одного месяца): ")
        logger_info.info(f"Выбран общий период времени по тикеру {ticker} - {period}")
    elif date == '1':
        start_period = input("Введите дату начала периода анализа (формат ввода - ГГ-ММ-ДД):")
        end_period = input("Введите дату окончания периода анализа (формат ввода - ГГ-ММ-ДД):")
        period = str((datetime.strptime(end_period, '%Y-%m-%d') - datetime.strptime(start_period, '%Y-%m-%d')).days) + 'd'
        logger_info.info(f"Выбран точный период времени с {start_period} по {end_period}, что составило {period} дней")

    #choosing a print style
    style = {'1': 'Solarize_Light2', '2': '_classic_test_patch', '3': '_mpl-gallery', '4': '_mpl-gallery-nogrid',
             '5': 'bmh', '6': 'classic', '7': 'dark_background', '8': 'fast', '9': 'fivethirtyeight', '10': 'ggplot',
             '11': 'grayscale', '12': 'seaborn-v0_8', '13': 'seaborn-v0_8-bright', '14': 'seaborn-v0_8-colorblind',
             '15': 'seaborn-v0_8-dark', '16': 'seaborn-v0_8-dark-palette', '17': 'seaborn-v0_8-darkgrid',
             '18': 'seaborn-v0_8-deep', '19': 'seaborn-v0_8-muted', '20': 'seaborn-v0_8-notebook',
             '21': 'seaborn-v0_8-paper', '22': 'seaborn-v0_8-pastel', '23': 'seaborn-v0_8-poster',
             '24': 'seaborn-v0_8-talk', '25': 'seaborn-v0_8-ticks', '26': 'seaborn-v0_8-white',
             '27': 'seaborn-v0_8-whitegrid', '28': 'tableau-colorblind10'}
    num_style = input("Введите цифру (от 1 до 28 включительно) соответствующую нужному стилю, чтобы посмотреть полный список стилей - введите 0: ")
    list_of_style = list(style.keys()) + ['0']
    while num_style not in list_of_style:
        num_style = input("ОШИБКА! Введите значение от 0 до 28:")
        logger_warning.warning(f"Введены НЕВЕРНЫЕ данные выбора стиля - {num_style}")
    if num_style == '0':
        print(style.items())
        num_style = input("Введите номер соответствующего стиля от 1 до 28: ")
        logger_info.info("Пользователь запросил список стилей")
    try:
        if 1 <= int(num_style) <= 28:
            choice_style = style.get(num_style)
            print(f'Вы выбрали - {choice_style} стиль', type(choice_style))
            logger_info.info(f"Пользователь выбрал {choice_style} стиль")
    except Exception:
        print('Стиль не был выбран, применён стандартный стиль')
        choice_style = None
        logger_info.info("Стиль не выбран пользователем")

    # Ввод данных пользователем о максимальном допустимом значении колебания цены
    threshold = float(input("Введите максимальное допустимое значение колебания цены, % (например, 1.5 - для 1.5%; Если не требуется, то введите - 0): "))
    filename_csv = input("Введите название csv файла, для сохранения среднего значения (если вы не хотите выводить данные в таблицу, введите - 0; если название не принципиально введите - 1): ")

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

    # calculation data's average
    average = prt.calculate_and_display_average_price(stock_data)
    print(f'The average value for the selected period (Среднее значение за выбранный период): {average}')

    # notify about strong fluctuations
    if threshold == 0:
        logger_info.info(f"Максимальное допустимое значение колебания цены НЕ ЗАДАНО")
        pass
    elif threshold > 0:
        prt.notify_if_strong_fluctuations(stock_data, threshold)
        logger_info.info(f"Задано максимальное допустимое значение колебания цены - {threshold}%")

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period, choice_style)

    # writing data to csv
    try:
        filename_csv_int = int(filename_csv)
        if filename_csv_int == 1:
            filename = prt.export_data_to_csv(data_average=average, ticker=ticker, period=period)
            logger_info.info(f"Среднее значение за выбранный период сохранено в csv-файл - {filename}")
            # Добавляем тест на проверку информации в записанном файле csv
            assert test_data(filename_csv=filename) == average, 'записывается неверное среднее значение закрытия за период'

        elif filename_csv_int != 0:
            filename = prt.export_data_to_csv(data_average=average, ticker=ticker, period=period, filename=filename_csv)
            logger_info.info(f"Среднее значение за выбранный период сохранено в csv-файл - {filename}")
            # Добавляем тест на проверку информации в записанном файле csv
            assert test_data(filename_csv=filename) == average, 'записывается неверное среднее значение закрытия за период'

        # elif int(filename_csv_int) == 0:
        #     logger_info.info("ОТКАЗ от сохранения - Среднее значение за выбранный период в csv-файл")
    except Exception:
        filename = prt.export_data_to_csv(data_average=average, ticker=ticker, period=period, filename=filename_csv)
        logger_info.info(f"Среднее значение за выбранный период сохранено в csv-файл под именем - {filename}")

        # Добавляем тест на проверку информации в записанном файле csv
        assert test_data(filename_csv=filename) == average, 'записывается неверное среднее значение закрытия за период'

    logger_info.debug('Завершение сеанса')


if __name__ == "__main__":
    import doctest
    main()
    doctest.testmod()

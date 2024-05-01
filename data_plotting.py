import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go


def create_and_save_plot(data, ticker, period, choice_style=None, filename=None):
    """
    Принимает данные по акции с новыми расчитанными значениями
    для последующей визуализации с помощью библиотек matplotlib и plotly.
    :param data:
    :param ticker:
    :param period:
    :param choice_style:
    :param filename:
    :return:
    """
    # Установка стиля
    if choice_style is not None:
        plt.style.use(choice_style)

    plt.figure(figsize=(12, 18)) # размеры (ширина и высота) диаграммы
    plt.subplot(3, 1, 1)

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
            plt.plot(dates, data['Standart_deviation_list'].values, label='Standart deviation')

        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')
        plt.plot(data['Date'], data['Standart_deviation_list'], label='Standart deviation')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend(loc='center left')
    # plt.grid(True)

    plt.subplot(3, 1, 2)
    plt.title("RSI")
    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['RSI_ema'].values, label='RSI EMA')
            plt.plot(dates, data['RSI_sma'].values, label='RSI SMA')

        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['RSI_ema'], label='RSI EMA')
        plt.plot(data['Date'], data['RSI_sma'], label='RSI SMA')
    plt.legend()
    plt.grid(True)

    plt.subplot(3, 1, 3)
    plt.title("MACD")
    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['MCAD_main'].values, label='MCAD basic')
            plt.plot(dates, data['MCAD_signal'].values, label='MCAD signal')

        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['MCAD_main'], label='MCAD basic')
        plt.plot(data['Date'], data['MCAD_signal'], label='MCAD signal')
    plt.legend(loc='upper left')
    plt.grid(True)


    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart__{choice_style}.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")

    # Подключаем альтернативную библиотеку для построения графиков
    date_time = data.index.to_numpy()
    fig = go.Figure([go.Scatter(x=date_time, y=data['Close'].values)])
    fig.show()



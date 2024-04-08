import matplotlib.pyplot as plt


def create_and_save_plot(data, ticker, period, filename=None):
    plt.figure(figsize=(12, 18)) # размеры (ширина и высота) диаграммы
    plt.subplot(3, 1, 1)
    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')

        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()
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
    plt.legend()
    plt.grid(True)


    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")

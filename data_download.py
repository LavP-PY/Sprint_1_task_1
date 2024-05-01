import yfinance as yf


def fetch_stock_data(ticker, period):
    """
    Принимает имя тикера и период, введённые пользователем.
    :param ticker:
    :param period:
    :return: Возвращает таблицу с данными об акции
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data

def calculate_and_display_average_price_rsi(data, period=14, ema=True):
    """
    Принимает таблицу с данными акции. Рассчитывает (по скользящим значениям цены закрытия) и возвращает индекс RSI
    :param data:
    :param period:
    :param ema:
    :return: RSI (индекс относительной силы)
    """
    close_delta = data['Close'].diff()
    # Делаем две серии: одну для низких закрытий и одну для высоких закрытий
    up = close_delta.clip(lower=0)
    down = -1 * close_delta.clip(upper=0)

    if ema == True:
        # Использование экспоненциальной скользящей средней
        ma_up = up.ewm(com=period - 1, adjust=True, min_periods=period).mean()
        ma_down = down.ewm(com=period - 1, adjust=True, min_periods=period).mean()
    else:
        # Использование простой скользящей средней
        ma_up = up.rolling(window=period).mean()
        ma_down = down.rolling(window=period).mean()

    rs = ma_up / ma_down
    rsi = 100 - (100 / (1 + rs))
    return rsi


def add_moving_average(data, window_size=5):
    """
    Рассчитывает и добавляет в таблицу данные по акции для последующей их визуализации:
        скользящая средняя, индикаторы RSI SMA и RSI EMA, индикаторы MACD (стандартная и сигнальная),
        стандарт отклонения выборки.
    Возвращает таблицу с новыми данными.
    :param data:
    :param window_size: стандартное значение для расчета скользящей средней
    :return: таблица data
    """
    # Расчет скользящей средней
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()

    # RSI
    data['RSI_ema'] = calculate_and_display_average_price_rsi(data=data, ema=True)
    data['RSI_sma'] = calculate_and_display_average_price_rsi(data=data, ema=False)

    # MCAD
    ema_fast = 12
    ema_slow = 26
    sma_signal = 9
    # Для вычисления экспоненциально взвешенной скользящей средней (EMA) за определенное количество предыдущих периодов используем функцию pandas.DataFrame.ewm()
    # min_periods в методе ewm, чтобы не рассчитывать значения в первых периодах  временного ряда, который основан на неполных данных
    data['Moving_Average_fast'] = data['Close'].ewm(com=ema_fast - 1, adjust=True, min_periods=ema_fast).mean()
    data['Moving_Average_slow'] = data['Close'].ewm(com=ema_slow - 1, adjust=True, min_periods=ema_slow).mean()
    data['MCAD_main'] = data['Moving_Average_fast'] - data['Moving_Average_slow']
    data['MCAD_signal'] = data['MCAD_main'].rolling(window=sma_signal).mean()

    # Расчет стандарта отклонения выборки по списку (calculate standard deviation of list)
    data['Standart_deviation_list'] = data['Close'].rolling(window=window_size).std()

    # Расчет для модуля practic_task_one_v2.py
    all_period = len(data)
    data['Average_period'] = data['Close'].sum() / all_period
    return data


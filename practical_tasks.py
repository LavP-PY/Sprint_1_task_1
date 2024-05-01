import pandas as pd


def calculate_and_display_average_price(data):
    """
    Функция рассчитывает среднюю цену закрытия акций за заданный период
    :param data:
    :return:
    """
    all_period = len(data)
    average_period = round(data['Close'].sum() / all_period, 2)
    return average_period


def notify_if_strong_fluctuations(data, threshold):
    """
    Функция рассчитывает и уведомляет о максимальных колебаниях за заданный период
    :param data:
    :param threshold:
    :return:
    """
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

# Экспорт данных в csv-файл
def export_data_to_csv(ticker, period, data_average, filename=None):
    """
    Функция сохраняет загруженные данные (среднюю цену закрытия акций за заданный период) об акциях в CSV файл
    :param ticker:
    :param period:
    :param data_average:
    :param filename:
    :return:
    """
    average_round = round(float(data_average), 2)
    data = {'Name': [ticker], 'Selected period': [period], 'Average value': [average_round]}
    frame = pd.DataFrame(data)
    if filename is None:
        filename = f"Average_value_{ticker}_for_{period}"
    frame.to_csv(f'{filename}.csv', index=False)
    return filename

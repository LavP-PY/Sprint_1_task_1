import data_download as dd
import data_plotting as dplt
import practical_tasks as prt
from datetime import datetime

def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print(
        "Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print(
        "Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):")
    date = input("Вы хотите указать общий период или точные даты? Введите '0'-общий или '1'-точные даты:")
    magic_words = ['0', '1']
    while date not in magic_words:
        date = input("ОШИБКА! Введите '0' или '1':")

    if date == '0':
        period = input("Введите период для данных (например, '1mo' для одного месяца): ")
    elif date == '1':
        start_period = input("Введите дату начала периода анализа (формат ввода - ГГ-ММ-ДД):")
        end_period = input("Введите дату окончания периода анализа (формат ввода - ГГ-ММ-ДД):")
        period = str((datetime.strptime(end_period, '%Y-%m-%d') - datetime.strptime(start_period, '%Y-%m-%d')).days) + 'd'

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
    if num_style == '0':
        print(style.items())
        num_style = input("ВВедите номер соответствующего стиля от 1 до 28: ")
    try:
        if 1 <= int(num_style) <= 28:
            choice_style = style.get(num_style)
            print(f'Вы выбрали - {choice_style} стиль', type(choice_style))
    except Exception:
        print('Стиль не был выбран, применён стандартный стиль')
        choice_style = None


    threshold = float(input("Введите максимальное допустимое значение колебания цены, % (например, 1.5 - для 1.5%; Если не требуется, то введите - 0): "))
    filename_csv = input("Введите название csv файла, для сохранения среднего значения (если вы не хотите выводить данные в таблицу, введите - 0; если название не принципиально введите - 1): ")

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)


    # calculation data's average
    average = prt.calculate_and_display_average_price(stock_data)
    print(f'The average value for the selected period (Среднее значение за выбранный период): {average}')

    # notify about strong fluctuations
    if threshold == 0:
        pass
    elif threshold > 0:
        prt.notify_if_strong_fluctuations(stock_data, threshold)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period, choice_style)

    # writing data to csv
    try:
        if int(filename_csv) == 1:
            prt.export_data_to_csv(data_average=average, ticker=ticker, period=period)
        elif int(filename_csv) != 0:
            prt.export_data_to_csv(data_average=average, ticker=ticker, period=period, filename=filename_csv)
    except Exception:
        prt.export_data_to_csv(data_average=average, ticker=ticker, period=period, filename=filename_csv)


if __name__ == "__main__":
    main()

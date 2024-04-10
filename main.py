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
    date = input("Вы хотите указать общий период или точные даты? Введите 'общий' или 'точно':")
    magic_words = ['общий', 'точно']
    while date not in magic_words:
        date = input("ОШИБКА! Введите 'общий' или 'точно':")

    if date == 'общий':
        period = input("Введите период для данных (например, '1mo' для одного месяца): ")
    elif date == 'точно':
        start_period = input("Введите дату начала периода анализа (формат ввода - ГГ-ММ-ДД):")
        end_period = input("Введите дату окончания периода анализа (формат ввода - ГГ-ММ-ДД):")
        period = str((datetime.strptime(end_period, '%Y-%m-%d') - datetime.strptime(start_period, '%Y-%m-%d')).days) + 'd'


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
    dplt.create_and_save_plot(stock_data, ticker, period)

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

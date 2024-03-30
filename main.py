import data_download as dd
import data_plotting as dplt
import practical_tasks



def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")
    threshold = float(input("Введите максимальное допустимое значение колебания цены, % (например, 1.5 - для 1.5%; Если не требуется, то введите - 0): "))

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

    # calculation data's average
    average = practical_tasks.calculate_and_display_average_price(stock_data)
    print(f'The average value for the selected period (Среднее значение за выбранный период): {average}')

    # notify about strong fluctuations
    if threshold == 0:
        pass
    elif threshold > 0:
        practical_tasks.notify_if_strong_fluctuations(stock_data, threshold)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period)



if __name__ == "__main__":
    main()

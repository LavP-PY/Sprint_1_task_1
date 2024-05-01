import csv


def test_data(filename_csv):
    """
    Проверяет на верность записанных данных в файл csv
    :param filename_csv:
    :return:
    """
    with open(f'{filename_csv}.csv', 'r', newline='') as ds:
        reader = csv.DictReader(ds, delimiter=',')
        values_average = []
        for row in reader:
            values = row['Average value']
            values_average.append(values)
        for i in values_average:
            check_average = float(i)
    return check_average


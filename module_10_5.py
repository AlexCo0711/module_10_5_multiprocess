# Домашнее задание по теме "Многопроцессное программирование"
# импорт необходимых библиотек
import multiprocessing
from datetime import datetime

# объявление функции чтения файлов
def read_info(name):
    # создание локального списка
    all_data = []
    # открытие файла на чтение
    with open(name, 'r') as f:
        # цикл считывания файла построчно
        while True:
            # считывание строки
            stroka = f.readline()
            # добавление считанной строки в конец списка
            all_data.append(stroka)
            # прерываем цикл, если строка пустая
            if not stroka:
                break


if __name__ == '__main__':
    # Линейный вызов
    # переменная списка файлов
    files = [f'./file {number}.txt' for number in range(1, 5)]
    # фиксация времени начала линейной обработки
    st1 = datetime.now()
    # цикл чтения списка файлов
    for f in files:
        # обращение к функции read_info для обработки файла f из files
        read = read_info(f)
    print(f'линейного вызов: {datetime.now() - st1}')

    # Многопроцессный
    # создание мультипроцессорного режима обработки
    # фиксация времени начала мультипроцессорной обработки
    st2 = datetime.now()
    # обращение к мультипроцессорному методу
    with multiprocessing.Pool(processes=4) as pool:
        # передача данных в мультипроцессорный метод
        pool.map(read_info, files)

    print(f'мультипроцесс: {datetime.now() - st2}')

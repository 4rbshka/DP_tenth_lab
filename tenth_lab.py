import numpy as np
import math
import statistics
import matplotlib.pyplot as plt


def bar_graph(corrs, m):  # функция построения гистограммы
    plt.bar(np.arange(m), corrs)
    plt.ylabel('y')  # Название оси y
    plt.xlabel('x')  # Название оси x
    plt.title('Гистограмма коэффициентов корреляции')  # Название графика
    plt.show()


def scatter_graph(x, y, x1, y1, y2, y3):  # функция построения точечной диаграммы
    plt.scatter(x, y)
    plt.scatter(x1, y1)
    plt.scatter(x1, y2)
    plt.scatter(x1, y3)
    plt.ylabel('y')  # Название оси y
    plt.xlabel('x')  # Название оси x
    plt.title('График зависимости Y от X')  # Название графика
    plt.show()


# 1. Стадия выбора
choice = input("Для работы с конкретными данными введите 1. В ином случае будет работа со случайными данными...\n")
if choice == '1':
    x_column = np.fromfile('10_x_data.txt', float, sep=" ")
else:
    x_column = np.random.random(60)
    x_column = np.sort(x_column)

# 2. Стадия создания матрицы с временным лагом
n = 15  # Количество столбцов матрицы y
length = len(x_column)
y_column = np.zeros(length)
for i in range(length):
    y_column[i] = 0.8 * math.cos(x_column[i] * 10) + 0.6 * math.sin(x_column[i] * 10)
y_matrix = np.zeros((n, length - (n - 1)))
for i in range(n):
    y_matrix[i] = y_column[n - 1 - i:length - i].copy()

# 3. Стадия нахождения коэффициентов корреляции
correlations = np.zeros(n)
quarter_period = 0
for i in range(n):
    correlations[i] = statistics.correlation(y_matrix[0], y_matrix[i])
    if correlations[i] > 0:
        quarter_period += 1

# 4. Стадия создания гистограммы
bar_graph(correlations, n)

# 5. Стадия создания моделей
dt = x_column[-1]/length
L1 = dt * quarter_period * 4
L2 = dt * (quarter_period - 1) * 4
L3 = dt * (quarter_period + 1) * 4

x1_column = np.zeros(length)
y_calc_1_column = np.zeros(length)
y_calc_2_column = np.zeros(length)
y_calc_3_column = np.zeros(length)
for i in range(length):
    x1_column[i] += i * dt
    y_calc_1_column[i] = math.cos(2*math.pi*x_column[i]/L1)
    y_calc_2_column[i] = math.cos(2 * math.pi * x_column[i] / L2)
    y_calc_3_column[i] = math.cos(2 * math.pi * x_column[i] / L3)

# 6. Стадия построения точечной диаграммы
scatter_graph(x_column, y_column, x1_column, y_calc_1_column, y_calc_2_column, y_calc_3_column)

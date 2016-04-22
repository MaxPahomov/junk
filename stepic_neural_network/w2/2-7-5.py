# Задача для самопроверки (то есть за неё не даются баллы).

# Реализуйте метод update_mini_batch класса Neuron. Когда вы решите сдать задачу, вам нужно будет просто скопировать соответствующие функции (которые вы написали в ноутбуке ) сюда. Копируем без учёта отступов; шаблон в поле ввода ответа уже будет, ориентируйтесь по нему. Сигнатура функции указана в ноутбуке, она остаётся неизменной.

# update_mini_batch считает градиент и обновляет веса нейрона на основе всей переданной ему порции данных, кроме того, возвращает 1, если алгоритм сошелся (абсолютное значение изменения целевой функции до и после обновления весов < eps), иначе возвращает 0.

# Мы будем проверять ваш алгоритм на данных разного размера. Пример данных, на которых вы можете проверить работу своего решения самостоятельно:

# np.random.seed(42)
# n = 10
# m = 5

# X = 20 * np.random.sample((n, m)) - 10
# y = (np.random.random(n) < 0.5).astype(np.int)[:, np.newaxis]
# w = 2 * np.random.random((m, 1)) - 1

# neuron = Neuron(w)
# neuron.update_mini_batch(X, y, 0.1, 1e-5)

# Если вы посмотрите на веса нейрона neuron после выполнения этого кода, то они должны быть такими:

# >>> print(neuron.w)
# [[-0.22571548]
#  [-0.45367083]
#  [ 0.65670199]
#  [-0.27851325]
#  [-0.41341191]]

import numpy as np

def update_mini_batch(self, X, y, learning_rate, eps):
    before = J_quadratic(self, X, y)
    grad = compute_grad_analytically(self, X, y)
    dw = -grad * learning_rate
    self.w += dw
    after = J_quadratic(self, X, y)
    return 1 if abs(after - before) < eps else 0
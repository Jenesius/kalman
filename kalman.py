import numpy as np


class KalmanFilter:
    def __init__(self, initial_offset, dt=1.0, q_delay=0.1, q_drift=0.01, r=0.2):
        # Инициализация параметров фильтра
        self.dt = dt  # Интервал времени между измерениями

        # Матрица состояния: [delay, drift]
        self.x = np.array([initial_offset, 0.0])

        # Ковариационная матрица состояния
        self.P = np.eye(2) * 1000  # Начальная неопределенность

        # Матрица перехода состояния
        self.F = np.array([[1, self.dt],
                           [0, 1]])

        # Матрица ковариации процесса
        self.Q = np.array([[q_delay, 0],
                           [0, q_drift]])

        # Матрица измерений
        self.H = np.array([[1, 0]])

        # Ковариация измерений
        self.R = np.array([[r]])

    def predict(self):
        # Прогноз состояния
        self.x = self.F @ self.x
        self.P = self.F @ self.P @ self.F.T + self.Q

    def update(self, measurement):
        # Обновление на основе измерения
        y = measurement - self.H @ self.x
        S = self.H @ self.P @ self.H.T + self.R
        K = self.P @ self.H.T @ np.linalg.inv(S)
        self.x = self.x + K @ y
        self.P = (np.eye(2) - K @ self.H) @ self.P

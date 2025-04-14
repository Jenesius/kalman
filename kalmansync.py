import numpy as np

class KalmanTimeSync:
    def __init__(self, p):
        # Инициализация состояния
        self.x = np.array([0.0, 0.0])  # [θ, ω]
        self.P = np.diag(p)  # Начальная ковариация
        self.last_update_time = None  # Время предыдущего измерения

        # Параметры шумов (интенсивности в непрерывном времени)
        self.q_theta = 1e-2  # [с/√с]
        self.q_omega = 1e-24  # [1/√с]

        # Матрица наблюдений H = [1, 0] (не зависит от Δt)
        self.H = np.array([[1, 0]])

    def update(self, z, current_time, delay):


        # Расчет Δt (для первого вызова Δt = 0)
        if self.last_update_time is None:
            dt = 0.0
        else:
            dt = current_time - self.last_update_time

        # Динамическое обновление матриц F и Q
        F = np.array([[1, dt],
                      [0, 1]])
        Q = np.diag([
            (self.q_theta ** 2) * dt,  # Дисперсия шума θ
            (self.q_omega ** 2) * dt  # Дисперсия шума ω
        ])

        # Прогноз (только если Δt > 0)
        if dt > 0:
            self.x = F @ self.x
            self.P = F @ self.P @ F.T + Q

        # Коррекция
        R = (delay / 2) ** 2 + 0.01 ** 2  # Дисперсия измерения
        y = z - self.H @ self.x  # Инновация
        S = self.H @ self.P @ self.H.T + R
        K = self.P @ self.H.T / S  # Калмановский коэффициент

        self.x += K.flatten() * y
        self.P = (np.eye(2) - K @ self.H) @ self.P

        # Обновление времени последнего измерения
        self.last_update_time = current_time

        return self.x[0]
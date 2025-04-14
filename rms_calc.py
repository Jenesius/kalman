import numpy as np
class RMSCalc:
    @staticmethod
    def calc(data):
        window_size = 3  # Размер окна
        rms_rolling = [
            np.sqrt(np.mean(np.square(data[i:i + window_size])))
            for i in range(len(data) - window_size + 1)
        ]

        return rms_rolling
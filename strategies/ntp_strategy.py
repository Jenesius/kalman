import ntplib
import time
from datetime import datetime

class NTPStrategy:
    def __init__(self, ntp_server, duration, interval):
        self.ntp_server = ntp_server
        self.duration = duration
        self.interval = interval

    def collect(self):
        """Сбор данных NTP-смещения"""
        client = ntplib.NTPClient()
        timestamps = []
        offsets = []
        delays = []

        start_time = time.time()
        end_time = start_time + self.duration

        print(f"Сбор данных в течение {self.duration} секунд...")

        while time.time() < end_time:
            try:
                response = client.request(self.ntp_server)
                print("original time:", response.orig_time)
                print("destinat time:", response.dest_time)
                print("destinat time:", time.time())
                print("offset:", response.offset)
                print("delay", response.delay, response.dest_time - response.orig_time,
                      time.time() - response.dest_time)

                current_time = time.time()
                offset_ms = response.offset * 1000  # Конвертация в миллисекунды
                delay_ms = response.delay * 1000

                timestamps.append(datetime.now())
                offsets.append(offset_ms)
                delays.append(delay_ms)

                print(f"{ datetime.fromtimestamp(current_time / 1e3).strftime('%H:%M:%S')} "
                      f"Offset: {offset_ms:+.3f} ms Delay: {delay_ms:+.3f} ms")

            except Exception as e:
                print(f"Ошибка: {str(e)}")
                timestamps.append(datetime.now())
                offsets.append(None)

            time.sleep(self.interval)

        return timestamps, offsets, delays
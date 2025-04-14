import matplotlib.pyplot as plt
import matplotlib.dates as mdates

class Canvas:

    def __init__(self, show_offsets = True, show_rms = True, show_kalman = True, interval = None):
        self.show_offsets = show_offsets
        self.show_rms = show_rms
        self.show_kalman = show_kalman
        self.interval = interval


    def plot_ntp_data(self, ax, timestamps, offsets):
        """Построение графика NTP-смещения"""

        ax.plot(timestamps, offsets,
                 linestyle='-',
                 color='#4A90E2',
                 label='Сырой offset'
                 )

    def plot_kalman(self, ax, timestamps, kalman_offsets):
        ax.plot(timestamps[0:], kalman_offsets,
                 linewidth=2,
                 linestyle='-',
                 color='#FF6B6B',
                 label='Фильтр Калмана'
                 )
    def plot_rms(self, ax, timestamps, rms_offsets):
        ax.plot(timestamps[2:], rms_offsets,
                linewidth=1,
                linestyle='-',
                color='#242424',
                label='Скользящее среднее'
                )

    def plot_ntp_delay(self, ax, timestamps, delays):
        ax.plot(timestamps, delays,
                 linewidth=1,
                 linestyle='-',
                 color='royalblue',
                 )

    def plot_kalman_delay(self, ax, timestamps, delays):
        ax.plot(timestamps, delays,
                 linewidth=1,
                 linestyle='-',
                 color='red',
                 )


    def plot(self, timestamps, offsets, delays, kalman_offsets, kalman_delays, rms_offsets):
        fig_offset = plt.figure(figsize=(16, 8))
        ax_offset = fig_offset.add_subplot(1, 1, 1)
        ax_offset.set_xlabel('Time')
        ax_offset.set_ylabel('Clock Offset (ms)')
        ax_offset.grid(True, alpha=0.3)

        #fig_delay = plt.figure(figsize=(16, 8))
        #ax_delay = fig_delay.add_subplot(1, 1, 1)
        #ax_delay.set_xlabel('Time')
        #ax_delay.set_ylabel('Delay (ms)')
        #ax_delay.grid(True, alpha=0.3)


        # Форматирование временной оси
        ax = plt.gca()
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        plt.gcf().autofmt_xdate()

        plt.tight_layout()


        if self.show_offsets:
            self.plot_ntp_data(ax_offset, timestamps, offsets)

        if self.show_rms:
            self.plot_rms(ax_offset, timestamps, rms_offsets)

        if self.show_kalman:
            self.plot_kalman(ax_offset, timestamps, kalman_offsets)
        ax_offset.legend (loc = 'upper right')

        self.try_display_interval(timestamps)

        #self.plot_ntp_delay(ax_delay, timestamps, delays)
        #self.plot_kalman_delay(ax_delay, timestamps, kalman_delays)

    def try_display_interval(self, timestamps):
        if self.interval is None: return;
        plt.axvline(timestamps[self.interval[0]], color='#08080825', linestyle='--')
        plt.axvline(timestamps[self.interval[1]], color='#08080825', linestyle='--')

    def show(self):
        plt.show()



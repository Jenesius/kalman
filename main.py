from kalmansync import KalmanTimeSync
from data_validator import DataValidator
from strategies.ntp_strategy import NTPStrategy
from strategies.local_strategy import LocalStrategy
from local_data_loader import LocalDataLoader
from rms_calc import RMSCalc
from canvas import Canvas
from report_builder import ReportBuilder

def collect_kalman(timestamps, offsets, delays):
    filter = KalmanTimeSync(
        p = [0.1, 1e-12]
    )

    kalman_offsets = []
    kalman_delays = []
    for index, item in enumerate(offsets):
        offset = filter.update(z=offsets[index], current_time=timestamps[index].microsecond, delay=delays[index])
        kalman_delays.append(filter.x[1])
        kalman_offsets.append(offset)


    return kalman_offsets, kalman_delays

def getFileName(name):
    return "./storage/{:s}.json".format(name)

if __name__ == "__main__":

    files = [
        "ntp_5400",
        "ptp_small"
    ]

    useLocal = True
    saveKalmanToCopyFile = True

    file = files[0]

    filename = getFileName(file)
    kalmanFileName = getFileName("kalman_" + file)

    ntps = [
        "time.windows.com",
        "3.by.pool.ntp.org"
    ]

    duration = 60 * 60 * 5
    interval = 4

    strategy = NTPStrategy(ntps[0], duration, interval) if not useLocal else LocalStrategy(filename)
    timestamps, offsets, delays = strategy.collect()

    valid_timestamps, valid_offsets, valid_delays = DataValidator.apply(timestamps, offsets, delays)

    rms_offsets = RMSCalc.calc(valid_offsets)
    kalman_offsets, kalman_delays = collect_kalman(valid_timestamps, valid_offsets, valid_delays)

    if saveKalmanToCopyFile:
        LocalDataLoader.save(kalmanFileName, valid_timestamps, kalman_offsets, kalman_delays)

    if not useLocal:
        LocalDataLoader.save(filename,  valid_timestamps, valid_offsets, valid_delays)


    builder = ReportBuilder(valid_timestamps, valid_offsets, kalman_offsets)
    builder.print_report(55)

    canvas = Canvas(interval = [50, -1], show_offsets=True, show_rms=False, show_kalman=True)
    canvas.plot(valid_timestamps, valid_offsets, valid_delays, kalman_offsets, kalman_delays, rms_offsets)
    canvas.show()



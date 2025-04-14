class DataValidator:
    @staticmethod
    def apply(timestamps, offsets, delays):
        valid_data = [(t, o, d) for t, o, d in zip(timestamps, offsets, delays) if o is not None]
        valid_ts, valid_offsets, valid_delays = zip(*valid_data) if valid_data else ([], [], [])

        return valid_ts, valid_offsets, valid_delays
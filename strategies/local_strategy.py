import json
from datetime import datetime

class LocalStrategy:
    def __init__(self, filename):
        self.filename = filename


    def convert_date(self, date_string):
        date_format = "%Y-%m-%d %H:%M:%S.%f"
        result = datetime.strptime(date_string, date_format)

        return result

    def collect(self):
        with open(self.filename, 'r') as f:
            data = json.load(f)
            timestamps = map(self.convert_date, data['timestamps'])
            offsets = data['offsets']
            delays = data['delays']

            return timestamps, offsets, delays
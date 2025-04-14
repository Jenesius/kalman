import json

class LocalDataLoader:

    @staticmethod
    def save(filename, timestamps, offsets, delays):

        f = open(filename, "w+")
        content = json.dumps({
            "timestamps": timestamps,
            "offsets": offsets,
            "delays": delays
        }, indent=4, sort_keys=True, default=str)
        f.write(content)
        f.close()
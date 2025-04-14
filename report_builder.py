class ReportBuilder:
    def __init__(self, timestamps, offsets,kalman_offsets):
        self.timestamps = timestamps
        self.offsets = offsets
        self.kalman_offsets = kalman_offsets

    def print_minmax_offsets(self, arr, start_with):
        min_value = min(arr[start_with:])
        max_value = max(arr[start_with:])

        print("Min raw offset {:f}, Max offset {:f}, diff {:f}".format(min_value, max_value, max_value - min_value))

    def print_report(self, start_with = 0):
        print("--- Report ---")

        self.print_minmax_offsets(self.offsets, start_with)
        self.print_minmax_offsets(self.kalman_offsets,start_with )

        print("--- ---")

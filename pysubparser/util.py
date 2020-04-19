from datetime import time


def time_to_millis(t: time) -> int:
    seconds = (t.hour * 60 + t.minute) * 60 + t.second
    return seconds * 1000 + t.microsecond//1000

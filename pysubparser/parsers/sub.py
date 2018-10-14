from datetime import time
from itertools import count

from pysubparser.classes.classes import Subtitle
from pysubparser.classes.exceptions import InvalidTimestampError


def int_to_time(value, fps):
    try:
        value = int(value) / float(fps)

        m, s = divmod(value, 60)
        h, m = divmod(m, 60)
        ms = (s - int(s)) * 1000000

        return time(hour=int(h), minute=int(m), second=int(s), microsecond=int(ms))
    except:
        raise InvalidTimestampError(value, '{int}', 'sub')


def parse(path, encoding='utf-8', **kwargs):
    fps = kwargs.get('fps', 23.976)

    index = count(0)
    with open(path, encoding=encoding) as file:

        for line in file:
            line = line.rstrip()

            start, end = line.replace('{', '').split('}')[:2]
            text = [t.split('}')[-1] for t in line.split('|')]

            start = int_to_time(start, fps)
            end = int_to_time(end, fps)

            yield Subtitle(next(index), start, end, text)

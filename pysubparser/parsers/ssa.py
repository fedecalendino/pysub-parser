from datetime import datetime
from itertools import count

from pysubparser.classes.classes import Subtitle
from pysubparser.classes.exceptions import InvalidTimestampError


TIMESTAMP_FORMAT = '%H:%M:%S.%f'


def parse_timestamps(timestamp):
    try:
        return datetime.strptime(timestamp + '0', TIMESTAMP_FORMAT).time()
    except:
        raise InvalidTimestampError(timestamp, TIMESTAMP_FORMAT, 'ssa/ass')


def parse(path, encoding='utf-8', **kwargs):
    index = count(0)

    with open(path, encoding=encoding) as file:
        for line in file:
            line = line.strip()

            if not line.startswith('Dialogue'):
                continue

            split = line.split(',')

            start = parse_timestamps(split[1])
            end = parse_timestamps(split[2])

            text_lines = ','.join(split[9:]).replace('  ', ' ').replace('\\N', '\\n').split('\\n')
            yield Subtitle(next(index), start, end, text_lines)

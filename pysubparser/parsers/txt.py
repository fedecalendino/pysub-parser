from datetime import datetime
from datetime import time
from typing import Iterator, Tuple
from itertools import count

from pysubparser.classes.classes import Subtitle
from pysubparser.classes.exceptions import InvalidTimestampError


TIMESTAMP_SEPARATOR = ','
TIMESTAMP_FORMAT = '%H:%M:%S.%f'


def parse_timestamps(line: str) -> Tuple[time, time]:
    try:
        start, end = line.split(TIMESTAMP_SEPARATOR)

        start = datetime.strptime(start + '0', TIMESTAMP_FORMAT).time()
        end = datetime.strptime(end + '0', TIMESTAMP_FORMAT).time()

        return start, end
    except:
        raise InvalidTimestampError(line, TIMESTAMP_FORMAT, 'txt')


def parse(
        path: str,
        encoding: str = "utf-8",
        **_
) -> Iterator[Subtitle]:
    index = count(0)

    with open(path, encoding=encoding) as file:
        line = '['

        while 'SUBTITLE' not in line:
            line = next(file)

        next(file)  # Skipping '[COLF]'

        for line in file:
            line = line.strip()
            start, end = parse_timestamps(line)
            lines = next(file).strip().split('[br]')

            yield Subtitle(next(index), start, end, lines)

            next(file).strip()

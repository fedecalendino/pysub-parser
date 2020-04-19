from datetime import datetime, time
from itertools import count
from typing import Iterator, Tuple

from pysubparser.classes.exceptions import InvalidTimestampError
from pysubparser.classes.subtitle import Subtitle

TIMESTAMP_SEPARATOR = ','
TIMESTAMP_FORMAT = '%H:%M:%S.%f'


def parse_timestamps(line: str) -> Tuple[time, time]:
    try:
        start, end = line.split(TIMESTAMP_SEPARATOR)

        start = datetime.strptime(start + '0', TIMESTAMP_FORMAT).time()
        end = datetime.strptime(end + '0', TIMESTAMP_FORMAT).time()

        return start, end
    except ValueError:
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

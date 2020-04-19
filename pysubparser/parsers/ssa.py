from datetime import datetime, time
from itertools import count
from typing import Iterator

from pysubparser.classes.exceptions import InvalidTimestampError
from pysubparser.classes.subtitle import Subtitle

TIMESTAMP_FORMAT = '%H:%M:%S.%f'


def parse_timestamps(timestamp: str) -> time:
    try:
        return datetime.strptime(timestamp + '0', TIMESTAMP_FORMAT).time()
    except ValueError:
        raise InvalidTimestampError(
            timestamp=timestamp,
            expected_format=TIMESTAMP_FORMAT,
            subtitle_type='ssa/ass'
        )


def parse(
        path: str,
        encoding: str = "utf-8",
        **_
) -> Iterator[Subtitle]:
    index = count(0)

    with open(path, encoding=encoding) as file:
        for line in file:
            line = line.strip()

            if not line.startswith('Dialogue'):
                continue

            split = line.split(',')

            start = parse_timestamps(split[1])
            end = parse_timestamps(split[2])

            lines = ','.join(split[9:]).replace('  ', ' ').replace('\\N', '\\n').split('\\n')
            yield Subtitle(next(index), start, end, lines)

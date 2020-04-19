from datetime import datetime, time
from itertools import count
from typing import Iterator, Tuple

from pysubparser.classes.exceptions import InvalidTimestampError
from pysubparser.classes.subtitle import Subtitle

TIMESTAMP_SEPARATOR = ' --> '
TIMESTAMP_FORMAT = '%H:%M:%S,%f'


def parse_timestamps(line: str) -> Tuple[time, time]:
    try:
        start, end = line.split(TIMESTAMP_SEPARATOR)

        start = datetime.strptime(start, TIMESTAMP_FORMAT).time()
        end = datetime.strptime(end, TIMESTAMP_FORMAT).time()

        return start, end
    except ValueError:
        raise InvalidTimestampError(line, TIMESTAMP_FORMAT, 'srt')


def parse(
        path: str,
        encoding: str = "utf-8",
        **_
) -> Iterator[Subtitle]:
    index = count(0)

    with open(path, encoding=encoding) as file:
        subtitle = None

        for line in file:
            line = line.rstrip()

            if not subtitle:
                if TIMESTAMP_SEPARATOR in line:
                    start, end = parse_timestamps(line)

                    subtitle = Subtitle(next(index), start, end)
            else:
                if line:
                    subtitle.add_line(line)
                else:
                    yield subtitle
                    subtitle = None


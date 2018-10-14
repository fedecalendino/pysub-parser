from datetime import datetime
from itertools import count

from pysubparser.classes.classes import Subtitle
from pysubparser.classes.exceptions import InvalidTimestampError

TIMESTAMP_SEPARATOR = ' --> '
TIMESTAMP_FORMAT = '%H:%M:%S,%f'


def parse_timestamps(line):
    try:
        start, end = line.split(TIMESTAMP_SEPARATOR)

        start = datetime.strptime(start, TIMESTAMP_FORMAT).time()
        end = datetime.strptime(end, TIMESTAMP_FORMAT).time()

        return start, end
    except:
        raise InvalidTimestampError(line, TIMESTAMP_FORMAT, 'srt')


def parse(path, encoding='utf-8', **kwargs):
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
                    subtitle.add_text_line(line)
                else:
                    yield subtitle
                    subtitle = None


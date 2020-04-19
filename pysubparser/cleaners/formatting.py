import re
from typing import Iterable, Iterator

from pysubparser.classes.subtitle import Subtitle

FORMAT_OPEN_CLEANER = re.compile(r'<[^[]*>', re.UNICODE)
FORMAT_CLOSE_CLEANER = re.compile(r'</[^[]*>', re.UNICODE)


def clean(subtitles: Iterable[Subtitle]) -> Iterator[Subtitle]:
    for subtitle in subtitles:
        subtitle.lines = list(map(
            lambda line: FORMAT_CLOSE_CLEANER.sub('', line).strip(),
            subtitle.lines
        ))

        subtitle.lines = list(map(
            lambda line: FORMAT_OPEN_CLEANER.sub('', line).strip(),
            subtitle.lines
        ))

        yield subtitle

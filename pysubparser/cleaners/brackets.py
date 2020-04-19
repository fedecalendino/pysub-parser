import re
from typing import Iterable, Iterator

from pysubparser.classes.subtitle import Subtitle

BRACKETS_CLEANER = re.compile(r'\[[^[]*\]', re.UNICODE)


def clean(subtitles: Iterable[Subtitle]) -> Iterator[Subtitle]:
    for subtitle in subtitles:
        subtitle.lines = list(map(
            lambda line: BRACKETS_CLEANER.sub('', line).strip(),
            subtitle.lines
        ))

        yield subtitle

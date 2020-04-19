import re
from typing import Iterable, Iterator

from pysubparser.classes.subtitle import Subtitle

BRACKETS_CLEANER = re.compile(r'\[[^[]*\]', re.UNICODE)


def clean(subtitles: Iterable[Subtitle]) -> Iterator[Subtitle]:
    for subtitle in subtitles:
        text = BRACKETS_CLEANER.sub('', subtitle.text)

        subtitle.text = text.strip()

        yield subtitle

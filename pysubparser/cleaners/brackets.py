import re
from typing import Iterator, List

from pysubparser.classes.subtitle import Subtitle

BRACKETS_CLEANER = re.compile(r'\[[^[]*\]', re.UNICODE)


def clean(subtitles: List[Subtitle]) -> Iterator[Subtitle]:
    for subtitle in subtitles:
        text = BRACKETS_CLEANER.sub('', subtitle.text)

        subtitle.text = text.strip()

        yield subtitle

import re
from typing import Iterator, List

from pysubparser.classes.subtitle import Subtitle

FORMAT_OPEN_CLEANER = re.compile(r'<[^[]*>', re.UNICODE)
FORMAT_CLOSE_CLEANER = re.compile(r'</[^[]*>', re.UNICODE)


def clean(subtitles: List[Subtitle]) -> Iterator[Subtitle]:
    for subtitle in subtitles:
        text = subtitle.text
        text = FORMAT_CLOSE_CLEANER.sub('', text)
        text = FORMAT_OPEN_CLEANER.sub('', text)

        subtitle.text = text.strip()

        yield subtitle

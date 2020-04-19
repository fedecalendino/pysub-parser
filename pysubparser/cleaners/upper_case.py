from typing import Iterator, List
from pysubparser.classes.subtitle import Subtitle


def clean(subtitles: List[Subtitle]) -> Iterator[Subtitle]:
    for subtitle in subtitles:
        subtitle.text = subtitle.text.upper()

        yield subtitle

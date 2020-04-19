from typing import Iterable, Iterator

from unidecode import unidecode

from pysubparser.classes.subtitle import Subtitle


def clean(subtitles: Iterable[Subtitle]) -> Iterator[Subtitle]:
    for subtitle in subtitles:
        subtitle.lines = list(map(unidecode, subtitle.lines))

        yield subtitle

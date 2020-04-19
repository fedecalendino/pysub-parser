from typing import Iterable, Iterator

from pysubparser.classes.subtitle import Subtitle


def clean(subtitles: Iterable[Subtitle]) -> Iterator[Subtitle]:
    for subtitle in subtitles:
        subtitle.lines = list(map(
            lambda line: line.lower(),
            subtitle.lines
        ))

        yield subtitle

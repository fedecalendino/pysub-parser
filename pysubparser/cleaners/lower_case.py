from typing import Iterable, Iterator

from pysubparser.classes.subtitle import Subtitle


def clean(subtitles: Iterable[Subtitle]) -> Iterator[Subtitle]:
    for subtitle in subtitles:
        subtitle.text = subtitle.text.lower()

        yield subtitle

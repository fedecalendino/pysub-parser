from typing import Iterable, Iterator
import textwrap
from pysubparser.classes.subtitle import Subtitle


def clean(subtitles: Iterable[Subtitle], width: int = 40) -> Iterator[Subtitle]:
    for subtitle in subtitles:
        subtitle.lines = textwrap.wrap(
            subtitle.text,
            width=width,
        )

        yield subtitle

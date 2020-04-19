from typing import Iterable

from pysubparser.classes.exceptions import InvalidSubtitleTypeError
from pysubparser.classes.subtitle import Subtitle
from pysubparser.writers import srt

WRITERS = {
    "srt": srt.write,
}


def write(
        subtitles: Iterable[Subtitle],
        path: str,
        subtitle_type: str = None,
):
    if not subtitle_type:
        subtitle_type = path[path.rfind(".") + 1:]

    writer = WRITERS.get(subtitle_type.lower())

    if not writer:
        raise InvalidSubtitleTypeError(subtitle_type, WRITERS.keys())

    return writer(subtitles, path)

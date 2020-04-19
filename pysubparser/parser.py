from pysubparser.classes.exceptions import InvalidSubtitleTypeError

from pysubparser.parsers import srt
from pysubparser.parsers import ssa
from pysubparser.parsers import sub
from pysubparser.parsers import txt


PARSERS = {
    "ass": ssa.parse,
    "ssa": ssa.parse,
    "srt": srt.parse,
    "sub": sub.parse,
    "txt": txt.parse
}


def parse(
        path: str,
        subtitle_type: str = None,
        encoding: str = "utf-8",
        **kwargs
):
    if not subtitle_type:
        subtitle_type = path[path.rfind(".") + 1:]

    parser = PARSERS.get(subtitle_type.lower())

    if not parser:
        raise InvalidSubtitleTypeError(subtitle_type, PARSERS.keys())

    return parser(path, encoding, **kwargs)

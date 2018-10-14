from pysubparser.classes.exceptions import InvalidSubtitleTypeError

from pysubparser.parsers import srt
from pysubparser.parsers import ssa
from pysubparser.parsers import sub
from pysubparser.parsers import txt

PARSERS = {
    'ass': ssa.parse,
    'ssa': ssa.parse,
    'srt': srt.parse,
    'sub': sub.parse,
    'txt': txt.parse
}


def parse(path, subtype=None, encoding='utf-8', **kwargs):
    if not subtype:
        subtype = path[path.rfind('.') + 1:]

    parser = PARSERS.get(subtype.lower())

    if not parser:
        raise InvalidSubtitleTypeError(subtype, PARSERS.keys())

    return parser(path, encoding, **kwargs)

from typing import Iterable

from pysubparser.classes.subtitle import Subtitle

TIMESTAMP_FORMAT = '%H:%M:%S,%f'


def write(subtitles: Iterable[Subtitle], path: str):
    with open(path, 'w+', encoding='utf-8') as file:
        for subtitle in subtitles:
            timestamp = "{start} --> {end}".format(
                start=subtitle.start.strftime(TIMESTAMP_FORMAT)[:-3],
                end=subtitle.end.strftime(TIMESTAMP_FORMAT)[:-3],
            )

            lines = [str(subtitle.index), timestamp]
            lines.extend(subtitle.lines)
            lines.append("")
            lines.append("")

            file.write("\n".join(lines))

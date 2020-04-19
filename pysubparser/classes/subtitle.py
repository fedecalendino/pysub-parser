from datetime import time
from typing import List

from pysubparser.util import time_to_millis


class Subtitle:
    __SLOTS__ = ["index", "start", "end", "text", "lines"]

    def __init__(
            self,
            index: int,
            start: time = None,
            end: time = None,
            lines: List[str] = None
    ):
        self.index: int = index
        self.start: time = start
        self.end: time = end
        self.lines: List[str] = lines if lines else []

    @property
    def text(self) -> str:
        return ' '.join(self.lines)

    @property
    def duration(self) -> int:
        return time_to_millis(self.end) - time_to_millis(self.start)

    def add_line(self, line: str):
        self.lines.append(line)

    def __repr__(self):
        return f"{self.index} > {self.text}"


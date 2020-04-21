from unittest import TestCase

import ddt

from pysubparser import parser, writer
from pysubparser.cleaners import ascii, brackets, formatting, lower_case

PATH = "./tests/files/{test_type}/test.{subtitle_type}"


@ddt.ddt
class WriterTester(TestCase):

    def _assert_subtitle(self, sub, index, text, start, end, duration):
        self.assertEqual(sub.index, index)
        self.assertEqual(sub.text, text)

        self.assertEqual(sub.start.hour, start[0])
        self.assertEqual(sub.start.minute, start[1])
        self.assertEqual(sub.start.second, start[2])

        self.assertEqual(sub.end.hour, end[0])
        self.assertEqual(sub.end.minute, end[1])
        self.assertEqual(sub.end.second, end[2])

        self.assertEqual(sub.duration, duration)

        self.assertTrue(str(index) in str(sub))
        self.assertTrue(text in str(sub))

    @ddt.data("ass", "ssa", "srt", "sub")
    def test_srt_writer(self, subtitle_type):
        path = PATH.format(test_type="valid", subtitle_type=subtitle_type)
        subtitles = parser.parse(path, subtitle_type=subtitle_type, fps=24)

        subtitles = brackets.clean(
            formatting.clean(
                lower_case.clean(
                    ascii.clean(
                        subtitles
                    )
                )
            )
        )

        new_path = f"{path}.srt"
        writer.write(subtitles, new_path)

        subtitles = parser.parse(new_path, subtitle_type="srt")

        self._assert_subtitle(
            sub=next(subtitles),
            index=0,
            text="subtitle",
            start=(0, 0, 1),
            end=(0, 0, 2),
            duration=1000
        )

        self._assert_subtitle(
            sub=next(subtitles),
            index=1,
            text="- subtitle",
            start=(0, 0, 3),
            end=(0, 0, 3),
            duration=500
        )

        self._assert_subtitle(
            sub=next(subtitles),
            index=2,
            text="subtitle",
            start=(0, 1, 5),
            end=(0, 1, 5),
            duration=250
        )

        self._assert_subtitle(
            sub=next(subtitles),
            index=3,
            text="subtitle",
            start=(1, 30, 0),
            end=(1, 35, 0),
            duration=300000
        )

        self._assert_subtitle(
            sub=next(subtitles),
            index=4,
            text="multi line subtitle",
            start=(2, 0, 0),
            end=(2, 11, 11),
            duration=671000
        )

        self._assert_subtitle(
            sub=next(subtitles),
            index=5,
            text="subtitle",
            start=(2, 20, 0),
            end=(3, 0, 0),
            duration=2400000
        )

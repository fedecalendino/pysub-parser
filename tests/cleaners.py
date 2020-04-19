from unittest import TestCase

from pysubparser.parser import parse
from pysubparser.cleaners import lower_case, upper_case


class CleanersTester(TestCase):

    def setUp(self) -> None:
        self.subtitles = parse("./tests/files/valid/test.srt")

    def test_lower_case_cleaner(self):
        expected = [
            "subtitle",
            "- subtitle",
            "[sound effect] subtitle",
            "<format>subtitle</format>",
            "multi line subtitle",
            "subtitle",
        ]

        clean_subtitles = lower_case.clean(self.subtitles)

        for subtitle, text in zip(clean_subtitles, expected):
            self.assertEqual(subtitle.text, text)

    def test_upper_case_cleaner(self):
        expected = [
            "SUBTITLE",
            "- SUBTITLE",
            "[SOUND EFFECT] SUBTITLE",
            "<FORMAT>SUBTITLE</FORMAT>",
            "MULTI LINE SUBTITLE",
            "SUBTITLE",
        ]

        clean_subtitles = upper_case.clean(self.subtitles)

        for subtitle, text in zip(clean_subtitles, expected):
            self.assertEqual(subtitle.text, text)

from unittest import TestCase

from pysubparser.cleaners import ascii, brackets, formatting, lower_case
from pysubparser.parser import parse


class CleanersTester(TestCase):

    def setUp(self) -> None:
        self.subtitles = parse("./tests/files/valid/cleaners.srt")

    def _assert_subtitles(self, subtitles, expected):
        for subtitle, text in zip(subtitles, expected):
            self.assertEqual(subtitle.text, text)

    def test_no_cleaner(self):
        expected = [
            "Subtitle",
            "- Subtitle",
            "[Sound effect] Subtitle",
            "<format>Subtitle</format>",
            "Multi line Subtitle",
            "Sübtîtlé",
        ]

        self._assert_subtitles(self.subtitles, expected)

    def test_ascii_cleaner(self):
        expected = [
            "Subtitle",
            "- Subtitle",
            "[Sound effect] Subtitle",
            "<format>Subtitle</format>",
            "Multi line Subtitle",
            "subtitle",
        ]

        clean_subtitles = ascii.clean(self.subtitles)
        self._assert_subtitles(clean_subtitles, expected)

    def test_lower_case_cleaner(self):
        expected = [
            "subtitle",
            "- subtitle",
            "[sound effect] subtitle",
            "<format>subtitle</format>",
            "multi line subtitle",
            "sübtîtlé",
        ]

        clean_subtitles = lower_case.clean(self.subtitles)
        self._assert_subtitles(clean_subtitles, expected)

    def test_formatting_cleaner(self):
        expected = [
            "Subtitle",
            "- Subtitle",
            "[Sound effect] Subtitle",
            "Subtitle",
            "Multi line Subtitle",
            "Sübtîtlé",
        ]

        clean_subtitles = formatting.clean(self.subtitles)
        self._assert_subtitles(clean_subtitles, expected)

    def test_brackets_cleaner(self):
        expected = [
            "Subtitle",
            "- Subtitle",
            "Subtitle",
            "<format>Subtitle</format>",
            "Multi line Subtitle",
            "Sübtîtlé",
        ]

        clean_subtitles = brackets.clean(self.subtitles)
        self._assert_subtitles(clean_subtitles, expected)


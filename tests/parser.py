from unittest import TestCase

from parameterized import parameterized

from pysubparser.parser import PARSERS
from pysubparser.parser import parse
from pysubparser.classes.exceptions import InvalidSubtitleTypeError
from pysubparser.classes.exceptions import InvalidTimestampError


PATH = './tests/files/{test_type}/test.{subtype}'


class ParserTester(TestCase):

    def validate(self, sub, index, text, clean, start, end, duration):
        self.assertEqual(sub.index, index)
        self.assertEqual(sub.text, text)
        self.assertEqual(sub.clean, clean)

        self.assertEqual(sub.start.hour, start[0])
        self.assertEqual(sub.start.minute, start[1])
        self.assertEqual(sub.start.second, start[2])

        self.assertEqual(sub.end.hour, end[0])
        self.assertEqual(sub.end.minute, end[1])
        self.assertEqual(sub.end.second, end[2])

        self.assertEqual(sub.duration, duration)

        self.assertTrue(str(index) in str(sub))
        self.assertTrue(text in str(sub))
        self.assertTrue(str(duration) in str(sub))

    @parameterized.expand(PARSERS.keys())
    def test_valid_subtitles(self, subtype):
        path = PATH.format(test_type='valid', subtype=subtype)

        subtitles = parse(path, subtype=subtype, fps=24)

        self.validate(
            sub=next(subtitles),
            index=0,
            text='Subtitle',
            clean='subtitle',
            start=(0, 0, 1),
            end=(0, 0, 2),
            duration=1000
        )

        self.validate(
            sub=next(subtitles),
            index=1,
            text='- Subtitle',
            clean='subtitle',
            start=(0, 0, 3),
            end=(0, 0, 3),
            duration=500
        )

        self.validate(
            sub=next(subtitles),
            index=2,
            text='[Sound effect] Subtitle',
            clean='subtitle',
            start=(0, 1, 5),
            end=(0, 1, 5),
            duration=250
        )

        self.validate(
            sub=next(subtitles),
            index=3,
            text='<format>Subtitle</format>',
            clean='subtitle',
            start=(1, 30, 0),
            end=(1, 35, 0),
            duration=300000
        )

        self.validate(
            sub=next(subtitles),
            index=4,
            text='Multi line Subtitle',
            clean='multi line subtitle',
            start=(2, 0, 0),
            end=(2, 11, 11),
            duration=671000
        )

        self.validate(
            sub=next(subtitles),
            index=5,
            text='Subtitle',
            clean='subtitle',
            start=(2, 20, 0),
            end=(3, 0, 0),
            duration=2400000
        )

    @parameterized.expand(PARSERS.keys())
    def test_invalid_timestamps(self, subtype):
        path = PATH.format(test_type='invalid_timestamps', subtype=subtype)

        subtitles = parse(path, subtype=subtype, fps=24)

        with self.assertRaises(InvalidTimestampError):
            next(subtitles)

    def test_invalid_file(self):
        with self.assertRaises(InvalidSubtitleTypeError):
            parse('test.py')

        with self.assertRaises(InvalidSubtitleTypeError):
            parse(PATH.format(test_type='valid', subtype='srt'), subtype='py')

    def test_invalid_encoding(self):
        with self.assertRaises(UnicodeDecodeError):
            list(parse(PATH.format(test_type='invalid_encoding', subtype='srt'), encoding='ascii'))


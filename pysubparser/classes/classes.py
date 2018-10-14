import re

import unidecode

ALPHA_CLEANER = re.compile(r'[^\w\s]+', re.UNICODE)
BRACKETS_CLEANER = re.compile(r'\[[^[]*\]', re.UNICODE)
FORMAT_CLOSE_CLEANER = re.compile(r'</[^[]*>', re.UNICODE)
FORMAT_OPEN_CLEANER = re.compile(r'<[^[]*>', re.UNICODE)
WHITESPACE_CLEANER = re.compile(r'\s+', re.UNICODE)


def time_to_milliseconds(time):
    return ((time.hour * 60 + time.minute) * 60 + time.second) * 1000 + time.microsecond//1000


class Subtitle:
    def __init__(self, index, start=None, end=None, text_lines=None):
        self.index = index
        self.start = start
        self.end = end
        self.text_lines = text_lines if text_lines else []

    @property
    def text(self):
        return ' '.join(self.text_lines)

    @property
    def clean(self):
        return self.clean_up(to_lowercase=True, to_ascii=True, remove_brackets=True, remove_formatting=True)

    @property
    def duration(self):
        return time_to_milliseconds(self.end) - time_to_milliseconds(self.start)

    def add_text_line(self, text):
        self.text_lines.append(text)

    def clean_up(self, to_lowercase=True, to_ascii=False, remove_brackets=False, remove_formatting=False):
        text = self.text

        if to_lowercase:
            text = text.lower()

        if remove_brackets:
            text = BRACKETS_CLEANER.sub('', text)

        if remove_formatting:
            text = FORMAT_CLOSE_CLEANER.sub('', text)
            text = FORMAT_OPEN_CLEANER.sub('', text)

        text = ALPHA_CLEANER.sub('', text)
        text = WHITESPACE_CLEANER.sub(' ', text).strip()

        if to_ascii:
            text = unidecode.unidecode(text)

        return text

    def __repr__(self):
        return f'{self.index} > {self.text} ({self.duration} ms.)'


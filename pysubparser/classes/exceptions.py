class InvalidSubtitleTypeError(ValueError):

    def __init__(self, subtype, accepted):
        message = f'{subtype} is not valid subtitle type ({list(accepted)}).'

        super().__init__(message)


class InvalidTimestampError(ValueError):

    def __init__(self, timestamp, expected_format, subtype):
        message = f'{timestamp} does not match the format for {subtype} ({expected_format}).'

        super().__init__(message)

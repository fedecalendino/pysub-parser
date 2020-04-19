class InvalidSubtitleTypeError(ValueError):

    def __init__(self, subtitle_type: str, accepted):
        message = f"{subtitle_type} is not valid" \
                  f" subtitle type ({list(accepted)})."

        super().__init__(message)


class InvalidTimestampError(ValueError):

    def __init__(self, timestamp, expected_format: str, subtitle_type: str):
        message = f"{timestamp} does not match the" \
                  f" format for {subtitle_type} ({expected_format})."

        super().__init__(message)

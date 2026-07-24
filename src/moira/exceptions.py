from httptoolkit.response import Response

__all__ = [
    "MoiraError",
    "MoiraApiError",
    "MoiraServerError",
]


class MoiraError(Exception):
    """Base exception"""


class MoiraApiError(MoiraError):
    def __init__(self, response: Response):
        super(MoiraApiError, self).__init__(response.reason)


class MoiraServerError(MoiraError):
    """"""

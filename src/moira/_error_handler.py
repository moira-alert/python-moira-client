from contextlib import contextmanager
from typing import Type

from httptoolkit.errors import HttpError

from moira.exceptions import MoiraApiError, MoiraServerError


class ErrorHandler:
    def __init__(self, error_class: Type[MoiraApiError]):
        self._error_class = error_class

    @contextmanager
    def handle(self):
        try:
            yield
        except HttpError as error:
            response = error.response
            if 400 <= response.status_code < 500:
                raise self._error_class(response=response) from error
            raise MoiraServerError(response.reason) from error

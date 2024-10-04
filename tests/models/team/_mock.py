try:
    from unittest.mock import patch, Mock

except ImportError:
    from mock import patch, Mock


__all__ = [
    "patch",
    "Mock",
]

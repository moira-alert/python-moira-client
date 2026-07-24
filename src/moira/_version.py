from os import environ

__version__ = environ.get("CI_COMMIT_TAG") or "0.dev0"

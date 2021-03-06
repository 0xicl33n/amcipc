"""Locations."""

from re import compile  # pylint: disable=W0622
from typing import NamedTuple


__all__ = ['Location']


REGEX = compile('.*\\[(-?\\d+), (~|-?\\d+), (-?\\d+)\\].*')


def _int_or_none(string):
    """Returns None iff coordinate is special "~"
    character or else the respective integer value.
    """

    if string == '~':
        return None

    return int(string)


class Location(NamedTuple):
    """A 3D location."""

    x: int
    y: int
    z: int

    @classmethod
    def from_response(cls, text):
        """Creates a location from a server response."""
        match = REGEX.fullmatch(text)
        return cls(*(_int_or_none(item) for item in match.groups()))

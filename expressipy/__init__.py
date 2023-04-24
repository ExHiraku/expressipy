"""
Expressipy: OtakuGIFs API Wrapper
~~~~~~~~~~~~~~~~~~~~~

A basic wrapper for the OtakuGIFs API.

:copyright: (c) 2023-present ExHiraku
:license: MIT, see LICENSE for more details.

"""

__title__ = "expressipy"
__author__ = "ExHiraku"
__license__ = "MIT"
__copyright__ = "Copyright 2023-present ExHiraku"
__version__ = "1.0"

from .client import Client
from .errors import InvalidReaction, ReactionNotAvailable, ReactionNotFound
from .reactions import REACTIONS

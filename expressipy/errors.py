"""
MIT License

Copyright (c) 2023 ExHiraku

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


class ExpressionException(Exception):
    """Base exception class for expressipy

    Caught to handle any exceptions raised from this library.
    """

    pass


class InvalidReaction(ExpressionException):
    """Exception that is raised when an unsupported reaction is provided."""

    pass


class ReactionNotAvailable(ExpressionException):
    """Exception that is raised when a reaction is not available on the API.

    This should not be called when a non-existing reaction is requested."""

    pass


class ReactionNotFound(ExpressionException):
    """Exception that is raised when a reaction does not exist on the API."""

    pass

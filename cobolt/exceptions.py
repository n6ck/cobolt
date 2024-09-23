"""
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""

from __future__ import annotations


class APIError(Exception):
    """Common exception for all API-related errors."""

    pass


class FetchError(APIError):
    """Common exception for all fetch-related errors."""

    pass


class FetchFailed(FetchError):
    """Raised when trying to fetch information from the requested service failed."""

    pass


class FetchCrticial(FetchError):
    """Raised when an unexpected error occurs while processing a request."""

    pass


class FetchEmpty(FetchError):
    """Raised when no media is returned from the requested service."""

    pass


class FetchRateLimited(FetchError):
    """Raised when the processing server is rate-limited by the API of the requested service."""

    pass


class FetchShortLinkFailed(FetchError):
    """Raised when information could not be retrieved from a shortened link."""

    pass

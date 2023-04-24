from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from .client import Client

    ClientT = TypeVar("ClientT", bound=Client)

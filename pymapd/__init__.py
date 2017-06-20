# module constants
# XXX: distribute with package, or place in site-packages at install
import sys
sys.path.insert(0, "../mapd-core/gen-py")
import mapd            # noqa
from mapd import MapD  # noqa


apilevel = "2.0"
threadsafety = 1  # TODO: check
paramstyle = "qmark"

from .connection import (  # noqa
    connect, Connection
)

from .exceptions import (
    Warning,
    Error,
    InterfaceError,
    DatabaseError,
    DataError,
    OperationalError,
    IntegrityError,
    InternalError,
    ProgrammingError,
    NotSupportedError,
)
from .utils import checksum


class SerialError(Exception):
    """Exception raised when there's a problem with serial."""


class SerialErrCheckSum(SerialError):
    """Exception raised when there'a problem with checksum."""


class SerialErrPckgLen(SerialError):
    """Exception raised when there'a problem with package length."""


class SerialForbidden(SerialError):
    """Exception raised when a given operation is not permitted by the UDC"""


class SerialInvalidCmd(SerialError):
    """Exception raised when the supplied command is invalid"""


SERIAL_ERROR = [
    "Ok",
    "Power supply in local mode",
    "Power supply in PC host mode",
    "Power supply interlocked",
    "UDC stuck",
    "DSP timeout",
    "DSP busy",
    "Resource is busy",
    "Invalid command",
]


def validate(func):
    def wrapper(*args, **kwargs):
        reply = func(*args, **kwargs)
        if reply != checksum(reply[:-1]):
            raise SerialErrCheckSum

        if reply[1] == 0x53:
            if reply[-2] == 4:
                raise SerialForbidden
            if reply[-2] == 8:
                raise SerialInvalidCmd
            # else:
            #    raise SerialError(SERIAL_ERROR[reply[-2]])

        if len(reply) != args[2]:
            raise SerialErrPckgLen(
                "Expected {} bytes, received {} bytes".format(args[2], len(reply))
            )

        return reply

    return wrapper

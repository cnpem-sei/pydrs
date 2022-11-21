import unittest

from pydrs.validation import (
    SerialErrCheckSum,
    SerialError,
    SerialErrPckgLen,
    SerialForbidden,
    SerialInvalidCmd,
    validate,
)


def mock_socket(self, _1, _2):
    return True


class TestValidation(unittest.TestCase):
    def setUp(self) -> None:
        @validate
        def transfer(_, x, s):
            return x

        self.transfer = transfer
        self.reset_input_buffer = lambda: ()

    def test_empty(self):
        with self.assertRaises(SerialErrPckgLen):
            self.transfer(self, b"", 3)

    def test_empty_new_eth(self):
        with self.assertRaises(SerialErrPckgLen):
            self.transfer(self, b"#", 3)

    def test_mismatched_size(self):
        with self.assertRaises(SerialErrPckgLen):
            self.transfer(self, b"\x01\x01", 3)

    def test_mismatched_size_new_eth(self):
        with self.assertRaises(SerialErrPckgLen):
            self.transfer(self, b"!\x01\x01", 3)

    def test_mismatched_checksum(self):
        with self.assertRaises(SerialErrCheckSum):
            self.transfer(self, b"\x01\x01", 2)

    def test_mismatched_checksum_new_eth(self):
        with self.assertRaises(SerialErrCheckSum):
            self.transfer(self, b"!\x01\x01", 2)

    def test_invalid_cmd(self):
        with self.assertRaises(SerialInvalidCmd):
            self.transfer(self, b"\x05\x53\x00\x01\x08\x9f", 6)

    def test_invalid_cmd_new_eth(self):
        with self.assertRaises(SerialInvalidCmd):
            self.transfer(self, b"!\x05\x53\x00\x01\x08\x9f", 6)

    def test_forbidden(self):
        with self.assertRaises(SerialForbidden):
            self.transfer(self, b"\x05\x53\x00\x01\x04\xa3", 6)

    def test_forbidden_new_eth(self):
        with self.assertRaises(SerialForbidden):
            self.transfer(self, b"!\x05\x53\x00\x01\x04\xa3", 6)

    def test_serial_error(self):
        with self.assertRaises(SerialError):
            self.transfer(self, b"!\x05\x53\x00\x01\x06\xa1", 6)

    def test_valid(self):
        self.assertEqual(
            self.transfer(self, b"\x05\x51\x00\x01\x04\xa5", 6),
            b"\x05\x51\x00\x01\x04\xa5",
        )

    def test_valid_new_eth(self):
        self.assertEqual(
            self.transfer(self, b"!\x05\x51\x00\x01\x04\xa5", 6),
            b"\x05\x51\x00\x01\x04\xa5",
        )


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import Mock, call, patch
from pydrs import GenericDRS, EthDRS
from pydrs.validation import SerialErrPckgLen


class TestEthConnect(unittest.TestCase):
    sequence = []

    @patch("socket.socket")
    def setUp(self, socket):
        socket = socket.return_value
        self.drs = GenericDRS("127.0.0.1", 5000)

    def _call_sequence(self, _):
        try:
            return self.sequence.pop()
        except IndexError:
            return b""

    def test_generic(self):
        self.assertIsInstance(self.drs, EthDRS)

    def test_transfer_message_ok(self):
        self.drs.socket.recv.return_value = b"\x12\x00\x00\x00\xEE"
        self.drs._transfer("\x12", 5)

        self.drs.socket.sendall.assert_called_with(
            b"\x11\x00\x00\x00\x07BH\x00\x00\x01\x12\xed"
        )

    def test_transfer_message_timeout(self):
        self.drs.socket.recv.return_value = b"\x22\x00\x00\x00\xDD"

        with self.assertRaises(TimeoutError):
            self.drs._transfer("\x12", 5)
            self.drs._reset_input_buffer.assert_called()

    def test_transfer_message_empty(self):
        self.sequence = [b"", b"\x12\x00\x00\x00\x05"]
        self.drs.socket.recv.side_effect = self._call_sequence

        with self.assertRaises(SerialErrPckgLen):
            self.drs._transfer("\x12", 5)
            self.drs._reset_input_buffer.assert_called()

    def test_set_timeout(self):
        self.drs.timeout = 5
        self.drs.socket.settimeout.assert_called_with(5)
        self.assertEqual(self.drs._serial_timeout, 5000)


if __name__ == "__main__":
    unittest.main()

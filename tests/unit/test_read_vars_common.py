import unittest
from unittest.mock import patch

from pydrs import GenericDRS

return_value = b"\x00" * 252


class TestCommon(unittest.TestCase):
    @patch("socket.socket")
    @patch("pydrs.EthDRS._transfer")
    def setUp(self, transfer, socket):
        socket = socket.return_value
        self.drs = GenericDRS("127.0.0.1", 5000)
        self.drs._transfer = transfer

    def _call_sequence(self, _):
        try:
            return self.sequence.pop()
        except IndexError:
            return b""

    def test_read(self):
        self.drs._transfer.return_value = return_value
        self.drs.read_vars_common()

    def test_version(self):
        ret_val = bytearray(return_value)
        ret_val[14:142] = bytearray(b"0.44.01    28/080.44.01    28/08") + b"\x00" * (
            128 - 32
        )
        self.drs._transfer.return_value = bytes(ret_val)

        read_vals = self.drs.read_vars_common()

        self.assertEqual(read_vals["version"]["udc_arm"], "0.44.01    28/08")
        self.assertEqual(read_vals["version"]["udc_c28"], "0.44.01    28/08")


if __name__ == "__main__":
    unittest.main()

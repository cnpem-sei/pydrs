import unittest
from unittest.mock import patch

from pydrs import EthDRS, GenericDRS

return_value = b"\x00" * 252


class TestCommon(unittest.TestCase):
    @patch("pydrs.EthDRS._transfer")
    def setUp(self, transfer):
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


if __name__ == "__main__":
    unittest.main()

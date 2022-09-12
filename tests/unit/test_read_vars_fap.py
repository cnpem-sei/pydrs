import unittest
from unittest.mock import patch

from pydrs import GenericDRS

return_value = b"\x00" * 690


class TestFAP(unittest.TestCase):
    @patch("pydrs.EthDRS._transfer")
    def setUp(self, transfer):
        self.drs = GenericDRS("127.0.0.1", 5000)
        self.drs._transfer = transfer

    def _call_sequence(self, _):
        try:
            return self.sequence.pop()
        except IndexError:
            return b""

    def test_no_interlocks(self):
        self.drs._transfer.return_value = b"\x00" * 359
        self.drs.read_vars_fap()

    def test_4p(self):
        self.drs._transfer.return_value = b"\x00" * 615
        self.drs.read_vars_fap_4p()

    def test_2p2s(self):
        self.drs._transfer.return_value = b"\x00" * 635
        self.drs.read_vars_fap_2p2s()


if __name__ == "__main__":
    unittest.main()

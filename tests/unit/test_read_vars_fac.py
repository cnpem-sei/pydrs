import unittest
from unittest.mock import patch

from pydrs import GenericDRS

return_value = b"\x00" * 590


class TestFAC(unittest.TestCase):
    @patch("pydrs.EthDRS._transfer")
    def setUp(self, transfer):
        self.drs = GenericDRS("127.0.0.1", 5000)
        self.drs._transfer = transfer

    def _call_sequence(self, _):
        try:
            return self.sequence.pop()
        except IndexError:
            return b""

    def test_2p4s_acdc(self):
        self.drs._transfer.return_value = b"\x00" * 374
        read_vals = self.drs.read_vars_fac_2p4s_acdc()

    def test_2p4s_dcdc(self):
        self.drs._transfer.return_value = b"\x00" * 462
        read_vals = self.drs.read_vars_fac_2p4s_dcdc()

    def test_2p_acdc_imas(self):
        self.drs._transfer.return_value = b"\x00" * 282
        read_vals = self.drs.read_vars_fac_2p_acdc_imas()

    def test_2s_acdc(self):
        self.drs._transfer.return_value = b"\x00" * 374
        read_vals = self.drs.read_vars_fac_2s_acdc()

    def test_2s_dcdc(self):
        self.drs._transfer.return_value = b"\x00" * 406
        read_vals = self.drs.read_vars_fac_2s_dcdc()

    def test_acdc(self):
        self.drs._transfer.return_value = b"\x00" * 366
        read_vals = self.drs.read_vars_fac_acdc()

    def test_dcdc(self):
        self.drs._transfer.return_value = b"\x00" * 346
        read_vals = self.drs.read_vars_fac_dcdc()

    def test_dcdc_ema(self):
        self.drs._transfer.return_value = b"\x00" * 338
        read_vals = self.drs.read_vars_fac_dcdc_ema()


if __name__ == "__main__":
    unittest.main()

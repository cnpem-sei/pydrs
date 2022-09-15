import unittest
from unittest.mock import patch

from pydrs import GenericDRS

return_value = b"\x00" * 390


class TestFBP(unittest.TestCase):
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

    def test_no_interlocks(self):
        self.drs._transfer.return_value = return_value

        read_vals = self.drs.read_vars_fbp()

        self.assertEqual(read_vals["soft_interlocks"], [])
        self.assertEqual(read_vals["hard_interlocks"], [])

    def test_interlocks(self):
        ilock = bytearray(return_value)
        ilock[246:250] = [0b0001, 0, 0, 0]
        ilock[250:254] = [0b000101000, 0, 0, 0]
        self.drs._transfer.return_value = bytes(ilock)

        read_vals = self.drs.read_vars_fbp()

        self.assertEqual(
            read_vals["soft_interlocks"], ["bit 0: Heat-Sink Overtemperature"]
        )
        self.assertEqual(
            read_vals["hard_interlocks"],
            ["bit 3: DCLink Undervoltage", "bit 5: DCLink Fuse Fault"],
        )

    def test_values(self):
        ret_val = bytearray(return_value)

        self.drs._transfer.return_value = return_value
        read_vals = self.drs.read_vars_fbp()

        self.assertEqual(read_vals["i_load"], "0.0 A")
        self.assertEqual(read_vals["v_load"], "0.0 V")
        self.assertEqual(read_vals["v_dclink"], "0.0 V")
        self.assertEqual(read_vals["duty_cycle"], "0.0 %")
        self.assertEqual(read_vals["temp_switches"], "0.0 °C")

        ret_val[254:258] = [0x00, 0x00, 0x00, 0x40]
        ret_val[258:262] = [0x00, 0x00, 0x00, 0x41]
        ret_val[262:266] = [0x00, 0x00, 0x00, 0x42]
        ret_val[266:270] = [0x00, 0x00, 0x00, 0x43]
        ret_val[270:274] = [0x00, 0x00, 0x00, 0x42]

        self.drs._transfer.return_value = bytes(ret_val)
        read_vals = self.drs.read_vars_fbp()

        self.assertEqual(read_vals["i_load"], "2.0 A")
        self.assertEqual(read_vals["v_load"], "8.0 V")
        self.assertEqual(read_vals["v_dclink"], "32.0 V")
        self.assertEqual(read_vals["duty_cycle"], "32.0 %")
        self.assertEqual(read_vals["temp_switches"], "128.0 °C")

    def test_dclink(self):
        self.drs._transfer.return_value = b"\x00" * 276
        self.assertIsInstance(self.drs.read_vars_fbp_dclink(), dict)


if __name__ == "__main__":
    unittest.main()

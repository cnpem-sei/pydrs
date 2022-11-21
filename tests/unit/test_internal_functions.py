import unittest
from unittest.mock import patch

from pydrs import GenericDRS
from pydrs.consts import common

status_keys = ["state", "open_loop", "interface", "active", "model", "unlocked"]


class TestFBP(unittest.TestCase):
    @patch("socket.socket")
    def setUp(self, socket):
        socket = socket.return_value
        self.drs = GenericDRS("127.0.0.1", 5000)

    def test_parse_status(self):
        for key in status_keys:
            self.assertIn(key, self.drs._parse_status(0b0000000000000000))

    def test_parse_status_open(self):
        vals = self.drs._parse_status(0b0000000000010000)
        self.assertEqual(vals["open_loop"], 1)

    def test_parse_status_unlocked(self):
        vals = self.drs._parse_status(0b0010000000000000)
        self.assertEqual(vals["unlocked"], 1)

    def test_parse_status_active(self):
        vals = self.drs._parse_status(0b0000000010000000)
        self.assertEqual(vals["active"], 1)

    def test_parse_status_state(self):
        for i, state in enumerate(common.op_modes):
            vals = self.drs._parse_status(i)
            self.assertEqual(vals["state"], state)

    def test_parse_status_model(self):
        for i, model in enumerate(common.ps_models):
            vals = self.drs._parse_status(i << 8)
            self.assertEqual(vals["model"], model)


if __name__ == "__main__":
    unittest.main()

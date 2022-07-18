import json
from unittest import TestCase

from pydrs import pydrs
from pydrs.validation import SerialInvalidCmd


class TestAct(TestCase):
    def setUp(self):
        with open("secrets.json") as f:
            self.secret = json.loads(f.read())

        self.drs = pydrs.EthDRS(self.secret["ip"], self.secret["port"])

    def test_turn_on(self):
        self.drs.turn_on()

    def test_turn_off(self):
        self.drs.turn_off()

    def test_invalid_password(self):
        with self.assertRaises(SerialInvalidCmd):
            self.drs.unlock_udc(0xDEAD)

    def test_valid_password(self):
        self.drs.unlock_udc(self.secret["password"])

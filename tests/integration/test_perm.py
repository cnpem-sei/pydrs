import json
from unittest import TestCase

from pydrs import pydrs
from pydrs.validation import SerialForbidden, SerialInvalidCmd


class TestPerm(TestCase):
    def setUp(self):
        with open("secrets.json") as f:
            self.secret = json.loads(f.read())

        self.drs = pydrs.EthDRS(self.secret["ip"], self.secret["port"])
        self.drs.lock_udc(self.secret["password"])

    def test_forbidden_set_param(self):
        with self.assertRaises(SerialForbidden):
            self.drs.set_ps_name("A Name")

    def test_invalid_password(self):
        with self.assertRaises(SerialInvalidCmd):
            self.drs.unlock_udc(0xDEAD)

    def test_valid_password(self):
        self.drs.unlock_udc(self.secret["password"])

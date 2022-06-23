from unittest import TestCase
from pydrs import pydrs
import json

from pydrs.validation import SerialInvalidCmd


class TestSet(TestCase):
    def setUp(self):
        with open("secrets.json") as f:
            self.secret = json.loads(f.read())

        self.drs = pydrs.EthDRS(self.secret["ip"], self.secret["port"])

    def test_set_slowref(self):
        self.drs.set_slowref(100)

    def test_set_slowref_fbp(self):
        self.drs.set_slowref_fbp(100)

    def test_set_slowref_readback_mon(self):
        self.assertAlmostEqual(0, self.drs.set_slowref_readback_mon(100), 3)

    def test_set_slowref_readback_ref(self):
        self.assertAlmostEqual(0, self.drs.set_slowref_readback_ref(100), 3)

    def test_invalid_password(self):
        with self.assertRaises(SerialInvalidCmd):
            self.drs.unlock_udc(0xDEAD)

    def test_valid_password(self):
        self.drs.unlock_udc(self.secret["password"])

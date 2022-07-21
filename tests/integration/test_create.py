from unittest import TestCase

from pydrs import pydrs
from pydrs.validation import SerialInvalidCmd


class TestCreate(TestCase):
    def test_create_eth(self):
        self.assertIsInstance(pydrs.GenericDRS("10.0.6.64", 5000), pydrs.EthDRS)

    def test_turn_off(self):
        self.assertIsInstance(pydrs.GenericDRS("/dev/ttyS1", 3000000), pydrs.SerialDRS)

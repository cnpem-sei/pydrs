from unittest import TestCase
from pydrs import pydrs
import json


class TestRead(TestCase):
    def setUp(self):
        with open("secrets.json") as f:
            self.secret = json.loads(f.read())

        self.drs = pydrs.EthDRS(self.secret["ip"], self.secret["port"])

    def test_read_udc_arm_version(self):
        self.assertEqual(self.drs.read_udc_arm_version(), "V0.43 2021-12-02")

    def test_get_scope_vars(self):
        self.drs.get_scope_vars()

    def test_get_default_ramp_waveform(self):
        self.assertEqual(len(self.drs.get_default_ramp_waveform()), 4000)

    def test_get_wfmref_vars(self):
        self.drs.get_wfmref_vars(1)

    def test_read_curve_block(self):
        self.assertEquals(len(self.drs.read_curve_block(0, 0)), 256)

    def test_get_ps_name(self):
        self.drs.unlock_udc(self.secret["password"])
        self.drs.set_ps_name(
            "Jiga FBP para teste de resposta a setpoints do grupo CONS"
        )
        self.assertEqual(
            self.drs.get_ps_name(),
            "Jiga FBP para teste de resposta a setpoints do grupo CONS",
        )
        self.drs.lock_udc(self.secret["password"])

    def test_get_param_bank(self):
        self.drs.get_param_bank()

    def test_get_param_valid(self):
        self.assertIsInstance(self.drs.get_param(26), float)

    def test_get_param_invalid(self):
        val = self.drs.get_param(2999)
        self.assertNotEquals(val, val)

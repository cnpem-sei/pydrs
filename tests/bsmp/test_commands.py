from unittest import TestCase

from siriuspy.pwrsupply.bsmp.constants import ConstPSBSMP

from pydrs.bsmp import CommonPSBSMP, EntitiesPS, SerialInterface


class TestSerialCommandsx0(TestCase):
    """Test BSMP consulting methods."""

    def setUp(self):
        """Common setup for all tests."""

        self._serial = SerialInterface(path="/serial", baudrate=9600)
        self._entities = EntitiesPS()

        self._pwrsupply = CommonPSBSMP(iointerface=self._serial, entities=self._entities, slave_address=1)

    def test_query_protocol_version(self):
        """Test"""

    def test_query_variable(self):
        """Test"""
        self._pwrsupply.pread_variable(var_id=ConstPSBSMP.V_PS_STATUS, timeout=500)

    def test_query_parameter(self):
        """Test"""
        self._pwrsupply.parameter_read(var_id=ConstPSBSMP.P_PS_NAME, timeout=500)

    def test_write_parameter(self):
        """Test"""
        self._pwrsupply.parameter_write(var_id=ConstPSBSMP.P_PS_NAME, value="pv_test_name", timeout=500)

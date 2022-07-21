from unittest import TestCase

from serial.serialutil import SerialException

from pydrs.bsmp import SerialInterface


class TestSerialInterface(TestCase):
    def test_serial_creation(self):
        with self.assertRaises(SerialException):
            SerialInterface(path="/serial", baudrate=9600, auto_connect=True)

        with self.assertRaises(TypeError):
            SerialInterface()

        with self.assertRaises(ValueError):
            SerialInterface(path=None, baudrate=None)

    def test_serial_write(self):
        raise NotImplementedError()

    def test_serial_read(self):
        raise NotImplementedError()

    def test_serial_request(self):
        raise NotImplementedError()

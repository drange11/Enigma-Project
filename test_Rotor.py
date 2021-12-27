import pytest
import Rotor

class TestClass:

    def test_getEncript():
        myRotor = Rotor(1, 0)
        assert myRotor.getEncriptChar('a') == 'd'

    def test_rotate():
        myRotor = Rotor(1, 0)
        myRotor.rotate()
        assert myRotor.getEncriptChar('a') == 'g'
from unittest import TestCase
from app.app import convert_to_cm, convert_to_inches

class TestConvertToCM(TestCase):
    def test_should_return_2_54_when_get_1(self):
        self.assertAlmostEqual(convert_to_cm(1), 2.54, places=1)


"""
 def test_deve_retornar_0_quando_receber_32(self):
        assert converte_F_para_C(32) == 0
"""
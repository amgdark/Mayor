import unittest
import sys
sys.path.append('../')

from app.NumeroMayor import NumeroMayor

class TestNumeroMayor(unittest.TestCase):
	def setUp(self):
		self.numero = NumeroMayor()

	def test_numero_5_mayor_que_4(self):
		self.assertEqual(self.numero.obtiene_mayor(5, 4), 5)

	def test_numero_3_mayor_que_8(self):
		self.assertEqual(self.numero.obtiene_mayor(3, 8), 8)	

	def test_numero_5_mayor_que_54(self):
		self.assertEqual(self.numero.obtiene_mayor(5, 5), 'son iguales')	

if __name__ == '__main__':
	unittest.main()		
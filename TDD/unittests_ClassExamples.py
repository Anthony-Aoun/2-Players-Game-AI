import unittest
import ClassExample



class TestClassExample(unittest.TestCase):
   
    def test_price(self):
        my_computer = ClassExample.PC('Lenovo','E570',1000.0,'intel i7','20 GB')
        self.assertEqual(my_computer.get_price(),1000.0)

    def test_discount(self):
        my_computer = ClassExample.PC('Lenovo','E570',1000.0,'intel i7','20 GB')
        my_computer.discount(20)
        self.assertEqual(my_computer.price,800.0)

    def test_password(self):
        my_phone = ClassExample.Mobile('iPhone','6S+',600.0,74,'1234')
        self.assertIs(my_phone.get_password(),'1234')

    def test_battery(self):
        my_phone = ClassExample.Mobile('iPhone','6S+',600.0,74,'1234')
        my_phone.recharge_battery(10)
        self.assertEqual(my_phone.battery_percentage,84)




if __name__=='__main__':
    unittest.main()
import unittest
from console import HBNBCommand

class TestConsoleCreate(unittest.TestCase):

    def test_create_with_string_params(self):
        HBNBCommand.classes['TestClass'] = lambda **kwargs: kwargs
        cmd = HBNBCommand()
        cmd.onecmd('create TestClass name="My House" color="Red"')
        result = cmd.onecmd('all')
        self.assertIn("'name': 'My House'", result)
        self.assertIn("'color': 'Red'", result)

    def test_create_with_float_params(self):
        HBNBCommand.classes['TestClass'] = lambda **kwargs: kwargs
        cmd = HBNBCommand()
        cmd.onecmd('create TestClass price=12.34 weight=5.67')
        result = cmd.onecmd('all')
        self.assertIn("'price': 12.34", result)
        self.assertIn("'weight': 5.67", result)

    def test_create_with_integer_params(self):
        HBNBCommand.classes['TestClass'] = lambda **kwargs: kwargs
        cmd = HBNBCommand()
        cmd.onecmd('create TestClass quantity=10 size=3')
        result = cmd.onecmd('all')
        self.assertIn("'quantity': 10", result)
        self.assertIn("'size': 3", result)

    def test_create_with_invalid_params(self):
        HBNBCommand.classes['TestClass'] = lambda **kwargs: kwargs
        cmd = HBNBCommand()
        cmd.onecmd('create TestClass name=My House')  # Missing quotes around value
        result = cmd.onecmd('all')
        self.assertEqual("**** Unknown syntax: name=My House\n", result)

if __name__ == '__main__':
    unittest.main()


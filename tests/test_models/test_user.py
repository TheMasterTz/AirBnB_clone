mport unittest
from models.user import User

class TestMyUser(unittest.TestCase):
    """Class TestMyUser to test class User"""

    def setUp(self):
        """setting up each test"""
        self.new = User()

    def tearsDown(self):
        """cleaning up after each test"""
        self.new = User()

    def test_empty_strings_before(self):
        """Check if the strings are empty before assignment"""
        self.assertFalse(self.new.email)
        self.assertFalse(self.new.password)
        self.assertFalse(self.new.first_name)
        self.assertFalse(self.new.last_name)

    def test_methods_exist(self):
        """Check if the methods are present"""
        assert self.new.__init__ is not None
        assert self.new.save is not None
        assert self.new.to_dict is not None
        assert self.new.updated_at is not None
        assert self.new.__str__ is not None

    def test_attributes_exist(self):
        """Assign attributes and check if they are not None"""
        self.new.email = 'hello.hi@hotmail.com'
        self.new.password = 'AnBJhNwIcEj'
        self.new.first_name = 'Larry'
        self.new.last_name = 'kapinga'

        self.assertNotEqual(self.new.email, None)
        self.assertNotEqual(self.new.password, None)
        self.assertNotEqual(self.new.first_name, None)
        self.assertNotEqual(self.new.last_name, None)

    def test_if_str(self):
        """Check if the attributes are strings"""
        self.new.email = 'hello.hi@hotmail.com'
        self.new.password = 'AnBJhNwIcEj'
        self.new.first_name = 'Larry'
        self.new.last_name = 'kapinga'

        self.assertEqual(type(self.new.email), str)
        self.assertEqual(type(self.new.password), str)
        self.assertEqual(type(self.new.first_name), str)
        self.assertEqual(type(self.new.last_name), str)

    def test_attributes_are_correct(self):
        """Check if assigments happened as intended"""
        self.new.email = 'hello.hi@hotmail.com'
        self.new.password = 'AnBJhNwIcEj'
        self.new.first_name = 'Larry'
        self.new.last_name = 'Kapinga'

        self.assertEqual(self.new.email, 'hello.hi@hotmail.com')
        self.assertEqual(self.new.password, 'AnBJhNwIcEj')
        self.assertEqual(self.new.first_name, 'Larry')
        self.assertEqual(self.new.last_name, 'Kapinga')

if __name__ == '__main__':
    unittest.main()

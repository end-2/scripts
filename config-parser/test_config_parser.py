import unittest
from config_parser import parse_file

class TestParsing(unittest.TestCase):
    test_file_path = "test-files/test"

    def test_parse_yaml(self):
        expected = {
            'configuration': {
                'settings': {
                    'language': 'English',
                    'theme': 'Light'
                },
                'users': [
                    {
                        'name': 'John Doe',
                        'age': 30,
                        'email': 'john.doe@example.com'
                    },
                    {
                        'name': 'Jane Doe',
                        'age': 28,
                        'email': 'jane.doe@example.com'
                    }
                ],
                'colors': ['Red', 'Blue', 'Green']
            }
        }
        result = parse_file(self.test_file_path+'.yaml')
        self.assertEqual(result, expected)

    def test_parse_yml(self):
        expected = {
            'configuration': {
                'settings': {
                    'language': 'English',
                    'theme': 'Light'
                },
                'users': [
                    {
                        'name': 'John Doe',
                        'age': 30,
                        'email': 'john.doe@example.com'
                    },
                    {
                        'name': 'Jane Doe',
                        'age': 28,
                        'email': 'jane.doe@example.com'
                    }
                ],
                'colors': ['Red', 'Blue', 'Green']
            }
        }
        result = parse_file(self.test_file_path+'.yml')
        self.assertEqual(result, expected)

    def test_parse_json(self):
        expected = {
            'configuration': {
                'settings': {
                    'language': 'English',
                    'theme': 'Light'
                },
                'users': [
                    {
                        'name': 'John Doe',
                        'age': 30,
                        'email': 'john.doe@example.com'
                    },
                    {
                        'name': 'Jane Doe',
                        'age': 28,
                        'email': 'jane.doe@example.com'
                    }
                ],
                'colors': ['Red', 'Blue', 'Green']
            }
        }
        result = parse_file(self.test_file_path+'.json')
        self.assertEqual(result, expected)

    def test_parse_xml(self):
        expected = {
            'settings': {
                'setting': 'Light'
            },
            'users': {
                'user': {
                    'name': 'Jane Doe',
                    'age': '28',
                    'email': 'jane.doe@example.com'
                }
            },
            'colors': {
                'color': 'Green'
            }
        }
        result = parse_file(self.test_file_path+'.xml')
        self.assertEqual(result, expected)

    def test_parse_conf(self):
        expected = {
            'settings': {
                'language': 'English',
                'theme': 'Light'
            },
            'users': {
                'John Doe': '{"age": 30, "email": "john.doe@example.com"}',
                'Jane Doe': '{"age": 28, "email": "jane.doe@example.com"}'
            },
            'colors': {
                'color1': 'Red',
                'color2': 'Blue',
                'color3': 'Green'
            }
        }
        result = parse_file(self.test_file_path+'.conf')
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

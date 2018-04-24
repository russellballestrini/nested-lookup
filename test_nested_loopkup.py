from unittest import TestCase

from nested_lookup import nested_lookup

class TestNestedLookup(TestCase):

    def setUp(self):
        self.subject_dict = {'a':1,'b':{'d':100},'c':{'d':200}}
        self.subject_dict2 = {
            'name' : 'Russell Ballestrini',
            'email_address' : 'test1@example.com',
            'other' : {
                'secondary_email' : 'test2@example.com',
                'EMAIL_RECOVERY' : 'test3@example.com',
                'email_address' : 'test4@example.com',
            },
        }

    def test_nested_lookup(self):
        results = nested_lookup('d', self.subject_dict)
        self.assertEqual(2, len(results))
        self.assertIn(100, results)
        self.assertIn(200, results)
        self.assertSetEqual({100,200}, set(results))

    def test_nested_lookup_wrapped_in_list(self):
        results = nested_lookup('d', [{}, self.subject_dict, {}])
        self.assertEqual(2, len(results))
        self.assertIn(100, results)
        self.assertIn(200, results)
        self.assertSetEqual({100,200}, set(results))

    def test_nested_lookup_wrapped_in_list_in_dict_in_list(self):
        results = nested_lookup('d', [{}, {'H' : [self.subject_dict]} ])
        self.assertEqual(2, len(results))
        self.assertIn(100, results)
        self.assertIn(200, results)
        self.assertSetEqual({100,200}, set(results))

    def test_nested_lookup_wrapped_in_list_in_list(self):
        results = nested_lookup('d', [ {}, [self.subject_dict, {}] ])
        self.assertEqual(2, len(results))
        self.assertIn(100, results)
        self.assertIn(200, results)
        self.assertSetEqual({100,200}, set(results))

    def test_wild_nested_lookup(self):
        results = nested_lookup(
            key = 'mail',
            document = self.subject_dict2
            wild = True,
        )
        self.assertEqual(4, len(results))
        self.assertIn('test1@example.com', results)
        self.assertIn('test2@example.com', results)
        self.assertIn('test3@example.com', results)

    def test_wild_with_keys_nested_lookup(self):
        matches = nested_lookup(
            key = 'mail',
            document = self.subject_dict2,
            wild = True,
            with_keys = True,
        )
        self.assertEqual(3, len(matches))
        self.assertIn('email_address', matches)
        self.assertIn('secondary_email', matches)
        self.assertIn('EMAIL_RECOVERY', matches)
        self.assertSetEqual({'test1@example.com','test4@example.com'}, set(matches['email_address']))
        self.assertIn('test2@example.com', matches['secondary_email'])

    def test_nested_lookup_with_keys(self):
        matches = nested_lookup('d', self.subject_dict, with_keys=True)
        self.assertIn('d', matches)
        self.assertEqual(2, len(matches['d']))
        self.assertSetEqual({100,200}, set(matches['d']))


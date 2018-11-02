from unittest import TestCase

from nested_lookup import nested_lookup, get_all_keys, get_occurrence_of_key,\
    get_occurrence_of_value


class TestNestedLookup(TestCase):

    def setUp(self):
        self.subject_dict = {"a": 1, "b": {"d": 100}, "c": {"d": 200}}
        self.subject_dict2 = {
            "name": "Russell Ballestrini",
            "email_address": "test1@example.com",
            "other": {
                "secondary_email": "test2@example.com",
                "EMAIL_RECOVERY": "test3@example.com",
                "email_address": "test4@example.com",
            },
        }
        self.subject_dict3 = {
            "build_version": {
                "model_name": "MacBook Pro",
                "build_version": {
                    "processor_name": "Intel Core i7",
                    "processor_speed": "2.7 GHz",
                    "core_details": {
                        "build_version": "4",
                        "l2_cache(per_core)": "256 KB"
                    }
                },
                "number_of_cores": "4",
                "memory": "256 KB",
            },
            "os_details": {
                "product_version": "10.13.6",
                "build_version": "17G65"
            },
            "name": "Test",
            "date": "YYYY-MM-DD HH:MM:SS"
        }

    def test_nested_lookup(self):
        results = nested_lookup("d", self.subject_dict)
        self.assertEqual(2, len(results))
        self.assertIn(100, results)
        self.assertIn(200, results)
        self.assertSetEqual({100, 200}, set(results))

    def test_nested_lookup_wrapped_in_list(self):
        results = nested_lookup("d", [{}, self.subject_dict, {}])
        self.assertEqual(2, len(results))
        self.assertIn(100, results)
        self.assertIn(200, results)
        self.assertSetEqual({100, 200}, set(results))

    def test_nested_lookup_wrapped_in_list_in_dict_in_list(self):
        results = nested_lookup("d", [{}, {"H": [self.subject_dict]}])
        self.assertEqual(2, len(results))
        self.assertIn(100, results)
        self.assertIn(200, results)
        self.assertSetEqual({100, 200}, set(results))

    def test_nested_lookup_wrapped_in_list_in_list(self):
        results = nested_lookup("d", [{}, [self.subject_dict, {}]])
        self.assertEqual(2, len(results))
        self.assertIn(100, results)
        self.assertIn(200, results)
        self.assertSetEqual({100, 200}, set(results))

    def test_wild_nested_lookup(self):
        results = nested_lookup(
            key="mail", document=self.subject_dict2, wild=True)
        self.assertEqual(4, len(results))
        self.assertIn("test1@example.com", results)
        self.assertIn("test2@example.com", results)
        self.assertIn("test3@example.com", results)

    def test_wild_with_keys_nested_lookup(self):
        matches = nested_lookup(
            key="mail", document=self.subject_dict2, wild=True, with_keys=True
        )
        self.assertEqual(3, len(matches))
        self.assertIn("email_address", matches)
        self.assertIn("secondary_email", matches)
        self.assertIn("EMAIL_RECOVERY", matches)
        self.assertSetEqual({
            "test1@example.com", "test4@example.com"},
            set(matches["email_address"])
        )
        self.assertIn("test2@example.com", matches["secondary_email"])

    def test_nested_lookup_with_keys(self):
        matches = nested_lookup("d", self.subject_dict, with_keys=True)
        self.assertIn("d", matches)
        self.assertEqual(2, len(matches["d"]))
        self.assertSetEqual({100, 200}, set(matches["d"]))

    def test_after_key_is_found(self):
        result = nested_lookup(
            key='build_version', document=self.subject_dict3
        )
        self.assertEqual(4, len(result))
        self.assertIn('4', result)
        self.assertIn('17G65', result)
        match1 = {
            'processor_name': 'Intel Core i7',
            'processor_speed': '2.7 GHz',
            'core_details': {
                'build_version': '4',
                'l2_cache(per_core)': '256 KB'
            }
        }
        self.assertIn(match1, result)
        match2 = {
            'build_version': {
                'processor_name': 'Intel Core i7',
                'processor_speed': '2.7 GHz',
                'core_details': {
                    'build_version': '4',
                    'l2_cache(per_core)': '256 KB'
                }
            },
            'memory': '256 KB',
            'model_name': 'MacBook Pro',
            'number_of_cores': '4'
        }
        self.assertIn(match2, result)


class TestGetAllKeys(TestCase):

    def setUp(self):
        self.sample1 = {
            "hardware_details": {
                "model_name": "MacBook Pro",
                "processor_details": {
                    "processor_name": "Intel Core i7",
                    "processor_speed": "2.7 GHz",
                    "core_details": {
                        "total_numberof_cores": "4",
                        "l2_cache(per_core)": "256 KB",
                    },
                },
                "total_number_of_cores": "4",
                "memory": "16 GB",
            },
            "os_details": {
                "product_version": "10.13.6", "build_version": "17G65"
            },
            "name": "Test",
            "date": "YYYY-MM-DD HH:MM:SS",
        }
        self.sample2 = {
            "hardware_details": {
                "model_name": "MacBook Pro",
                "processor_details": [
                    {
                        "processor_name": "Intel Core i7",
                        "processor_speed": "2.7 GHz",
                        "core_details": {
                            "total_numberof_cores": "4",
                            "l2_cache(per_core)": "256 KB",
                        },
                    }
                ],
                "total_number_of_cores": "4",
                "memory": "16 GB",
            }
        }
        self.sample3 = {
            "hardware_details": {
                "model_name": "MacBook Pro",
                "processor_details": [
                    {
                        "processor_name": "Intel Core i7",
                        "processor_speed": "2.7 GHz"
                    },
                    {
                        "total_numberof_cores": "4",
                        "l2_cache(per_core)": "256 KB"
                    },
                ],
                "total_number_of_cores": "4",
                "memory": "16 GB",
            }
        }
        self.sample4 = {
            "values": [
                {
                    "checks": [
                        {
                            "monitoring_zones": [
                                "mzdfw",
                                "mzfra",
                                "mzhkg",
                                "mziad",
                                "mzlon",
                                "mzord",
                                "mzsyd"
                            ]
                        }
                    ]
                }
            ]
        }

    def test_sample_data1(self):
        result = get_all_keys(self.sample1)
        self.assertEqual(15, len(result))
        keys_to_verify = [
            "model_name",
            "core_details",
            "l2_cache(per_core)",
            "build_version",
            "date",
        ]
        for key in keys_to_verify:
            self.assertIn(key, result)

    def test_sample_data2(self):
        result = get_all_keys(self.sample2)
        self.assertEqual(10, len(result))
        keys_to_verify = [
            "hardware_details",
            "processor_speed",
            "total_numberof_cores",
            "memory",
        ]
        for key in keys_to_verify:
            self.assertIn(key, result)

    def test_sample_data3(self):
        result = get_all_keys(self.sample3)
        self.assertEqual(9, len(result))
        keys_to_verify = [
            "processor_details",
            "processor_name",
            "l2_cache(per_core)",
            "total_number_of_cores",
        ]
        for key in keys_to_verify:
            self.assertIn(key, result)

    def test_sample_data4(self):
        result = get_all_keys(self.sample4)
        self.assertEqual(3, len(result))
        keys_to_verify = [
            "values",
            "checks",
            "monitoring_zones"
        ]
        for key in keys_to_verify:


class TestGetOccurrence(TestCase):
    def setUp(self):
        self.sample1 = {
            "build_version": {
                "model_name": "MacBook Pro",
                "build_version": {
                    "processor_name": "Intel Core i7",
                    "processor_speed": "2.7 GHz",
                    "core_details": {
                        "build_version": "4",
                        "l2_cache(per_core)": "256 KB"
                    }
                },
                "number_of_cores": "4",
                "memory": "256 KB",
            },
            "os_details": {
                "product_version": "10.13.6",
                "build_version": "17G65"
            },
            "name": "Test",
            "date": "YYYY-MM-DD HH:MM:SS"
        }
        self.sample2 = {
            "hardware_details": {
                "model_name": "MacBook Pro",
                "processor_details": [{
                    "processor_name": "4",
                    "processor_speed": "2.7 GHz",
                    "core_details": {
                        "total_numberof_cores": "4",
                        "l2_cache(per_core)": "256 KB"
                    }
                }],
                "total_number_of_cores": "4",
                "memory": "16 GB",
            }
        }
        self.sample3 = {
            "hardware_details": {
                "model_name": "MacBook Pro",
                "processor_details": [
                    {
                        "total_number_of_cores": "4",
                        "processor_speed": "2.7 GHz",
                    },
                    {
                        "total_number_of_cores": "4",
                        "l2_cache(per_core)": "256 KB"
                    }
                ],
                "total_number_of_cores": "4",
                "memory": "16 GB",
            }
        }

    def test_sample_data1(self):
        result = get_occurrence_of_key(self.sample1, 'build_version')
        self.assertEqual(4, result)
        result = get_occurrence_of_value(self.sample1, '256 KB')
        self.assertEqual(2, result)

    def test_sample_data2(self):
        result = get_occurrence_of_key(self.sample2, 'core_details')
        self.assertEqual(1, result)
        result = get_occurrence_of_value(self.sample2, '4')
        self.assertEqual(3, result)

    def test_sample_data3(self):
        result = get_occurrence_of_key(self.sample3, 'total_number_of_cores')
        self.assertEqual(3, result)
        result = get_occurrence_of_value(self.sample3, '4')
        self.assertEqual(3, result)


if __name__ == "__main__":
    pass

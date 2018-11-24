from unittest import TestCase

from nested_lookup import nested_update, nested_delete


class BaseLookUpApi(TestCase):
    def setUp(self):
        self.sample_data1 = {
            "build_version": {
                "model_name": 'MacBook Pro',
                "build_version": {
                    "processor_name": 'Intel Core i7',
                    "processor_speed": '2.7 GHz',
                    "core_details": {
                        "build_version": '4',
                        "l2_cache(per_core)": '256 KB'
                    }
                },
                "number_of_cores": '4',
                "memory": '256 KB'
            },
            "os_details": {
                "product_version": '10.13.6',
                "build_version": '17G65'
            },
            "name": 'Test',
            "date": 'YYYY-MM-DD HH:MM:SS'
        }

        self.sample_data2 = {
            "hardware_details": {
                "model_name": 'MacBook Pro',
                "processor_details": [
                    {
                        "processor_name": 'Intel Core i7',
                        "processor_speed": '2.7 GHz'
                    },
                    {
                        "total_number_of_cores": '4',
                        "l2_cache(per_core)": '256 KB'
                    }
                ],
                "total_number_of_cores": '5',
                "memory": '16 GB'
            }
        }

        self.sample_data3 = {
            "values": [{
                "checks": [{
                    "monitoring_zones":
                    ["mzdfw", "mzfra", "mzhkg", "mziad",
                     "mzlon", "mzord", "mzsyd"]
                }]
            }]
        }


class TestNestedDelete(BaseLookUpApi):
    def test_sample_data1(self):
        result = {
            "os_details": {
                "product_version": '10.13.6'
            },
            "name": 'Test',
            "date": 'YYYY-MM-DD HH:MM:SS'
        }
        self.assertEqual(
            result, nested_delete(self.sample_data1, 'build_version')
        )

    def test_sample_data2(self):
        result = {
            "hardware_details": {
                "model_name": 'MacBook Pro',
                "total_number_of_cores": '5',
                "memory": '16 GB'
            }
        }
        self.assertEqual(
            result, nested_delete(self.sample_data2, 'processor_details')
        )

    def test_sample_data3(self):
        result = {"values": [{"checks": [{}]}]}
        self.assertEqual(
            result, nested_delete(self.sample_data3, 'monitoring_zones')
        )


class TestNestedUpdate(BaseLookUpApi):
    def test_sample_data1(self):
        result = {
            "build_version": "Test1",
            "os_details": {
                "product_version": '10.13.6',
                "build_version": 'Test1'
            },
            "name": 'Test',
            "date": 'YYYY-MM-DD HH:MM:SS'
        }
        self.assertEqual(
            result, nested_update(self.sample_data1, 'build_version', 'Test1')
        )

    def test_sample_data2(self):
        result = {
            "hardware_details": {
                "model_name": 'MacBook Pro',
                "processor_details": {
                    'test_key1': 'test_value1'
                },
                "total_number_of_cores": '5',
                "memory": '16 GB'
            }
        }
        self.assertEqual(
            result, nested_update(
                self.sample_data2, 'processor_details',
                {'test_key1': 'test_value1'}
            )
        )

    def test_sample_data3(self):
        result = {
            "values": [{
                "checks": {
                    'key1': ['value1'],
                    'key2': 'value2'
                }
            }]
        }
        self.assertEqual(
            result, nested_update(
                self.sample_data3, 'checks',
                {
                    'key1': ['value1'],
                    'key2': 'value2'
                }
            )
        )

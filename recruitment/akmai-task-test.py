import unittest
from recruitment.akamai_task import occurrence_sort


class AkamaiTaskTest(unittest.TestCase):
    def test_occurrence_sort(self):

        self.assertEqual(['1', '2', '2', '3', '3', '3', '4', '4', '4', '4'], occurrence_sort("4434343212"))


if __name__ == '__main__':
    unittest.main()

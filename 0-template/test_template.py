import os
import unittest
from template import part_one, part_two


class TestTemplate(unittest.TestCase):
    def setUp(self):
        self.test_one = "test_one.txt"
        self.test_two = "test_two.txt"

        with open(self.test_one, "w") as f:
            f.write(
                """
Hello, World!
            """.strip()
            )

        with open(self.test_two, "w") as f:
            f.write(
                """
Hello, World!
            """.strip()
            )

    def tearDown(self):
        os.remove(self.test_one)
        os.remove(self.test_two)

    def test_part_one(self):
        # Test case 1: Given example in challenge
        self.assertEqual(part_one("test_one.txt"), True)

    def test_part_two(self):
        # # Test case 1: Given example in challenge
        self.assertEqual(part_two("test_two.txt"), True)


if __name__ == "__main__":
    unittest.main()

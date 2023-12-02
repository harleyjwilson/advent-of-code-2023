import os
import unittest
from trebuchet import part_one, part_two


class TestTrebuchet(unittest.TestCase):
    def setUp(self):
        self.test_one = "test_one.txt"
        self.test_two = "test_two.txt"
        self.test_three = "test_three.txt"
        self.test_four = "test_four.txt"

        with open(self.test_one, "w") as f:
            f.write(
                """
1abc2
            """.strip()
            )

        with open(self.test_two, "w") as f:
            f.write(
                """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
            """.strip()
            )

        with open(self.test_three, "w") as f:
            f.write(
                """
two1nine
            """.strip()
            )

        with open(self.test_four, "w") as f:
            f.write(
                """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
            """.strip()
            )

    def tearDown(self):
        os.remove(self.test_one)
        os.remove(self.test_two)
        os.remove(self.test_three)
        os.remove(self.test_four)

    def test_part_one(self):
        # Test case 1: First line of given example in challenge
        self.assertEqual(part_one("test_one.txt"), 12)

        # Test case 2: Given example in challenge
        self.assertEqual(part_one("test_two.txt"), 142)

    def test_part_two(self):
        # Test case 1: First line of given example in challenge
        self.assertEqual(part_two("test_three.txt"), 29)

        # Test case 2: Given example in challenge
        self.assertEqual(part_two("test_four.txt"), 281)


if __name__ == "__main__":
    unittest.main()

import os
import unittest
from cube_conundrum import part_one, part_two


class TestCubeConundrum(unittest.TestCase):
    def setUp(self):
        self.test_one = "test_one.txt"
        self.test_two = "test_two.txt"
        self.test_three = "test_three.txt"

        with open(self.test_one, "w") as f:
            f.write(
                """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
            """.strip()
            )

        with open(self.test_two, "w") as f:
            f.write(
                """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            """.strip()
            )

        with open(self.test_three, "w") as f:
            f.write(
                """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
            """.strip()
            )

    def tearDown(self):
        os.remove(self.test_one)
        os.remove(self.test_two)
        os.remove(self.test_three)

    def test_part_one(self):
        # Test case 1: Given example in challenge
        self.assertEqual(part_one("test_one.txt"), 8)

    def test_part_two(self):
        # Test case 1: First line of given example in challenge
        self.assertEqual(part_two("test_two.txt"), 48)

        # Test case 2: Given example in challenge
        self.assertEqual(part_two("test_three.txt"), 2286)


if __name__ == "__main__":
    unittest.main()

import unittest
from main import symmetrical

def main():
    unittest.main()

class TestSymmetrical(unittest.TestCase):

    # Assumes width = 5 and height = 5
    def test_odd_box_symmetrical(self):
        positions = [(0, 0), (4, 0), (1, 1), (3,1), (2,2)]
        self.assertTrue(symmetrical(positions, 5, 5))
    
    def test_odd_box_asymmetrical(self):
        positions = [(0, 0), (4, 0), (1, 1), (3,2), (2,2)]
        self.assertFalse(symmetrical(positions, 5, 5))

    # Assumes width = 6 and height = 6
    def test_even_box_symmetrical(self):
        positions = [(0, 0), (5, 0), (1, 1), (4, 1), (2, 1), (3, 1)]
        self.assertTrue(symmetrical(positions, 6, 6))

    def test_even_box_asymmetrical(self):
        positions = [(0, 0), (5, 0), (1, 1), (4, 0), (2, 1), (3, 1)]
        self.assertFalse(symmetrical(positions, 6, 6))

if __name__ == "__main__":
    main()

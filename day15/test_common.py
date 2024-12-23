import unittest
from utils import get_initial_robot_pos

class TestGetInitialPosition(unittest.TestCase):

    def test_initial_pos_not_found(self):
    
        w = 5
        h = 5
        a = [
            "#####",
            "#.O.#",
            "#O.@#",
            "#.O.#",
            "#####"
        ]

        pos = get_initial_robot_pos(a, w, h)

        self.assertTupleEqual(pos, (3, 2))

    def test_initial_pos_found(self):
        w = 5
        h = 5
        a = [
            "#####",
            "#.O.#",
            "#O..#",
            "#.O.#",
            "#####"
        ]
    
        pos = get_initial_robot_pos(a, w, h)

        self.assertTupleEqual(pos, (-1, -1)) 
 

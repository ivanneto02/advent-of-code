import unittest
from utils import widen_state
from utils import wide_move_up
from utils import wide_move_left
from utils import wide_move_down
from utils import wide_move_right

# These should be straightforward because we cannot influence
# other boxes
class TestWideMoveLeft(unittest.TestCase):

    def test_cannot_move_bounds(self):

        a = [
            "##########",
            "##@.....##",
            "##[]....##",
            "##..[]..##",
            "##....[]##",
            "##########"
        ]

        expected = [
            "##########",
            "##@.....##",
            "##[]....##",
            "##..[]..##",
            "##....[]##",
            "##########"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (2, 1)

        b, npos = wide_move_left(a, pos)

        self.assertEqual(pos, npos)
        self.assertEqual(b, expected)
    
    def test_cannot_move_boxes(self):
        a = [
            "##########",
            "##[][]@.##",
            "##[]....##",
            "##..[]..##",
            "##....[]##",
            "##########"
        ]

        expected = [
            "##########",
            "##[][]@.##",
            "##[]....##",
            "##..[]..##",
            "##....[]##",
            "##########"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (6, 1)

        b, npos = wide_move_left(a, pos)

        self.assertEqual(pos, npos)
        self.assertEqual(b, expected)
    
    def test_simple_move(self):
        a = [
            "##########",
            "##..@...##",
            "##[]....##",
            "##..[]..##",
            "##....[]##",
            "##########"
        ]

        expected = [
            "##########",
            "##.@....##",
            "##[]....##",
            "##..[]..##",
            "##....[]##",
            "##########"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (4, 2)

        b, npos = wide_move_left(a, pos)

        self.assertEqual(npos, (3,1))
        self.assertEqual(b, expected)
    
    # TODO
    def test_move_boxes(self):
        a = [
            "##########",
            "##@.....##",
            "##[]....##",
            "##..[]..##",
            "##....[]##",
            "##########"
        ]

        expected = [
            "##########",
            "##@.....##",
            "##[]....##",
            "##..[]..##",
            "##....[]##",
            "##########"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (2, 2)

        b, npos = wide_move_left(a, pos)

        self.assertEqual(pos, npos)
        self.assertEqual(b, expected)

# These should be straightforward because we cannot influence
# other boxes
class TestWideMoveUp(unittest.TestCase):

    def test_cannot_move_bounds(self):
        None
    
    def test_cannot_move_boxes(self):
        None

    def test_simple_move(self):
        None

    def test_move_boxes(self):
        None

class TestWideMoveRight(unittest.TestCase):
    None

class TestWideMoveDown(unittest.TestCase):
    None

class TestWidenState(unittest.TestCase):
    def test_widen_state(self):
        a = [
            "#####",
            "#...#",
            "#O..#",
            "#.O.#",
            "#.@O#",
            "#####"
        ]

        expected = [
            "##########",
            "##......##",
            "##[]....##",
            "##..[]..##",
            "##..@.[]##",
            "##########"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        w = 5
        h = 6

        b, nw, nh = widen_state(a, w, h)

        self.assertEqual(nw, 10)
        self.assertEqual(nh, 12)
        self.assertEqual(b, expected)

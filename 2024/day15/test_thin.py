import unittest
from utils import move_left
from utils import move_up
from utils import move_right
from utils import move_down

class TestMoveDown(unittest.TestCase):

    def test_cannot_move_bounds(self):

        a = [
            "#####",
            "#.O.#",
            "#...#",
            "#@O.#",
            "#####"
        ]

        expected = [
            "#####",
            "#.O.#",
            "#...#",
            "#@O.#",
            "#####"
        ]
    
        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (1,3)
        
        b, newpos = move_down(a, pos)

        self.assertEqual(pos, newpos)
        self.assertEqual(b, expected)

    def test_cannot_move_boxes(self):
        a = [
            "#####",
            "#@OO#",
            "#OO.#",
            "#OO.#",
            "#####"
        ]

        expected = [
            "#####",
            "#@OO#",
            "#OO.#",
            "#OO.#",
            "#####"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (1,1)
        
        b, newpos = move_down(a, pos)
        
        self.assertEqual(pos, newpos)
        self.assertEqual(b, expected)

    def test_can_move_simple(self):
        a = [
            "#####",
            "#@O.#",
            "#...#",
            "#.O.#",
            "#####"
        ]

        expected = [
            "#####",
            "#.O.#",
            "#@..#",
            "#.O.#",
            "#####"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (1,1)
        
        b, newpos = move_down(a, pos)

        self.assertEqual(newpos, (1,2))
        self.assertEqual(b, expected)

    def test_can_move_boxes(self):
        a = [
            "#####",
            "#@O.#",
            "#O.O#",
            "#.O.#",
            "#####"
        ]

        expected = [
            "#####",
            "#.O.#",
            "#@.O#",
            "#OO.#",
            "#####"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (1,1)
        
        b, newpos = move_down(a, pos)

        self.assertEqual(newpos, (1,2))
        self.assertEqual(b, expected)

class TestMoveRight(unittest.TestCase):

    def test_cannot_move_bounds(self):

        a = [
            "#####",
            "#.O.#",
            "#..@#",
            "#.O.#",
            "#####"
        ]

        expected = [
            "#####",
            "#.O.#",
            "#..@#",
            "#.O.#",
            "#####"
        ]
    
        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (3,2)
        
        b, newpos = move_right(a, pos)

        self.assertEqual(pos, newpos)
        self.assertEqual(b, expected)

    def test_cannot_move_boxes(self):
        a = [
            "#####",
            "#.OO#",
            "#@OO#",
            "#.O.#",
            "#####"
        ]

        expected = [
            "#####",
            "#.OO#",
            "#@OO#",
            "#.O.#",
            "#####"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (1,2)
        
        b, newpos = move_right(a, pos)
        
        self.assertEqual(pos, newpos)
        self.assertEqual(b, expected)

    def test_can_move_simple(self):
        a = [
            "#####",
            "#.O.#",
            "#@..#",
            "#.O.#",
            "#####"
        ]

        expected = [
            "#####",
            "#.O.#",
            "#.@.#",
            "#.O.#",
            "#####"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (1,2)
        
        b, newpos = move_right(a, pos)

        self.assertEqual(newpos, (2,2))
        self.assertEqual(b, expected)

    def test_can_move_boxes(self):
        a = [
            "#####",
            "#.OO#",
            "#@O.#",
            "#.O.#",
            "#####"
        ]

        expected = [
            "#####",
            "#.OO#",
            "#.@O#",
            "#.O.#",
            "#####"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (1,2)
        
        b, newpos = move_right(a, pos)

        self.assertEqual(newpos, (2,2))
        self.assertEqual(b, expected)

class TestMoveUp(unittest.TestCase):

    def test_cannot_move_bounds(self):

        a = [
            "#####",
            "#@O.#",
            "#...#",
            "#.O.#",
            "#####"
        ]

        expected = [
            "#####",
            "#@O.#",
            "#...#",
            "#.O.#",
            "#####"
        ]
    
        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (1,1)
        
        b, newpos = move_up(a, pos)

        self.assertEqual(pos, newpos)
        self.assertEqual(b, expected)

    def test_cannot_move_boxes(self):
        a = [
            "#####",
            "#.OO#",
            "#OO@#",
            "#.O.#",
            "#####"
        ]

        expected = [
            "#####",
            "#.OO#",
            "#OO@#",
            "#.O.#",
            "#####"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (3,2)
        
        b, newpos = move_up(a, pos)
        
        self.assertEqual(pos, newpos)
        self.assertEqual(b, expected)

    def test_can_move_simple(self):
        a = [
            "#####",
            "#.O.#",
            "#..@#",
            "#.O.#",
            "#####"
        ]

        expected = [
            "#####",
            "#.O@#",
            "#...#",
            "#.O.#",
            "#####"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (3,2)
        
        b, newpos = move_up(a, pos)

        self.assertEqual(newpos, (3,1))
        self.assertEqual(b, expected)

    def test_can_move_boxes(self):
        a = [
            "#####",
            "#.O.#",
            "#O.O#",
            "#.O@#",
            "#####"
        ]

        expected = [
            "#####",
            "#.OO#",
            "#O.@#",
            "#.O.#",
            "#####"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (3,3)
        
        b, newpos = move_up(a, pos)

        self.assertEqual(newpos, (3,2))
        self.assertEqual(b, expected)

class TestMoveLeft(unittest.TestCase):

    def test_cannot_move_bounds(self):

        a = [
            "#####",
            "#.O.#",
            "#@..#",
            "#.O.#",
            "#####"
        ]

        expected = [
            "#####",
            "#.O.#",
            "#@..#",
            "#.O.#",
            "#####"
        ]
    
        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (1,2)
        
        b, newpos = move_left(a, pos)

        self.assertEqual(pos, newpos)
        self.assertEqual(b, expected)

    def test_cannot_move_boxes(self):
        a = [
            "#####",
            "#.O.#",
            "#OO@#",
            "#.O.#",
            "#####"
        ]

        expected = [
            "#####",
            "#.O.#",
            "#OO@#",
            "#.O.#",
            "#####"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (3,2)
        
        b, newpos = move_left(a, pos)
        
        self.assertEqual(pos, newpos)
        self.assertEqual(b, expected)

    def test_can_move_simple(self):
        a = [
            "#####",
            "#.O.#",
            "#..@#",
            "#.O.#",
            "#####"
        ]

        expected = [
            "#####",
            "#.O.#",
            "#.@.#",
            "#.O.#",
            "#####"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (3,2)
        
        b, newpos = move_left(a, pos)

        self.assertEqual(newpos, (2,2))
        self.assertEqual(b, expected)

    def test_can_move_boxes(self):
        a = [
            "#####",
            "#.O.#",
            "#.O@#",
            "#.O.#",
            "#####"
        ]

        expected = [
            "#####",
            "#.O.#",
            "#O@.#",
            "#.O.#",
            "#####"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (3,2)
        
        b, newpos = move_left(a, pos)

        self.assertEqual(newpos, (2,2))
        self.assertEqual(b, expected)

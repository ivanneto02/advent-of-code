import unittest
from utils import widen_state
from utils import wide_move_up
from utils import wide_move_left
from utils import wide_move_down
from utils import wide_move_right
from utils import propagate_push_up

class TestPropagation(unittest.TestCase):

    def test_propagation_cannot_move_1(self):
        a = [
            "########",
            "##..[]##",
            "##.[].##",
            "##[]..##",
            "########"
        ]

        box_pos = (2,3)

        a = [list(x) for x in a]

        self.assertEqual(propagate_push_up(a, box_pos), 0)

    def test_propagation_cannot_move_2(self):
        a = [
            "########",
            "##[]..##",
            "##.[].##",
            "##..[]##",
            "########"
        ]

        box_pos = (4,3)

        a = [list(x) for x in a]

        self.assertEqual(propagate_push_up(a, box_pos), 0)

    def test_propagation_cannot_move_3(self):
        a = [
            "########",
            "##[][]##",
            "##.[].##",
            "##.[].##",
            "########"
        ]

        box_pos = (3,3)

        a = [list(x) for x in a]

        self.assertEqual(propagate_push_up(a, box_pos), 0)
    
    def test_propagation_cannot_move_4(self):
        a = [
            "########",
            "##..[]##",
            "##.[].##",
            "##.[].##",
            "########"
        ]

        box_pos = (3,3)

        a = [list(x) for x in a]

        self.assertEqual(propagate_push_up(a, box_pos), 0)

    def test_propagation_cannot_move_5(self):
        a = [
            "########",
            "##[]..##",
            "##.[].##",
            "##.[].##",
            "########"
        ]

        box_pos = (3,3)

        a = [list(x) for x in a]

        self.assertEqual(propagate_push_up(a, box_pos), 0)

    def test_propagation_cannot_move_6(self):
        a = [
            "########",
            "##[]#.##",
            "##.[].##",
            "##.[].##",
            "########"
        ]

        box_pos = (3,3)

        a = [list(x) for x in a]

        self.assertEqual(propagate_push_up(a, box_pos), 0)

    def test_propagation_cannot_move_7(self):
        a = [
            "########",
            "##..#.##",
            "##[][]##",
            "##.[].##",
            "########"
        ]

        box_pos = (3,3)

        a = [list(x) for x in a]

        self.assertEqual(propagate_push_up(a, box_pos), 0)

    def test_propagation_cannot_move_8(self):
        a = [
            "########",
            "##[]..##",
            "##[][]##",
            "##.[].##",
            "########"
        ]

        box_pos = (3,3)

        a = [list(x) for x in a]

        self.assertEqual(propagate_push_up(a, box_pos), 0)

    def test_propagation_can_move_1(self):
        a = [
            "########",
            "##....##",
            "##[][]##",
            "##.[].##",
            "########"
        ]

        box_pos = (3,3)

        a = [list(x) for x in a]

        self.assertEqual(propagate_push_up(a, box_pos), 1)

    def test_propagation_can_move_2(self):
        a = [
            "########",
            "##....##",
            "##..[]##",
            "##.[].##",
            "########"
        ]

        box_pos = (3,3)

        a = [list(x) for x in a]

        self.assertEqual(propagate_push_up(a, box_pos), 1)

    def test_propagation_can_move_3(self):
        a = [
            "########",
            "##....##",
            "##[]..##",
            "##.[].##",
            "########"
        ]

        box_pos = (3,3)

        a = [list(x) for x in a]

        self.assertEqual(propagate_push_up(a, box_pos), 1)

    def test_propagation_can_move_4(self):
        a = [
            "########",
            "##[]..##",
            "##..[]##",
            "##.[].##",
            "########"
        ]

        box_pos = (3,3)

        a = [list(x) for x in a]

        self.assertEqual(propagate_push_up(a, box_pos), 1)

    def test_propagation_can_move_5(self):
        a = [
            "########",
            "##..[]##",
            "##[]..##",
            "##.[].##",
            "########"
        ]

        box_pos = (3,3)

        a = [list(x) for x in a]

        self.assertEqual(propagate_push_up(a, box_pos), 1)

    def test_propagation_can_move_6(self):
        a = [
            "########",
            "##....##",
            "##.[].##",
            "##.[].##",
            "########"
        ]

        box_pos = (3,3)

        a = [list(x) for x in a]

        self.assertEqual(propagate_push_up(a, box_pos), 1)



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

        pos = (4, 1)

        b, npos = wide_move_left(a, pos)

        self.assertEqual(npos, (3,1))
        self.assertEqual(b, expected)
    
    def test_move_boxes(self):
        a = [
            "##########",
            "##[].[]@##",
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

        pos = (7, 1)

        b, npos = wide_move_left(a, pos)

        self.assertEqual(npos, (6, 1))
        self.assertEqual(b, expected)

# These should be straightforward because we cannot influence
# other boxes
class TestWideMoveUp(unittest.TestCase):

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

        b, npos = wide_move_up(a, pos)

        self.assertEqual(pos, npos)
        self.assertEqual(b, expected)
    
    def test_cannot_move_boxes_1(self):
        a = [
            "##########",
            "##[][]..##",
            "##[]@...##",
            "##..[]..##",
            "##....[]##",
            "##########"
        ]

        expected = [
            "##########",
            "##[][]..##",
            "##[]@...##",
            "##..[]..##",
            "##....[]##",
            "##########"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (4, 2)

        b, npos = wide_move_up(a, pos)

        self.assertEqual(pos, npos)
        self.assertEqual(b, expected)
   
    def test_cannot_move_boxes_2(self):
        a = [
            "##########",
            "##[][]..##",
            "##[].@..##",
            "##..[]..##",
            "##....[]##",
            "##########"
        ]

        expected = [
            "##########",
            "##[][]..##",
            "##[].@..##",
            "##..[]..##",
            "##....[]##",
            "##########"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (5, 2)

        b, npos = wide_move_up(a, pos)

        self.assertEqual(pos, npos)
        self.assertEqual(b, expected)

    def test_simple_move(self):
        a = [
            "##########",
            "##[][]..##",
            "##[]..@.##",
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

        pos = (6, 2)

        b, npos = wide_move_up(a, pos)

        self.assertEqual(npos, (6, 1))
        self.assertEqual(b, expected)
   
    def test_cannot_move_boxes_3(self):
        a = [
            "##########",
            "##[][]..##",
            "##[]....##",
            "##.[]...##",
            "##.@..[]##",
            "##########"
        ]

        expected = [
            "##########",
            "##[][]..##",
            "##[]....##",
            "##.[]...##",
            "##.@..[]##",
            "##########"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (3, 4)

        b, npos = wide_move_up(a, pos)

        self.assertEqual(pos, npos)
        self.assertEqual(b, expected)

    def test_cannot_move_boxes_4(self):
        a = [
            "##########",
            "##[][]..##",
            "##[]....##",
            "##.[]...##",
            "##..@.[]##",
            "##########"
        ]

        expected = [
            "##########",
            "##[][]..##",
            "##[]....##",
            "##.[]...##",
            "##..@.[]##",
            "##########"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (4, 4)

        b, npos = wide_move_up(a, pos)

        self.assertEqual(pos, npos)
        self.assertEqual(b, expected)

    def test_move_boxes_1(self):
        a = [
            "##########",
            "##[].[].##",
            "##[]....##",
            "##..[]..##",
            "##..@.[]##",
            "##########"
        ]

        expected = [
            "##########",
            "##[].[].##",
            "##[][]..##",
            "##..@...##",
            "##....[]##",
            "##########"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (4, 4)

        b, npos = wide_move_up(a, pos)

        self.assertEqual(npos, (4, 3))
        self.assertEqual(b, expected)

    def test_move_boxes_2(self):
        a = [
            "##########",
            "##[].[].##",
            "##[]....##",
            "##..[]..##",
            "##...@[]##",
            "##########"
        ]

        expected = [
            "##########",
            "##[].[].##",
            "##[][]..##",
            "##...@..##",
            "##....[]##",
            "##########"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (5, 4)

        b, npos = wide_move_up(a, pos)

        self.assertEqual(npos, (5, 3))
        self.assertEqual(b, expected)

    def test_move_boxes_3(self):
        a = [
           "####################",
           "##....[]....[]..[]##",
           "##............[]..##",
           "##..[][]....[]..[]##",
           "##...[].......[]..##",
           "##[]##....[]......##",
           "##[]......[]..[]..##",
           "##..[][]..@[].[][]##",
           "##........[]......##",
           "####################"
       ]

        expected = [
           "####################",
           "##....[]....[]..[]##",
           "##............[]..##",
           "##..[][]....[]..[]##",
           "##...[]...[]..[]..##",
           "##[]##....[]......##",
           "##[]......@...[]..##",
           "##..[][]...[].[][]##",
           "##........[]......##",
           "####################"
       ]


        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (10, 7)

        b, npos = wide_move_up(a, pos)

        # msg = "\n"
        # for s in b:
        #     msg += "".join(s) + "\n"

        self.assertEqual(npos, (10, 6))
        self.assertEqual(b, expected)

class TestWideMoveRight(unittest.TestCase):

    def test_cannot_move_bounds(self):

        a = [
            "##########",
            "##.....@##",
            "##[]....##",
            "##..[]..##",
            "##....[]##",
            "##########"
        ]

        expected = [
            "##########",
            "##.....@##",
            "##[]....##",
            "##..[]..##",
            "##....[]##",
            "##########"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (8, 1)

        b, npos = wide_move_right(a, pos)

        self.assertEqual(pos, npos)
        self.assertEqual(b, expected)
    
    def test_cannot_move_boxes(self):
        a = [
            "##########",
            "##[].@[]##",
            "##[]....##",
            "##..[]..##",
            "##....[]##",
            "##########"
        ]

        expected = [
            "##########",
            "##[].@[]##",
            "##[]....##",
            "##..[]..##",
            "##....[]##",
            "##########"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (5, 1)

        b, npos = wide_move_right(a, pos)

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
            "##...@..##",
            "##[]....##",
            "##..[]..##",
            "##....[]##",
            "##########"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (4, 1)

        b, npos = wide_move_right(a, pos)

        self.assertEqual(npos, (5, 1))
        self.assertEqual(b, expected)
    
    def test_move_boxes(self):
        a = [
            "##########",
            "##[]@[].##",
            "##[]....##",
            "##..[]..##",
            "##....[]##",
            "##########"
        ]

        expected = [
            "##########",
            "##[].@[]##",
            "##[]....##",
            "##..[]..##",
            "##....[]##",
            "##########"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (4, 1)

        b, npos = wide_move_right(a, pos)

        self.assertEqual(npos, (5, 1))
        self.assertEqual(b, expected)

class TestWideMoveDown(unittest.TestCase):
    def test_cannot_move_bounds(self):

        a = [
            "##########",
            "##......##",
            "##[]....##",
            "##..[]..##",
            "##@...[]##",
            "##########"
        ]

        expected = [
            "##########",
            "##......##",
            "##[]....##",
            "##..[]..##",
            "##@...[]##",
            "##########"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (2, 4)

        b, npos = wide_move_down(a, pos)

        self.assertEqual(pos, npos)
        self.assertEqual(b, expected)
    
    def test_cannot_move_boxes_1(self):
        a = [
            "##########",
            "##[][]..##",
            "##[]@...##",
            "##..[]..##",
            "##.[][].##",
            "##########"
        ]

        expected = [
            "##########",
            "##[][]..##",
            "##[]@...##",
            "##..[]..##",
            "##.[][].##",
            "##########"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (4, 2)

        b, npos = wide_move_down(a, pos)

        self.assertEqual(pos, npos)
        self.assertEqual(b, expected)
   
    def test_cannot_move_boxes_2(self):
        a = [
            "##########",
            "##[][]..##",
            "##[].@..##",
            "##..[]..##",
            "##.[][].##",
            "##########"
        ]

        expected = [
            "##########",
            "##[][]..##",
            "##[].@..##",
            "##..[]..##",
            "##.[][].##",
            "##########"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (5, 2)

        b, npos = wide_move_down(a, pos)

        self.assertEqual(pos, npos)
        self.assertEqual(b, expected)

    def test_simple_move(self):
        a = [
            "##########",
            "##[][]..##",
            "##[]..@.##",
            "##..[]..##",
            "##....[]##",
            "##########"
        ]

        expected = [
            "##########",
            "##[][]..##",
            "##[]....##",
            "##..[]@.##",
            "##....[]##",
            "##########"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (6, 2)

        b, npos = wide_move_down(a, pos)

        self.assertEqual(npos, (6, 3))
        self.assertEqual(b, expected)
   
    def test_cannot_move_boxes_3(self):
        a = [
            "##########",
            "##[][]..##",
            "##[]....##",
            "##.[].@.##",
            "##....[]##",
            "##########"
        ]

        expected = [
            "##########",
            "##[][]..##",
            "##[]....##",
            "##.[].@.##",
            "##....[]##",
            "##########"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (6, 3)

        b, npos = wide_move_down(a, pos)

        self.assertEqual(pos, npos)
        self.assertEqual(b, expected)

    def test_cannot_move_boxes_4(self):
        a = [
            "##########",
            "##[][]..##",
            "##[]....##",
            "##.[]..@##",
            "##....[]##",
            "##########"
        ]

        expected = [
            "##########",
            "##[][]..##",
            "##[]....##",
            "##.[]..@##",
            "##....[]##",
            "##########"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (7, 3)

        b, npos = wide_move_down(a, pos)

        self.assertEqual(pos, npos)
        self.assertEqual(b, expected)


    def test_move_boxes_1(self):
        a = [
            "##########",
            "##[].[].##",
            "##[]@...##",
            "##..[]..##",
            "##....[]##",
            "##########"
        ]

        expected = [
            "##########",
            "##[].[].##",
            "##[]....##",
            "##..@...##",
            "##..[][]##",
            "##########"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (4, 2)

        b, npos = wide_move_down(a, pos)

        self.assertEqual(npos, (4, 3))
        self.assertEqual(b, expected)

    def test_move_boxes_2(self):
        a = [
            "##########",
            "##[].[].##",
            "##[].@..##",
            "##..[]..##",
            "##....[]##",
            "##########"
        ]

        expected = [
            "##########",
            "##[].[].##",
            "##[]....##",
            "##...@..##",
            "##..[][]##",
            "##########"
        ]

        a = [ list(x) for x in a ]
        expected = [ list(x) for x in expected ]

        pos = (5, 2)

        b, npos = wide_move_down(a, pos)

        self.assertEqual(npos, (5, 3))
        self.assertEqual(b, expected)

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
        self.assertEqual(nh, 6)
        self.assertEqual(b, expected)

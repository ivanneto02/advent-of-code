import unittest
from test_common import TestGetInitialPosition

from test_thin import TestMoveLeft
from test_thin import TestMoveUp
from test_thin import TestMoveRight
from test_thin import TestMoveDown

from test_wide import TestWidenState
from test_wide import TestWideMoveLeft
from test_wide import TestWideMoveUp
from test_wide import TestWideMoveRight
from test_wide import TestWideMoveDown

def main():

    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner()

    # Part 1 movement
    suite.addTest(unittest.makeSuite(TestMoveLeft))
    suite.addTest(unittest.makeSuite(TestMoveUp))
    suite.addTest(unittest.makeSuite(TestMoveRight))
    suite.addTest(unittest.makeSuite(TestMoveDown))

    # Part 2 movement

    # Part 2 utility
    suite.addTest(unittest.makeSuite(TestWidenState))

    # Common
    suite.addTest(unittest.makeSuite(TestGetInitialPosition))

    runner.run(suite)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import sys, os, unittest

sys.path.insert(0, os.path.abspath(__package__) + os.path.sep + "tumbler")

from TumblerModel import TumblerModel
from TumblerController import TumblerController

model = TumblerModel()
controller = TumblerController()

class TestTumblerController(unittest.TestCase):
    def testRaise(self):
        start = model.getBaseTumbler()

        expected = [
            [ 'U', 'B', 'V', 'W', 'E' ],
            [ 'A', 'G', 'C', 'D', 'J' ],
            [ 'F', 'L', 'H', 'I', 'O' ],
            [ 'K', 'Q', 'M', 'N', 'T' ],
            [ 'P', ' ', 'R', 'S', ' ' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]

        result = controller.raiseTumbler(start)
        self.assertEqual(expected, result)

    def testLower(self):
        expected = model.getBaseTumbler()

        start = [
            [ 'U', 'B', 'V', 'W', 'E' ],
            [ 'A', 'G', 'C', 'D', 'J' ],
            [ 'F', 'L', 'H', 'I', 'O' ],
            [ 'K', 'Q', 'M', 'N', 'T' ],
            [ 'P', ' ', 'R', 'S', ' ' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]

        result = controller.lowerTumbler(start)
        self.assertEqual(expected, result)

    def testUpperLeftLowered(self):
        start = [
            [ 'U', ' ', 'V', 'W', ' ' ],
            [ 'A', 'B', 'C', 'D', 'E' ],
            [ 'F', 'G', 'H', 'I', 'J' ],
            [ 'K', 'L', 'M', 'N', 'O' ],
            [ 'P', 'Q', 'R', 'S', 'T' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]
        expected = [
            [ 'U', ' ', 'V', 'W', ' ' ],
            [ 'B', 'C', 'D', 'E', 'A' ],
            [ 'G', 'H', 'I', 'J', 'F' ],
            [ 'K', 'L', 'M', 'N', 'O' ],
            [ 'P', 'Q', 'R', 'S', 'T' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]

        result = controller.rotateLeft(start, True, False)
        self.assertEqual(expected, result)

    def testUpperLeftRaised(self):
        start = [
            [ 'U', 'B', 'V', 'W', 'E' ],
            [ 'A', 'G', 'C', 'D', 'J' ],
            [ 'F', 'L', 'H', 'I', 'O' ],
            [ 'K', 'Q', 'M', 'N', 'T' ],
            [ 'P', ' ', 'R', 'S', ' ' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]
        expected = [
            [ 'B', 'V', 'W', 'E', 'U' ],
            [ 'G', 'C', 'D', 'J', 'A' ],
            [ 'F', 'L', 'H', 'I', 'O' ],
            [ 'K', 'Q', 'M', 'N', 'T' ],
            [ 'P', ' ', 'R', 'S', ' ' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]

        result = controller.rotateLeft(start, True, True)
        self.assertEqual(expected, result)

    def testUpperRightLowered(self):
        start = [
            [ 'U', ' ', 'V', 'W', ' ' ],
            [ 'A', 'B', 'C', 'D', 'E' ],
            [ 'F', 'G', 'H', 'I', 'J' ],
            [ 'K', 'L', 'M', 'N', 'O' ],
            [ 'P', 'Q', 'R', 'S', 'T' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]
        expected = [
            [ 'U', ' ', 'V', 'W', ' ' ],
            [ 'E', 'A', 'B', 'C', 'D' ],
            [ 'J', 'F', 'G', 'H', 'I' ],
            [ 'K', 'L', 'M', 'N', 'O' ],
            [ 'P', 'Q', 'R', 'S', 'T' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]

        result = controller.rotateRight(start, True, False)
        self.assertEqual(expected, result)

    def testUpperRightRaised(self):
        start = [
            [ 'U', 'B', 'V', 'W', 'E' ],
            [ 'A', 'G', 'C', 'D', 'J' ],
            [ 'F', 'L', 'H', 'I', 'O' ],
            [ 'K', 'Q', 'M', 'N', 'T' ],
            [ 'P', ' ', 'R', 'S', ' ' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]
        expected = [
            [ 'E', 'U', 'B', 'V', 'W' ],
            [ 'J', 'A', 'G', 'C', 'D' ],
            [ 'F', 'L', 'H', 'I', 'O' ],
            [ 'K', 'Q', 'M', 'N', 'T' ],
            [ 'P', ' ', 'R', 'S', ' ' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]

        result = controller.rotateRight(start, True, True)
        self.assertEqual(expected, result)

    def testLowerLeftLowered(self):
        start = [
            [ 'U', ' ', 'V', 'W', ' ' ],
            [ 'A', 'B', 'C', 'D', 'E' ],
            [ 'F', 'G', 'H', 'I', 'J' ],
            [ 'K', 'L', 'M', 'N', 'O' ],
            [ 'P', 'Q', 'R', 'S', 'T' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]
        expected = [
            [ 'U', ' ', 'V', 'W', ' ' ],
            [ 'A', 'B', 'C', 'D', 'E' ],
            [ 'F', 'G', 'H', 'I', 'J' ],
            [ 'L', 'M', 'N', 'O', 'K' ],
            [ 'Q', 'R', 'S', 'T', 'P' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]

        result = controller.rotateLeft(start, False, False)
        self.assertEqual(expected, result)

    def testLowerLeftRaised(self):
        start = [
            [ 'U', 'B', 'V', 'W', 'E' ],
            [ 'A', 'G', 'C', 'D', 'J' ],
            [ 'F', 'L', 'H', 'I', 'O' ],
            [ 'K', 'Q', 'M', 'N', 'T' ],
            [ 'P', ' ', 'R', 'S', ' ' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]
        expected = [
            [ 'U', 'B', 'V', 'W', 'E' ],
            [ 'A', 'G', 'C', 'D', 'J' ],
            [ 'L', 'H', 'I', 'O', 'F' ],
            [ 'Q', 'M', 'N', 'T', 'K' ],
            [ 'P', ' ', 'R', 'S', ' ' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]

        result = controller.rotateLeft(start, False, True)
        self.assertEqual(expected, result)

    def testLowerRightLowered(self):
        start = [
            [ 'U', ' ', 'V', 'W', ' ' ],
            [ 'A', 'B', 'C', 'D', 'E' ],
            [ 'F', 'G', 'H', 'I', 'J' ],
            [ 'K', 'L', 'M', 'N', 'O' ],
            [ 'P', 'Q', 'R', 'S', 'T' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]
        expected = [
            [ 'U', ' ', 'V', 'W', ' ' ],
            [ 'A', 'B', 'C', 'D', 'E' ],
            [ 'F', 'G', 'H', 'I', 'J' ],
            [ 'O', 'K', 'L', 'M', 'N' ],
            [ 'T', 'P', 'Q', 'R', 'S' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]

        result = controller.rotateRight(start, False, False)
        self.assertEqual(expected, result)

    def testLowerRightRaised(self):
        start = [
            [ 'U', 'B', 'V', 'W', 'E' ],
            [ 'A', 'G', 'C', 'D', 'J' ],
            [ 'F', 'L', 'H', 'I', 'O' ],
            [ 'K', 'Q', 'M', 'N', 'T' ],
            [ 'P', ' ', 'R', 'S', ' ' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]
        expected = [
            [ 'U', 'B', 'V', 'W', 'E' ],
            [ 'A', 'G', 'C', 'D', 'J' ],
            [ 'O', 'F', 'L', 'H', 'I' ],
            [ 'T', 'K', 'Q', 'M', 'N' ],
            [ 'P', ' ', 'R', 'S', ' ' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]

        result = controller.rotateRight(start, False, True)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    inittest.main()

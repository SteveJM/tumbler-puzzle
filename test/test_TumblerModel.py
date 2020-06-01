#!/usr/bin/env python3
import sys, os, unittest

sys.path.insert(0, os.path.abspath(__package__) + os.path.sep + "tumbler")

from TumblerModel import TumblerModel

model = TumblerModel()

class TestTumblerModel(unittest.TestCase):
    def testCheckPins(self):
        zeroDelta = [
            [ 'U', ' ', 'V', 'W', ' ' ],
            [ 'A', 'B', 'C', 'D', 'E' ],
            [ 'F', 'G', 'H', 'I', 'J' ],
            [ 'K', 'L', 'M', 'N', 'O' ],
            [ 'P', 'Q', 'R', 'S', 'T' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]
        oneDelta = [
            [ 'A', ' ', 'V', 'W', ' ' ],
            [ 'P', 'Q', 'R', 'S', 'T' ],
            [ 'U', 'B', 'C', 'D', 'E' ],
            [ 'F', 'G', 'H', 'I', 'J' ],
            [ 'K', 'L', 'M', 'N', 'O' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]
        twoDelta = [
            [ 'U', ' ', 'C', 'D', ' ' ],
            [ 'F', 'G', 'H', 'I', 'J' ],
            [ 'K', 'L', 'M', 'N', 'O' ],
            [ 'A', 'B', 'V', 'W', 'E' ],
            [ 'P', 'Q', 'R', 'S', 'T' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]

        self.assertFalse(model.checkStatus(zeroDelta, 'pins', 1))
        self.assertTrue(model.checkStatus(oneDelta, 'pins', 1))
        self.assertFalse(model.checkStatus(twoDelta, 'pins', 1))
        self.assertTrue(model.checkStatus(twoDelta, 'pins', 2))

    def testCheckTop(self):
        zeroDelta = [
            [ 'U', ' ', 'V', 'W', ' ' ],
            [ 'A', 'B', 'C', 'D', 'E' ],
            [ 'F', 'G', 'H', 'I', 'J' ],
            [ 'K', 'L', 'M', 'N', 'O' ],
            [ 'P', 'Q', 'R', 'S', 'T' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]
        oneDelta = [
            [ 'U', ' ', 'V', 'W', ' ' ],
            [ 'A', 'L', 'C', 'D', 'E' ],
            [ 'K', 'B', 'M', 'N', 'O' ],
            [ 'F', 'G', 'H', 'I', 'J' ],
            [ 'P', 'Q', 'R', 'S', 'T' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]
        twoDelta = [
            [ 'U', ' ', 'H', 'W', ' ' ],
            [ 'A', 'L', 'C', 'D', 'E' ],
            [ 'K', 'B', 'M', 'N', 'O' ],
            [ 'F', 'G', 'V', 'I', 'J' ],
            [ 'P', 'Q', 'R', 'S', 'T' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]

        self.assertFalse(model.checkStatus(zeroDelta, 'top', 1))
        self.assertTrue(model.checkStatus(oneDelta, 'top', 1))
        self.assertFalse(model.checkStatus(twoDelta, 'top', 1))
        self.assertTrue(model.checkStatus(twoDelta, 'top', 2))

    def testCheckBottom(self):
        zeroDelta = [
            [ 'U', ' ', 'V', 'W', ' ' ],
            [ 'A', 'B', 'C', 'D', 'E' ],
            [ 'F', 'G', 'H', 'I', 'J' ],
            [ 'K', 'L', 'M', 'N', 'O' ],
            [ 'P', 'Q', 'R', 'S', 'T' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]
        oneDelta = [
            [ 'U', ' ', 'V', 'W', ' ' ],
            [ 'F', 'G', 'H', 'I', 'J' ],
            [ 'A', 'B', 'C', 'D', 'E' ],
            [ 'K', 'L', 'R', 'N', 'O' ],
            [ 'P', 'Q', 'M', 'S', 'T' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]
        twoDelta = [
            [ 'U', ' ', 'H', 'W', ' ' ],
            [ 'F', 'G', 'H', 'I', 'J' ],
            [ 'S', 'B', 'C', 'D', 'E' ],
            [ 'P', 'L', 'M', 'N', 'O' ],
            [ 'K', 'Q', 'R', 'A', 'T' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]

        self.assertFalse(model.checkStatus(zeroDelta, 'bottom', 1))
        self.assertTrue(model.checkStatus(oneDelta, 'bottom', 1))
        self.assertFalse(model.checkStatus(twoDelta, 'bottom', 1))
        self.assertTrue(model.checkStatus(twoDelta, 'bottom', 2))

    def testCheckAll(self):
        zeroDelta = [
            [ 'U', ' ', 'V', 'W', ' ' ],
            [ 'A', 'B', 'C', 'D', 'E' ],
            [ 'F', 'G', 'H', 'I', 'J' ],
            [ 'K', 'L', 'M', 'N', 'O' ],
            [ 'P', 'Q', 'R', 'S', 'T' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]
        twoDelta = [
            [ 'U', ' ', 'V', 'W', ' ' ],
            [ 'Q', 'B', 'C', 'D', 'E' ],
            [ 'F', 'G', 'H', 'I', 'J' ],
            [ 'K', 'L', 'M', 'N', 'O' ],
            [ 'P', 'A', 'R', 'S', 'T' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]
        threeDelta = [
            [ 'U', ' ', 'V', 'W', ' ' ],
            [ 'A', 'L', 'C', 'D', 'E' ],
            [ 'F', 'G', 'H', 'B', 'J' ],
            [ 'K', 'I', 'M', 'N', 'O' ],
            [ 'P', 'Q', 'R', 'S', 'T' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]

        self.assertFalse(model.checkStatus(zeroDelta, 'all', 1))
        self.assertTrue(model.checkStatus(twoDelta, 'all', 2))
        self.assertFalse(model.checkStatus(threeDelta, 'all', 2))
        self.assertTrue(model.checkStatus(threeDelta, 'all', 3))

#!/usr/bin/env python3
from enum import Enum
from optparse import OptionParser
import sys
from TumblerController import TumblerController
from TumblerModel import TumblerModel
from TumblerMoves import Move
from TumblerView import TumblerView

tumblerModel = TumblerModel()
tumblerController = TumblerController()
tumblerView = TumblerView()

def doMove(prevMoves, prevTumbler, prevRaised, options):
    moves = prevMoves.copy()
    if len(moves) < options.depth:
        currentMove = Move.LOWER if prevRaised else Move.RAISE
        depth = len(moves)
        lastMove = moves[depth - 1] if depth > 0 else -1
        moves.append(-1)   # Just to grow the move list
        while currentMove != Move.VOID:
            # Perform the actual moves 
            moves[depth] = currentMove
            if currentMove == Move.RAISE:
                if lastMove == Move.LOWER:
                    # Pointless doing a RAISE directly after a LOWER
                    currentMove = Move.next(currentMove) # Skip LOWER
                    currentMove = Move.next(currentMove)
                    continue
                raised = True
                tumbler = tumblerController.raiseTumbler(prevTumbler)
            elif currentMove == Move.LOWER:
                if lastMove == Move.RAISE:
                    # Pointless doing a LOWER directly after a RAISE
                    currentMove = Move.next(currentMove)
                    continue
                raised = False
                tumbler = tumblerController.lowerTumbler(prevTumbler)
            elif currentMove == Move.UPPER_LEFT:
                skip = False
                index = depth - 1
                count = 0
                while index >= 0:
                    if moves[index] == Move.UPPER_RIGHT:
                        # Pointless doing an UPPER_LEFT after an UPPER_RIGHT
                        skip = True
                        break
                    if moves[index] == Move.RAISE or moves[index] == Move.LOWER:
                        break
                    if moves[index] == Move.UPPER_LEFT:
                        count += 1
                        if count >= 2:
                            # Pointless doing three in the same direction.
                            skip = True
                            break
                    index -= 1
                if skip:
                    currentMove = Move.next(currentMove)
                    continue
                raised = prevRaised
                tumbler = tumblerController.rotateLeft(prevTumbler, True, raised)
            elif currentMove == Move.UPPER_RIGHT:
                skip = False
                index = depth - 1
                count = 0
                while index >= 0:
                    if moves[index] == Move.UPPER_LEFT:
                        # Pointless doing an UPPER_RIGHT after an UPPER_LEFT
                        skip = True
                        break
                    if moves[index] == Move.RAISE or moves[index] == Move.LOWER:
                        break
                    if moves[index] == Move.UPPER_RIGHT:
                        count += 1
                        if count >= 2:
                            # Pointless doing three in the same direction.
                            skip = True
                            break
                    index -= 1
                if skip:
                    currentMove = Move.next(currentMove)
                    continue
                raised = prevRaised
                tumbler = tumblerController.rotateRight(prevTumbler, True, raised)
            elif currentMove == Move.LOWER_LEFT:
                skip = False
                index = depth - 1
                count = 0
                while index >= 0:
                    if moves[index] == Move.LOWER_RIGHT:
                        # Pointless doing an LOWER_LEFT after an LOWER_RIGHT
                        skip = True
                        break
                    if moves[index] == Move.RAISE or moves[index] == Move.LOWER:
                        break
                    if moves[index] == Move.LOWER_LEFT:
                        count += 1
                        if count >= 2:
                            # Pointless doing three in the same direction.
                            skip = True
                            break
                    index -= 1
                if skip:
                    currentMove = Move.next(currentMove)
                    continue
                raised = prevRaised
                tumbler = tumblerController.rotateLeft(prevTumbler, False, raised)
            elif currentMove == Move.LOWER_RIGHT:
                skip = False
                index = depth - 1
                count = 0
                while index >= 0:
                    if moves[index] == Move.LOWER_LEFT:
                        # Pointless doing an LOWER_RIGHT after an LOWER_LEFT
                        skip = True
                        break
                    if moves[index] == Move.RAISE or moves[index] == Move.LOWER:
                        break
                    if moves[index] == Move.LOWER_RIGHT:
                        count += 1
                        if count >= 2:
                            # Pointless doing three in the same direction.
                            skip = True
                            break
                    index -= 1
                if skip:
                    currentMove = Move.next(currentMove)
                    continue
                raised = prevRaised
                tumbler = tumblerController.rotateRight(prevTumbler, False, raised)
            if not raised:
                noteworthy = tumblerModel.checkStatus(tumbler, options.mode, options.pieces)
                if noteworthy:
                    print("---------")
                    for i in range(len(moves)):
                        print(moves[i].name, end=", ")
                    print("\n")
                    tumblerView.printDelta(tumbler, options.mode)

            doMove(moves, tumbler, raised, options)
            currentMove = Move.next(currentMove)
            if currentMove == Move.LOWER:
                currentMove = Move.next(currentMove) # Skip


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option('-d', '--depth', dest='depth', help='maximum move depth (default 14)',
                     action='store', type='int', default=14)
    parser.add_option('-p', '--pieces', dest='pieces', help='maximum moved pieces (default 5)',
                     action='store', type='int', default=5)
    parser.add_option('-m', '--mode', dest='mode', help='Noteworthy state check mode; pins, top, bottom, or all (default all)',
                     action='store', type='str', default="all")
    (options, args) = parser.parse_args()

    moves = []
    doMove(moves, tumblerModel.getBaseTumbler(), False, options)
    sys.exit(0)

# tumbler-puzzle
This is a Python program to find move sequences to help solve the Nintendo "Ten Billion Barrel" puzzle.

The code here relates to [my blog post](https://www.silicontrenches.com/post/nintendo-tumbler-puzzle).

More details about this puzzle can be found on [Wikipedia](https://en.wikipedia.org/wiki/Nintendo_tumbler_puzzle).

## To Run
Simple download this repo and run it.

    Usage: tumbler.py [options]

    Options:
      -h, --help            show this help message and exit
      -d DEPTH, --depth=DEPTH
                            maximum move depth (default 16)
      -p PIECES, --pieces=PIECES
                            maximum moved pieces (default 5)
      -m MODE, --MODE=MODE  Noteworthy state check mode; pins, top, bottom, or all (default all)

"Depth" is the number of puzzle moves to iterate over, hint: 14 is a good number.

"Pieces" is the number of puzzle pieces to allow to have been displaces for the sequences to be noteworthy.

"mode" is the validation mode used to check for noteworthy sequences, as follows:
  "all" - All beads in puzzle.
  "pins" - The three slots in the very first row, in the completed puzzle these hold the three black breads.
  "top" - The pins as above, alng with the first row of coloured beads.
  "bottom" - The lower-most row of beads.

## Tests
There are some unit tests to validate the bead manipulation functions, these will be useful if you
want to try and optimise them further. I run the tests using VSCode.
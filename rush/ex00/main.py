from checkmate import checkmate

def main():
    board1 = """\
R...
.K..
..P.
....\
"""
    print("Board 1:", end=' ')
    checkmate(board1)
#-----------------------------------
    board2 = """\
..
.K\
"""
    print("Board 2:", end=' ')
    checkmate(board2)
#-----------------------------------
    board3 = """\
R.P.
.K..
..P.
....\
"""
    print("Board 3:", end=' ')
    checkmate(board3)
#-----------------------------------
    board4 = """\
R...
.K..
..P.Q
....\
"""
    print("Board 4:", end=' ')
    checkmate(board4)

if __name__ == "__main__":
    main()
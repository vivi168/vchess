# https://pypi.org/project/python-chess/
import chess
import chess.uci

# ranks = rows (1,2,3,4..)
# files = columns (a,b,c...)
def square(file_idx, rank_idx):
    return rank_idx*8 + file_idx


def print_board(board, unicode=True):
    for j in range(7, -1, -1):
        print('  +---+---+---+---+---+---+---+---+')
        print('{} |'.format(j+1), end='')
        for i in range(8):
            piece = board.piece_at(square(i, j))
            if piece:
                if unicode:
                    symbol = piece.unicode_symbol()
                else:
                    symbol = piece.symbol()

                print(' {} |'.format(symbol), end="")
            else:
                print('   |', end="")
        print()
    print('  +---+---+---+---+---+---+---+---+')
    print('    a   b   c   d   e   f   g   h')


board = chess.Board()

engine = chess.uci.popen_engine('./stockfish-9-64')
engine.uci()
engine.ucinewgame()
engine.position(board)

print(engine.author)
print_board(board)

if __name__ == '__main__':
    while not board.is_game_over():
        # player
        # TODO : can start as black
        moved = False
        while not moved:
            # TODO : can get hint
            # can save game
            # can quit
            # can undo move
            move = input('your move: ')
            try:
                chessMove = board.parse_uci(move)
                board.push(chessMove)
                engine.position(board)
                moved = True
                print_board(board)
            except ValueError:
                print('error')

        # engine
        print('thinking...')
        best_move, ponder_move = engine.go(movetime=2000)
        board.push(best_move)
        engine.position(board)
        print(best_move)
        print_board(board)

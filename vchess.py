# https://pypi.org/project/python-chess/
import chess
import chess.uci


board = chess.Board()

engine = chess.uci.popen_engine('./stockfish-9-64')
engine.uci()
engine.ucinewgame()
engine.position(board)

print(engine.author)
# TODO : custom board rendering
print(board)

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
                print(board)
            except ValueError:
                print('error')

        # engine
        print('thinking...')
        best_move, ponder_move = engine.go(movetime=2000)
        board.push(best_move)
        engine.position(board)
        print(best_move)
        print(board)

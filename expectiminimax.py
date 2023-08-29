import statistics
import game_logic as g
import time

def expectiminimax(game, depth, maximizing_player):
    if depth == 0 or game.game_over_check():
        return game.score
    
    if maximizing_player:
        max_eval = float('-inf')
        for move in game.possible_moves():
            new_game = game.__deepcopy__()
            new_game.move(move)
            eval = expectiminimax(new_game, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        total_eval = 0
        empty_cells = game.board.get_empty_tiles()
        for cell in empty_cells:
            new_game_2 = game.__deepcopy__()
            game.board.add_tile(2, cell[0], cell[1])  # Assume a new tile with value 2 is placed
            prob_2 = 0.9  # Probability of spawning a 2
            eval_2 = expectiminimax(new_game_2, depth - 1, True) * prob_2

            new_game_4 = game.__deepcopy__()
            game.board.add_tile(4, cell[0], cell[1])  # Assume a new tile with value 2 is placed
            prob_4 = 0.1  # Probability of spawning a 4
            eval_4 = expectiminimax(new_game_4, depth - 1, True) * prob_4

            total_eval += eval_2 + eval_4
        
        return total_eval / len(empty_cells)

def find_best_move(game, depth):
    best_move = None
    best_eval = float('-inf')
    possible_moves = game.possible_moves()
    for move in game.possible_moves():
        #Make a __deepcopy__ of the game
        game___deepcopy__ = game.__deepcopy__()
        eval = expectiminimax(game___deepcopy__, depth - 1, False)
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

if __name__ == '__main__':
    # Make a new game
    game = g.Game()
    game.setup_board()
    game.display_updated_board()
    while not game.game_over_check():
        move = find_best_move(game, 3)
        game.move(move)
        time.sleep(1000)
        game.display_updated_board()
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


board = [''] * 9
current_player = 'O' 


winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  
    [0, 4, 8], [2, 4, 6]  
]

def check_winner(board):
    for combination in winning_combinations:
        a, b, c = combination
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return 'D' if '' not in board else None

def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    if winner == 'O':
        return -1
    if winner == 'D':
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == '':
                board[i] = 'X'
                score = minimax(board, False)
                board[i] = ''
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == '':
                board[i] = 'O'
                score = minimax(board, True)
                board[i] = ''
                best_score = min(score, best_score)
        return best_score

def find_best_move():
    best_score = -float('inf')
    move = None
    for i in range(9):
        if board[i] == '':
            board[i] = 'X'
            score = minimax(board, False)
            board[i] = ''
            if score > best_score:
                best_score = score
                move = i
    return move

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/make_move', methods=['POST'])
def make_move():
    global current_player, board
    data = request.json
    index = int(data['index'])

    
    if board[index] == '' and current_player == 'O':
        board[index] = 'O'
        current_player = 'X'

        
        winner = check_winner(board)
        if winner:
            return jsonify({'winner': winner, 'board': board})

        
        ai_move = find_best_move()
        if ai_move is not None:
            board[ai_move] = 'X'
            current_player = 'O'
        
        winner = check_winner(board)
        return jsonify({'winner': winner, 'board': board})
    
    return jsonify({'board': board})

@app.route('/restart', methods=['POST'])
def restart():
    global board, current_player
    board = [''] * 9
    current_player = 'O'
    return jsonify({'board': board})

if __name__ == '__main__':
    app.run(debug=True)

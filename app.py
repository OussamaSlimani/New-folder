from flask import Flask, jsonify, request
from flask_cors import CORS  # Import Flask-CORS

import random

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Single game state
game = {
    "board": ["", "", "", "", "", "", "", "", ""],
    "current_turn": "X",
    "winner": None,
    "draw": False
}

# Helper functions
def check_winner(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != "":
            return board[condition[0]]
    return None

def is_draw(board):
    return all(cell != "" for cell in board)

def make_computer_move():
    available_positions = [i for i, cell in enumerate(game["board"]) if cell == ""]
    if not available_positions:
        return None
    return random.choice(available_positions)

# Routes
@app.route("/start_game", methods=["POST"])
def start_game():
    global game
    game = {
        "board": ["", "", "", "", "", "", "", "", ""],
        "current_turn": "X",
        "winner": None,
        "draw": False
    }
    return jsonify({"message": "Game started!"})

@app.route("/make_move", methods=["POST"])
def make_move():
    global game

    if game["winner"] or game["draw"]:
        return jsonify({"error": "Game is already over"}), 400

    data = request.json
    position = data.get("position")

    if position is None or not (0 <= position < 9):
        return jsonify({"error": "Invalid position"}), 400

    if game["board"][position] != "":
        return jsonify({"error": "Position already taken"}), 400

    # Make the player's move
    game["board"][position] = game["current_turn"]

    # Check for winner or draw
    winner = check_winner(game["board"])
    if winner:
        game["winner"] = winner
    elif is_draw(game["board"]):
        game["draw"] = True

    # Switch turn to computer
    if not game["winner"] and not game["draw"]:
        game["current_turn"] = "O"

    return jsonify({"game": game})

@app.route("/make_computer_move", methods=["POST"])
def make_computer_move_route():
    global game

    if game["winner"] or game["draw"]:
        return jsonify({"error": "Game is already over"}), 400

    if game["current_turn"] != "O":
        return jsonify({"error": "It's not the computer's turn"}), 400

    position = make_computer_move()
    if position is None:
        return jsonify({"error": "No moves left"}), 400

    # Make the computer's move
    game["board"][position] = "O"

    # Check for winner or draw
    winner = check_winner(game["board"])
    if winner:
        game["winner"] = winner
    elif is_draw(game["board"]):
        game["draw"] = True

    # Switch turn back to player
    if not game["winner"] and not game["draw"]:
        game["current_turn"] = "X"

    return jsonify({"game": game})

@app.route("/game_status", methods=["GET"])
def game_status():
    return jsonify({"game": game})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

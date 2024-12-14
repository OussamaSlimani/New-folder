## **API Endpoints for X O**

### **1. Start a New Game**

- **Endpoint**: `/start_game`
- **Method**: `POST`
- **Description**: Resets the game to its initial state.
- **Response**:
  ```json
  {
    "message": "Game started!"
  }
  ```

### **2. Make a Move**

- **Endpoint**: `/make_move`
- **Method**: `POST`
- **Description**: Makes a move on the board.
- **Request Body**:

  ```json
  {
    "position": <index>
  }
  ```

  - `position`: The index of the cell to mark (0 to 8, left to right, top to bottom).

- **Responses**:
  - On Success:
    ```json
    {
      "game": {
        "board": ["X", "", "", "", "", "", "", "", ""],
        "current_turn": "O",
        "winner": null,
        "draw": false
      }
    }
    ```
  - On Invalid Position:
    ```json
    {
      "error": "Invalid position"
    }
    ```
  - If the Game is Over:
    ```json
    {
      "error": "Game is already over"
    }
    ```

### **3. Get Game Status**

- **Endpoint**: `/game_status`
- **Method**: `GET`
- **Description**: Retrieves the current state of the game.
- **Response**:
  ```json
  {
    "game": {
      "board": ["X", "", "", "", "", "", "", "", ""],
      "current_turn": "O",
      "winner": null,
      "draw": false
    }
  }
  ```

---

## **Game Board Representation**

The board is represented as an array of 9 elements, with indices mapped as follows:

| Index | Cell          |
| ----- | ------------- |
| 0     | Top-Left      |
| 1     | Top-Center    |
| 2     | Top-Right     |
| 3     | Middle-Left   |
| 4     | Middle-Center |
| 5     | Middle-Right  |
| 6     | Bottom-Left   |
| 7     | Bottom-Center |
| 8     | Bottom-Right  |

---

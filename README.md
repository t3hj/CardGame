# Two-Player Card Game

### Overview
This is a Python-based two-player card game where players compete to win rounds based on the values and colors of their cards. The game determines a winner by comparing each card's number or color hierarchy, and keeps track of scores and game history using external files.

### Features
- **User Authentication**: Validates both players' details.
- **Card Game Logic**: Players compete based on card numbers and colors:
  - If card numbers are equal, colors follow a hierarchy: yellow > red > black.
- **Winner Determination**: The player with the most cards at the end wins.
- **External File Storage**: Winner details, top 5 players, and their cards and scores are stored in separate files.

### How to Play
1. Input player details.
2. Each player is dealt 15 cards.
3. Compare cards each round based on number and color.
4. The player who wins the most rounds is declared the winner.

### File Structure
- `winner.txt`: Stores current game winner’s details.
- `leaderboard.txt`: Stores the top 5 players' names and scores.
- `cards.txt`: Stores the cards of the players.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/t3hj/CardGame.git
   ```
2. Navigate to the project directory:
   ```bash
   cd CardGame
   ```
3. Run the program:
   ```bash
   python main.py
   ```

### Future Improvements
- Add a graphical user interface (GUI) for easier interaction.
- Include more card types or special abilities.
- Implement multiplayer mode over a network.

### Contributing
Feel free to submit a pull request if you'd like to contribute!

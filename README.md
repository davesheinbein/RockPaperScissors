# Rock Paper Scissors

## Project Overview

The Rock, Paper, Scissors game serves as an engaging way to explore the fundamentals of artificial intelligence and game theory. In this project, you will implement strategies for a player bot to effectively compete against predefined opponent bots. Each bot employs different tactics, allowing for a diverse range of gameplay experiences. The challenge lies in analyzing the opponents' behavior and adapting your strategy to outsmart them consistently.

This project is part of the [FreeCodeCamp machine learning with Python Certification](https://www.freecodecamp.org/learn/machine-learning-with-python). The goal of this project is to create a Rock, Paper, Scissors game where your program competes against four different bots, winning at least 60% of the games in each match.

View the project requirements here: [Rock Paper Scissors project](https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/rock-paper-scissors).

## Table of Contents

- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Game Logic](#game-logic)
- [Contributing](#contributing)
- [License](#license)

## Technologies Used

- Python
- Unittest for testing
- FreeCodeCamp for project requirements and certification

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/davesheinbein/RockPaperScissors.git
   ```
2. Navigate to the project directory:
   ```bash
   cd RockPaperScissors
   ```
3. Install any necessary dependencies (if applicable).

## Usage

To play the game against the bots, run the following command:

```bash
python main.py
```

This will execute the main game loop, playing the game against the specified bots and showing the results.

### Running Tests

To run the unit tests, you can uncomment the line in `main.py`:

```python
# main(module='test_module', exit=False)
```

Then, run the main script:

```bash
python main.py
```

## Game Logic

The game is played according to the standard rules:
- Rock (R) beats Scissors (S)
- Scissors (S) beats Paper (P)
- Paper (P) beats Rock (R)

The player function implements a strategy to counter the bots based on their previous moves.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

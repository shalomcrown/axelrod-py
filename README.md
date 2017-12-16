# axelrod-py
h2. Reproduction of Robert Axelrod's first game theory simulation in Python

The idea is to pit different algorithms against eac other in an interative prisoner's dilemma. 
Each pair of algorithms is played 1000 times consecutively. Algorithms are also played against themselves.
After each run, a list of scores is printed out.


To add an algorithm, simply create a Python file containing a function Play that accepts two parameters:
* The other player's previous move (0:Cooperate, 1:Cheat, None:Starting new game)
* You payoff from the previous round of None if starting a new game
The function should return 0 for cooperation, 1 for cheating.

Place the Python file in the 'implementations' sub-folder, and run the main program.

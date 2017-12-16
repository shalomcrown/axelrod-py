# axelrod-py
Reproduction of Robert Axelrod's first game theory simulation in Python

The idea is to pit different algorithms against each other in an iterative prisoner's dilemma. 
Each pair of algorithms is played 1000 times consecutively. Algorithms are also played against themselves.
After each run, a list of scores is printed out.

The program currently includes some basic algorithms including 'tit for tat' and 'random play'.

Surprisingly 'random play' currently wins by a small margin over 'tit for tat'. This may be due to a bug.

The payoff matrix is found in the top of the 'axelrod.py' file. Note that this assumes that 0 means cooperation and 1 cheating. 

To add an algorithm, simply create a Python file containing a function 'play' that accepts two parameters:
* The other player's previous move (0:Cooperate, 1:Cheat, None:Starting new game)
* You payoff from the previous round or None if starting a new game
The function should return 0 for cooperation, 1 for cheating.

Place the Python file in the 'implementations' sub-folder, and run the main program.

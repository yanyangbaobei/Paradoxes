# Paradoxes
Interesting Paradoxes and Simulations

### Monty Hall Problem
Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice? <br>
N.B.: Same as Bertrand's box paradox and Three prison problem.
#### Answer
yes, switch. The chance of picking No.2 to win a car is 2/3 and stay with No.1 to win is only 1/3. It is because the host the chance to win through No.1, No.2, No.3 are all 1/3. When you choose No.1, you get 1/3 chance to win, and No.2 together with No.3 has 2/3 chance. Now host rule out one choice for you, i.e., No.3 (he has knowledge). So the chance to win through No.2 doubles.
#### Simulation Example:
```
MT = MontyHall(10000) # specify T=10000 as number of rounds 
MT.Simulation() 
```

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


### Two Envelopes Problem
You are given two indistinguishable envelopes, each containing money, one contains twice as much as the other. You may pick one envelope and keep the money it contains. Having chosen an envelope at will, but before inspecting it, you are given the chance to switch envelopes. Should you switch?

#### The switching argument: 
Now suppose you reason as follows:
1. I denote by A the amount in my selected envelope.
2. The probability that A is the smaller amount is 1/2, and that it is the larger amount is also 1/2.
3. The other envelope may contain either 2A or A/2.
4. If A is the smaller amount, then the other envelope contains 2A.
5. If A is the larger amount, then the other envelope contains A/2.
6. Thus the other envelope contains 2A with probability 1/2 and A/2 with probability 1/2.
7. So the expected value of the money in the other envelope is: 
$$ \frac{1}{2} (2A) + \frac{1}{2} (\frac{A}{2}) = \frac{5}{4}A $$
8. This is greater than A, so I gain on average by swapping.
9. After the switch, I can denote that content by B and reason in exactly the same manner as above.
10. I will conclude that the most rational thing to do is to swap back again.
11. To be rational, I will thus end up swapping envelopes indefinitely.
12. As it seems more rational to open just any envelope than to swap indefinitely, we have a contradiction.

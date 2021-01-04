# Probability and Statistics for Engineering and the Sciences
#### Jay Devore - Eighth Edition

## Chapter Two - Probaility

- **sample space**: the set of all possible outcomes of an experiment, denoted by S.
- **event**: any subset in a sample space. Called *simple* if it consists of exactly one outcome and *compound* otherwise.
  - ex. Consider rolling a dice three times. The sample space is {111,112,113...} and the event that at least one roll is a two is {112,122,222,212..}
- **permutation**: an ordered subset
- **combinations**: an unordered subset
  
### Some definitions from set theory:
- the **complement** of A, denoted by A', is the set of all outcomes in S that are not in A. 
- the **union** of two events, denoted by <img width="40" src="./photos/devore5.png">, means all outcomes in A *or* B.
- the **intersection** of two events, denoted by <img width="40" src="./photos/devore6.png">, means all outcomes in A *and* B.
- the **null event** is the event that contains no outcomes.
  - when the intersection of two events is the null event, they are **mutually exclusive** or **disjoint**.

### Some basic properites of probability: 
- 0 <= P(A) <= 1
- P(S) = 1
- If A1, A2, A3... is a collection of disjoint events, then <img width="150" src="./photos/devore7.png">
- P(A) + P(A') = 1
- For two events: <img width="160" src="./photos/devore8.png">
  - Similarly for three events: <img width="400" src="./photos/devore9.png">

### Determining probability: 
- Interpreting probability: the ratio of occurences of event A to trials performed is called the **relative frequency** and is defined by n(A)/n.
  - As n gets arbitrarily large, the relative frequency becomes the limiting or **long-run relative frequency**, which is the interpretation of probability.
  - This doesn't mean that if the probability of an event is 10%, that 1/10 trials will cause that event, since 10 is not a long run number.
- For N **equally likely outcomes**, the probability of each outcome is 1/N
- For **ordered pairs of outcomes**, where the first event can be selected in n ways and the second event can be selected in m ways, the number of pairs possible is n*m. Still valid if events are dependent.
  - this product rule generalizes for k-tuples.
- the number of permuatations possible is given by: <img width="70" src="./photos/devore10.png">, where n is the total number of outcomes and k is the number of outcomes being chosen.
- the number of combinations possible is given by: <img width="80" src="./photos/devore11.png">
  - note that n choose n is 1 and n choose 0 is 0.

### Conditional probability: 
- the conditional probability of A given that event B has definitely occured is given by P(A|B).
  - the **prior** probability of A is P(A)
  - the **posterior** probability of A is P(A|B). Once we've gained knowledge of B, P(A) changes.
- <img width="90" src="./photos/devore12.png">
- **exhaustive** means if at least one A_i must occur.
- **law of total probability**: If events A1, A2... are mutually exclusive and exhaustive, then for some B: <img width="120" src="./photos/devore13.png">
  - a great example for this is a deck of cards. Let B be a red card and let each A_i be the card values (1,2..jack, queen...). Then P(B = red cards) = P(B|jack)P(jack) + P(B|1)P(1) + ... = 13*[(2/4)*(4/52)]
- **Bayes' Theorem**: <img width="200" src="./photos/devore14.png">

### Idependence:
- two events are independent if P(A|B) = P(A)
- two events are independent if and only if <img width="100" src="./photos/devore15.png">
  - events A1, A2, ... are **mutually independent** for every subset if <img width="200" src="./photos/devore16.png">
- if two events are mutually exclusive, they can't be independent

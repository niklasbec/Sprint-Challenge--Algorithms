#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

O(n): iterating from 0 to n^3 ----- n steps incrementing n^2 every iteration ----- n^3 = n^2 * n

b)

O(n logn): inner loop is logarithmic so log n ---- outer loop is will run n times

c)

looks like its just counting down from n, so ----> O(n)

## Exercise II

Written on the premise of n = 50, f = 32

First floor to throw an egg of = n / 2  ----> 25
Egg doesnt break, throw out all the values below 26th floor
Egg breaks, throw out all the values above 25th floor
We now have Floor 26 - 50 left
We take the middle again ------------> 38
Egg breaks we throw out all values above 37
26-37 is left, we take the median which is 31.5 rounded to 32
Egg breaks
26-32
29 Egg doesnt break
29-32
30.5 -> 31
Egg doesnt break
We now now the highest floor we can throw of without breaking the egg is floor 31
It cost us 5 eggs instead of 32

Algo: 

if n == 0:
    return 0
elif n == 1:
    return 1
else:
    middle = n / 2
    then check for break true or false and go up or down accordingly
    repeat till done

runtime complexity: O(log2 n)


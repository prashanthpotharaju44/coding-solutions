# Tuples

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

**Task**  
Given an integer, $n$, and $n$ space-separated integers as input, create a tuple, $t$, of those $n$ integers. Then compute and print the result of $hash(t)$.  

**Note:** [hash()](https://docs.python.org/3/library/functions.html#hash) is one of the functions in the `__builtins__` module, so it need not be imported.  

**Input Format**

The first line contains an integer, $n$, denoting the number of elements in the tuple.	 			
The second line contains $n$ space-separated integers describing the elements in tuple $t$.  

**Constraints**

 

**Output Format**

Print the result of $hash(t)$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-04T17:05:54.478Z  

```py
if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    x = 0x345678
    mult = 1000003
    length = len(integer_list)

    for item in integer_list:
        x = (x ^ item) * mult
        length -= 1
        mult += 82520 + length + length

    x += 97531

    x &= (1 << 64) - 1

    if x >= (1 << 63):
        x -= (1 << 64)

    if x == -1:
        x = -2

    print(x)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/python-tuples/problem)
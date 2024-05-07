0x02. Minimum Operations

The problem "Minimum Operations" involves finding the minimum number of operations required to reach a certain number from the number 1, given a set of rules.
Problem Statement:
You start with the number 1 and you can perform either of the following two operations:
1. Double the number.
2. Add one to the number.
Example:
Let's say the target number n is 10.

Starting from 1, we can double the number to get 2.
Then, we double 2 to get 4.
Next, we double 4 to get 8.
Finally, we add 1 to 8 to get 9.
Now, we double 9 to get 18.
Finally, we subtract 1 from 18 to get 10

Pseudocode:
function minOperations(n):
    operations = 0
    while n > 1:
        if n is even:
            n = n / 2
        else:
            n = n - 1
        increment operations by 1
    return operations
-------------------------------------------------
Task:
0. Minimum Operations
mandatory
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
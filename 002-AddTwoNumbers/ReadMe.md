# Explanation

# 1. Subject
You are given two __non-empty__ linked lists representing two non-negative integers. The digits are stored in __reverse order__ and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

```Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```

# 2. Solution
Here the problem is not really hard because the lists are in the correct order. That means that the first number
of the list embodies the unit, the second the tens, and so on. So we can just loop over the two lists at the same
time and compute the sum of the two numbers. Also we need to take care of the carry in the case of `number1 + number2 >= 10`. We also need to take care of the fact that one list might be smaller than the other. In this case we only need to copy the remaining elements of the non empty list __modulo the carry__.
__2 things to note__: Once we iterate through all the elements we need to take care of the carry again and add another
node `if carry == 1` with a value of `1`. at the end of our function we might need to return the created list but as
we iterated through it during our algorithm if we do that we will actually return the last node of our list... To take
care of this problem we might just define 2 lists: `mylist` which will be the list we will populate through our 
algorithm and `dummy` which will just be a list that points to the first node of `mylist`. Then at the end we can just
return `dummy.next` or `dummy` depending on how we actually initialized the `dummy` list.
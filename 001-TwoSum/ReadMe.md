# Explanation

# 1. Subject
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

```
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

# 2. Solution
the most trivial solution would be use 2 loops. For example for the first iteration we will have on our example:
+ outer loop pointer: 2
+ inner loop pointer: go through values [7, 11, 15]

At each iteration of the inner loop we add the number pointed by the outer loop with the number of the inner loop. We will
then have in the order: `2+7`, `2+11`, `2+15`. As `2+7` = `9` (= target) we can immediately returns the indices of the elements `2` and `7`. This solution works because we won't have the possibility to have `2+2` (the inner loop starts at `pointer outer loop` + 1). Moreover if we return `[pointer outer loop, pointer inner loop]` we are sure that the elements are sorted in increasing order.

Time complexity: O(n²)
Space complexity: O(1)

Well. This solution is a very naive solution of course. Could we do better? Actually the problem seek to find the sum of
2 numbers. Let `n` be the target number and let `x` and `y` be 2 numbers from the array `nums`. So we want to find the indices of  `x` and `y` in `nums` such that: `x + y = n`. But we already know `x` and `n` so the problem we want to solve is: 

find `y` such that `y = n - x` 

Hence, if we precomputed `n - x` for all `x` in nums and if we associate to each number the indice of `x` in nums,
we will have, on our example: `[7 -> 0, 2 -> 1, -2 -> 2, -6 -> 3]`

Then, we only need to iterate once through our array `nums` (these number are actually our y) and at each iteration we
check if: `y` is in our dictionary (that means we check if `y = n - x`), if this is the case then it means that there are `x` and `y` in our array `nums` such that `x + y = n`. Now we only need to return the indices. The first indices is actually the indices we get from iterating from the array `nums` and the second indice comes from our mapping.

__2 things to check__: we need not indice1 == indice2 otherwise we would have use 2 times the same number. So we need to check
that `y` is in our mapping and indice1 (that we get from iterating through our `nums` array) is different from indice2 (that we get from our mapping). The other thing we need to check is that _indice1 <= indice2_. It is the case. To prove it, let's assume by absurd that _indice2 < indice1_ then that would have mean that `y = n - x` but `x != n - y` where `y` is the number at indice2 and x the number at indice1. Of course this is false, so we just showed by absurd that _indice1 <= indice2_.

Time complexity: O(n)
Space complexity: O(n)
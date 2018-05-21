# Explanation

# 1. Subject
Given a string, find the length of the __longest substring without__ repeating characters.

```Example:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

# 2. Solution
The Naive solution would be to use 2 loops but we can do better. To see what we can do, let's work out an example:
input: `abcucjbjoap`

Let's imagine we iterate (one loop) over the string:
0. if pointer is on a: longest substring = a
1. if pointer is on b: longest substring = ab
2. if pointer is on c: longest substring = abc
3. if pointer is on u: longest substring = abcu
4. if pointer is on c: longest substring = abcu (because c is already in abcu)
5. if pointer is on j: longest substring = abcu (because len(ucj) < len(abcu))
6. if pointer is on b: longest substring = abcu or ucjb
7. if pointer is on j: longest substring = abcu or ucjb (because len(bj) < len(abcu) = len(ucjb))
8. if pointer is on o: longest substring = abcu or ucjb (because len(bjo) < len(abcu))
9. if pointer is on a: longest substring = abcu or ucjb or bjoa
10. if pointer is on p: longest substring = bjoap (because len(bjoap) > len(abcu) = len(ucjb) = len(bjoa))

This is how an human being will do to find the longest substring without repeating characters if he has to
see a character at a time (= loop through the string). So what did we actually do? We need to distinguish few cases:

+ __from 3 -> 4__ why didn't we get a longer substring? because `c` is already in the substring which we can also translate
by: because __current iteration number__ - __last iteration number we encouter `c`__ < length of `abcu` (4 - 2 < 4)
+ __from 4 -> 5__ why didn't we get a longer substring? because as we encounter a `c` previously we already know that the new candidate won't be a string beginning by `abcu`. As in the previous iteration we saw a `c` that is already in
`abcu` the next best candidate will actually be `ucj` (that is to say the next best candidate will be a substring starting at the index of `c` + 1). Here we compare `ucj` and `abcu`, `abcu` is still longer so we keep it.

That's it. The algorithm is that simple. We need to carefully update the index of the letter we encounter in our string
at the end of our algorithm each time. For example if we see `c` at iteration 2 then in our dictionary we will have
d[c] = 2. But as we iterate through our string, at iteration 4 we encounter another `c` so we set the best candidate to `uc` (s[last time we encounter `c` + 1: current_position] with current_position included!) and __then__ we update our dictionary so that d[c] = 4. Finally we compare the length of the best substring so far to the length of the best
candidate and we update it accordingly...
And we continue looping...

Time complexity: O(n)
Space complexity: O(n)
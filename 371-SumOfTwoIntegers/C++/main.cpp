class Solution {
public:
    int getSum(int a, int b) {
        /* c is the carry   
        the total is solely a + b + c
        which is nothing else then a ^ b ^ c + handle the final carry... */
        while (b != 0) {
            int c = (a & b) << 1;
            a = a ^ b;
            b = c;
        }

        return a;
    }
};
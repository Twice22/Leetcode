class Solution {
public:
    int reverse(int x) {               
        long long n = 0;
        while (x) {
            n = (x % 10) + n * 10;
            x /= 10;
        }
        
        return (n < INT_MIN || n > INT_MAX) ? 0 : n;
    }
};
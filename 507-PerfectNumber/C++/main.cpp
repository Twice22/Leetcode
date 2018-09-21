class Solution {
public:
    bool checkPerfectNumber(int num) {
        if (num <= 1) return false;
        int limit = ceil(sqrt(num));
        
        int total = 0;
        for (size_t i = 2; i < limit; ++i) {
            if (num % i == 0) total += i + num / i;
        }
        
        return total+1 == num;
    }
};
#include <string>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        size_t size = s.size();
        int overall_max = 0, max_len = 0;
        
        map<char, int> d;
        
        for(size_t i = 0; i < size; ++i) {
            if (d.count(s[i]) == 0) {
                max_len++;
            } else {
                max_len = i - d[s[i]] > max_len ? max_len + 1 : i - d[s[i]];
            }
            
            d[s[i]] = i;
            
            overall_max = max_len > overall_max ? max_len : overall_max;
        }
        
        return overall_max;
    }
};
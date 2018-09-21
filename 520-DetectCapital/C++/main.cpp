class Solution {
public:
    bool detectCapitalUse2(string word) {
        int prev_version = toupper(word[0]) == word[0] ? 1 : 0;
        
        for (size_t i = 1; i < word.size(); ++i) {
            char letter = word[i];
            int version = toupper(letter) == letter ? 1 : 0;
            if (version > prev_version || version < prev_version && i > 1) {
                return false;
            }
            prev_version = version;
        }
        return true;
    }
    
    bool detectCapitalUse(string word) {
        size_t sz = word.size();
        // if allMaj == True it means all the letters SHOULD be capitalized
        bool allMaj = (word[0] <= 'Z' and word[sz-1] <= 'Z') ? true : false;
        
        for (size_t i = 1; i < sz; ++i) {
            if (allMaj && word[i] >= 'a' || !allMaj && word[i] <= 'Z') return false;
        }
        return true;
    }
};
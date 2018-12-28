class Solution {
public:
    string toGoatLatin(string S) {
        // http://www.cplusplus.com/reference/sstream/istringstream/istringstream/
        std::istringstream is{S};
        std::string word, result, a = "a";
        set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
        while (is >> word) {
            // if not vowels rotate
            if (vowels.find(std::tolower(word[0])) == vowels.end()) {
                // http://www.cplusplus.com/reference/algorithm/rotate/?kw=rotate
                std::rotate(word.begin(), word.begin() + 1, word.end());
            }
            result += word + "ma" + a + ' ';
            a.push_back('a'); // add 'a' according to the index
        }
        
        // remove last space " "
        if (!result.empty()) result.pop_back();
        return result;
    }
};
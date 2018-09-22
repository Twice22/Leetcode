class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        string alphabet = "abcdefghijklmnopqrstuvwxyz";
        set<string> wordSet(wordList.begin(), wordList.end());
        
        if (wordSet.find(endWord) == wordSet.end()) return 0;
        
        size_t size = beginWord.size();
        set<string> curWords{beginWord};
        set<string> endWords{endWord};
        
        set<string> seen; // recall which values we have already seen
        int c = 1; // counter
        
        while (!curWords.empty()) {
            
            // use 2-end BFS
            if (curWords.size() > endWords.size()) {
                set<string> temp(endWords.begin(), endWords.end());
                endWords = curWords;
                curWords = temp;
            }
            
            set<string> nextWords;
            
            for (auto possible_word: curWords) {
                
                // change one letter of each parent word
                for (size_t i = 0; i < size; ++i) {
                    for (auto letter: alphabet) {
                        char prev = possible_word[i];
                        possible_word[i] = letter;
                        
                        // early stopping
                        if (endWords.find(possible_word) != endWords.end()) {
                            return c + 1;
                        }
                        
                        if (seen.find(possible_word) == seen.end() && wordSet.find(possible_word) != wordSet.end()) {
                            seen.insert(possible_word);
                            nextWords.insert(possible_word);
                        }
                        
                        // switch back the letter we modified
                        possible_word[i] = prev;
                    }
                }
            }
            
            // iterate BFS
            curWords = nextWords;
            c++;
            
        }
        
        return 0;        
    }
};
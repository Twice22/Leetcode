class WordDictionary {
    struct TrieNode {
        bool word = false;
        unordered_map<char, TrieNode*> children;
        
        explicit TrieNode(bool word=false, unordered_map<char, TrieNode*> children=unordered_map<char, TrieNode*> {}) :
        word(word), children(std::move(children)) {}
    };
    
    std::unique_ptr<TrieNode> root;
public:
    /** Initialize your data structure here. */
    WordDictionary() {
        root = std::make_unique<TrieNode>();
    }
    
    /** Adds a word into the data structure. */
    void addWord(string word) {
        auto current = root.get(); // get raw pointer
        for (auto letter: word) {
            if (current->children.find(letter) == current->children.end()) {
                auto child = new TrieNode;
                current->children.emplace(letter, child);
            }
            current = current->children.at(letter);
        }
        current->word = true;
    }
    
    bool recsearch(string word, TrieNode* node) {               
        if (word.size() == 0) {
            if (node->word == true)
                return true;
            else
                return false;
        }
            
        bool res = false;
        if (word[0] == '.') {
            for (auto key: node->children) {                
                res = res || recsearch(word.substr(1), node->children[key.first]);
            }
        } else if (node->children.find(word[0]) != node->children.end()) {
            res = res || recsearch(word.substr(1), node->children[word[0]]);
        }
        
        return res;
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    bool search(string word) {
        return recsearch(word, root.get());
    }
};


/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * bool param_2 = obj.search(word);
 */
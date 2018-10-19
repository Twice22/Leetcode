class Trie {
    struct TrieNode {
        bool word;
        unordered_map<char, TrieNode*> children;
        
        explicit TrieNode(bool word=false, unordered_map<char, TrieNode*> children=unordered_map<char, TrieNode*> {}) :
        word(word), children(std::move(children)) {}
    };
    
    std::unique_ptr<TrieNode> root;
    
public:
    /** Initialize your data structure here. */
    Trie() {
        root = std::make_unique<TrieNode>();
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        auto current = root.get();
        for (const auto& letter : word) {
            // if letter not in children
            if (current->children.find(letter) == current->children.end()) {
                auto child = new TrieNode;
                current->children.emplace(letter, child);
            }
            current = current->children.at(letter);
        }
        current->word = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        auto current = root.get();
        for (const auto& letter : word) {
            if (current->children.find(letter) == current->children.end()) {
                return false;
            }
            current = current->children.at(letter);
        }
        return current->word;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        auto current = root.get();
        for (const auto& letter : prefix) {
            if (current->children.find(letter) == current->children.end()) {
                return false;
            }
        current = current->children.at(letter);
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * bool param_2 = obj.search(word);
 * bool param_3 = obj.startsWith(prefix);
 */
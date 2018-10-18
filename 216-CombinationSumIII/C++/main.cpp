class Solution {
private:
    vector<vector<int>> res;

public:
    void appendCombination(int k, int n, 
                           vector<int> combination=vector<int>(),
                           int beg=1) {
        if (k == 0 && n == 0) {
            res.push_back(combination);
            return;
        }
        
        for (int i = beg; i < 10; ++i) {
            if (n - i >= 0) {
                combination.push_back(i);
                appendCombination(k-1, n-i, combination, i+1);
                combination.pop_back();
            }
        }
    }
    
    vector<vector<int>> combinationSum3(int k, int n) {
        appendCombination(k, n);
        return res;
        
    }
};
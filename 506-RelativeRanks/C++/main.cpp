class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& nums) {
        unordered_map<int, int> table;
        vector<int> copy(nums.begin(), nums.end());
        sort(nums.rbegin(), nums.rend());
        
        for(size_t i = 0; i < nums.size(); ++i) {
            table[nums[i]] = i;
        }
        
        vector<string> ranks{"Gold Medal", "Silver Medal", "Bronze Medal"};
        vector<string> res;
        
        for(size_t i = 0; i < copy.size(); ++i) {
            int n = copy[i];
            res.push_back( table[n] < 3 ? ranks[table[n]] : to_string(table[n] + 1) );
        }
        
        return res;
    }
};
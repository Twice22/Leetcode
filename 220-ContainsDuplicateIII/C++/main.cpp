class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        if (k < 0 or t < 0) {
            return false;
        }
        
        unordered_map<int, int> d;
        
        for (int i = 0; i < nums.size(); i++) {
            int n = nums[i];
            int idx = n / (t+1);
            for (int x = idx-1; x <= idx+1; x++) { // cannot use size_t x as size_t is unsigned integer
                if (d.find(x) != d.end() && abs( (long) d[x] -  (long) n) <= t) // need long to avoid overflow
                    return true;
            }
            d[idx] = n;
            if (d.size() > k) {
                d.erase(nums[i-k] / (t+1));
            }
        }
        return false;
    }
};
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int length = nums.size();
        
        // populate map
        map<int, int> d;
        for(size_t i = 0; i < length; ++i) {
                d[target-nums[i]] = i;
                //d.insert(pair<int,int>(target-nums[i], i));
            }
        
        for(size_t i = 0; i < length; ++i) {
            if (d.count(nums[i]) != 0 && d[nums[i]] != i) {
                return (vector<int>) { i, d[nums[i]]};
            }
        }
        
        return (vector<int>) {0};
    }
};
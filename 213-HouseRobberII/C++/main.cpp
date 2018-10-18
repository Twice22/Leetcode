class Solution {
public:
    int linerob(vector<int>& nums, int beg, int end) {
        if (nums.empty())
            return 0;
        
        int max_without_last = 0, max_with_last = 0;
        for (int i = beg; i < end; ++i) {
            int temp = max_with_last;
            max_with_last = max(max_without_last + nums[i], max_with_last);
            max_without_last = temp;
        }
        
        return max(max_without_last, max_with_last);
    }
    
    int rob(vector<int>& nums) {
        if (nums.empty())
            return 0;
        
        if (nums.size() <= 2)
            return nums.size() == 2 ? max(nums[0], nums[1]) : nums[0];
        
        size_t end = nums.size();        
        return max(linerob(nums, 1, end), linerob(nums, 0, end-1));
    }
};
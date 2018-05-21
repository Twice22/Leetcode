#include <limits>

using namespace std;


class Solution {
public:
    int inf = numeric_limits<int>::max();
    
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() == 0 && nums2.size() == 0) {
            return .0;
        }
        
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }
        
        int size1 = nums1.size(), size2 = nums2.size();
        int beg = 0, end = size1;
        
        while (beg <= end) {
            int mid1 = (end + beg) / 2;
            int mid2 = (size1 + size2 + 1) / 2 - mid1;
            
            int maxLeftNums1 = mid1 == 0 ? -inf : nums1[mid1-1];
            int minRightNums1 = mid1 == size1 ? inf : nums1[mid1];
            
            int maxLeftNums2 = mid2 == 0 ? -inf : nums2[mid2-1];
            int minRightNums2 = mid2 == size2 ? inf : nums2[mid2];
            
            if (maxLeftNums1 <= minRightNums2 && maxLeftNums2 <= minRightNums1) {
                if ((size1 + size2) % 2 == 0) {
                    return (double) ((max(maxLeftNums1, maxLeftNums2) +
                                  min(minRightNums1, minRightNums2)) / 2.0);
                } else {
                    return (double) (max(maxLeftNums1, maxLeftNums2));
                }
            } else if (maxLeftNums1 > minRightNums2) {
                end = mid1 - 1;
            } else {
                beg = mid1 + 1;
            }
        }
        
        return .0;
    }
};
import "math"

func ternary(condition bool, a int, b int) int {
    return (map[bool]int{true: a, false: b})[condition]
}

func ternaryOp(condition bool, a int, nums []int,  idx int) int {
    if idx >= 0 && idx < len(nums) {
        return (map[bool]int{true: a, false: nums[idx]})[condition]
    }
    return a
    
}

func min(a int, b int) int {
    return ternary(a < b, a, b)
}

func max(a int, b int) int {
    return ternary(a > b, a, b)
}

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
    if len(nums1) == 0 && len(nums2) == 0 {
        return .0
    }

    if len(nums1) > len(nums2) {
        return findMedianSortedArrays(nums2, nums1)
    }
    
    // Define infinity values
    Inf := int(math.Inf(+1)) - 1
    
    // at this point len(nums1) < len(nums2)
    size_1, size_2 := len(nums1), len(nums2)
    
    beg, end := 0, size_1
    
    for beg <= end {
        mid1 := (end + beg) / 2
        
        mid2 := (size_1 + size_2 + 1) / 2 - mid1

        maxLeftNums1 := ternaryOp(mid1 == 0, -Inf, nums1, mid1-1)
        minRightNums1 := ternaryOp(mid1 == size_1, +Inf, nums1, mid1)

        maxLeftNums2 := ternaryOp(mid2 == 0, -Inf, nums2, mid2-1)
        minRightNums2 := ternaryOp(mid2 == size_2, +Inf, nums2, mid2)
        
        if (maxLeftNums1 <= minRightNums2 && maxLeftNums2 <= minRightNums1) {
            if (size_1 + size_2) % 2 == 0 {
                return float64((max(maxLeftNums1, maxLeftNums2) +
                              min(minRightNums1, minRightNums2))) / 2.0
            } else {
                return float64(max(maxLeftNums1, maxLeftNums2))
            }
        } else if (maxLeftNums1 > minRightNums2) {
            end = mid1 - 1
        } else {
            beg = mid1 + 1
        }
    }
    
    return .0 
}
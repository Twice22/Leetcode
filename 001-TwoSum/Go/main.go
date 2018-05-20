func twoSum(nums []int, target int) []int {
    d := make(map[int]int)
    
    // initialize the map
    for idx, value := range nums {
        d[target - value] = idx
    }
    
    // browse the list
    for i, n := range nums {
        if val, ok := d[n]; ok && val != i {
            return []int{i, val}
        } 
    }

    return nil
}
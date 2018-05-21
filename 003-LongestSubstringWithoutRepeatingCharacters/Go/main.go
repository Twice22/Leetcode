func lengthOfLongestSubstring(s string) int {
    var overall_max, max_len int
    d := make(map[rune]int)
    
    for idx, letter := range s {
        if _, ok := d[letter]; !ok {
            max_len++
        } else {
            if idx - d[letter] > max_len {
                max_len++
            } else {
                max_len = idx - d[letter]
            }
        }
        
        d[letter] = idx
        
        overall_max = (map[bool]int{true: max_len, false: overall_max})[max_len > overall_max]
    }
    
    return overall_max
}
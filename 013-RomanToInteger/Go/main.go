func romanToInt(s string) int {
    d := map[rune]int{'M': 1000, 'D': 500, 'C': 100, 'L': 50,
                      'X':10, 'V': 5, 'I':1, '@': 0}
    
    var res int = 0
    prev_l := '@'
    for _, l := range s {
        if d[prev_l] < d[l] {
            res += d[l] - 2 * d[prev_l]
        } else {
            res += d[l]
        }
        prev_l = l
    }
    return res
}
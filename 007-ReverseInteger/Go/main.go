func reverse(x int) int {
    if x < 0 {
        return -reverse(-x)
    }
    
    var n int
    for x != 0 {
        n = (x % 10) + n * 10
        x /= 10
    }
    
    if n > (1 << 31) {
        return 0
    }
    
    return n
}
func isPalindrome(x int) bool {
    if x < 0 {
        return false
    }
    
    n, x_bis := 0, x
    
    for x_bis != 0 {
        r := x_bis % 10
        x_bis = x_bis / 10
        n = n * 10 + r
    }
        
    return x == n
}
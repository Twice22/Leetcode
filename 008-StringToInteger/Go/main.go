package main

import "fmt"

func min(a int, b int) int {
    if a > b {
        return b
    }
    return a
}

func max(a int, b int) int {
    if a > b {
        return a
    }
    return b
}

func myAtoi(str string) int {
    if str == "" {
        return 0
    }
    
    d := map[rune]int{'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
             '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    max_int := (1 << 31) - 1
    min_int := -(1 << 31)
    
    sign := 1
    size := len(str)
    i := 0
    
    for i < size && str[i] == ' ' {
        i++
    }
    
    if i == size {
        return 0
    }
    
    // chheck +/- sign
    if str[i] == '+' || str[i] == '-' {
        if string(str[i]) == "+" {
            sign = 1
        } else {
            sign = -1
        }
        i++
    } else if _, ok := d[rune(str[i])]; !ok {
        return 0
    }
    
    beg := i
    for i < size {
        if _, ok := d[rune(str[i])]; ok {
            i++
        } else {
            break
        }
    }
    
    number := str[beg:i]
    
    // convert to string
    res := 0
    for _, figure := range number {
        res = d[figure] + res * 10
        if res > max_int {
            break
        }
    }

    result := sign * res

    return max(min(result, max_int), min_int)
}

func main() {
    fmt.Println(myAtoi("9223372036854775808"))
}
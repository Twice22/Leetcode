package main

import "fmt"

type vrange struct {
    b int
    e  int
}

func convert(s string, numRows int) string {
    if s == "" {
        return ""
    } else if numRows == 1 {
        return s
    }
    
    result := ""
    size := len(s)
    modulo := 2 * (numRows - 1)
    
    // initialization
    var idx []int
    for i := 0; i < size; i++ {
        if i % modulo == 0 {
            idx = append(idx, i)
        }
    }
    
    var queue []vrange
    for i := 0; i < (len(idx) - 1); i++ {
        queue = append(queue, vrange{idx[i], idx[i+1]})
    }
    
    // add last tuple if exists
    if idx[len(idx) - 1] < size {
        queue = append(queue, vrange{idx[len(idx) - 1], idx[len(idx) - 1]+modulo})
    }
    
    visited := make(map[int]bool)
    for i := 0; i < size; i++ {
        visited[i] = false
    }
    
    for len(queue) != 0 {
        var new_queue []vrange
        beg, end := -1, -1
        for _, elem := range queue {
            beg, end = elem.b, elem.e
            if beg < size && !visited[beg] {
                result += string(s[beg])
                visited[beg] = true
            }
            if end < size && !visited[end] {
                result += string(s[end])
                visited[end] = true
            }
            if beg <= end {
                new_queue = append(new_queue, vrange{beg+1, end-1})
            }
        }
        queue = new_queue
    }

    return result
    
}

func main() {
    fmt.Println(convert("PAYPALISHIRING", 3))
}
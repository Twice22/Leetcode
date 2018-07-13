package main

import "fmt"

func maxArea(height []int) int {
    best_surface := 0
    min_height := 0
    
    ptr1, ptr2 := 0, len(height) - 1
    
    for ptr1 < ptr2 {
        if height[ptr1] > height[ptr2] {
            min_height = height[ptr2]
            ptr2 -= 1
        } else {
            min_height = height[ptr1]
            ptr1 += 1
        }
        
        if min_height * (ptr2 - ptr1 + 1) > best_surface {
            best_surface = min_height * (ptr2 - ptr1 + 1)
        }
    }
    
    return best_surface
}

func main() {
    fmt.Println(maxArea([]int{1,1,2,5,4,6,2,1,4}))
}
import (
    "strings"
)

func min(a int, b int) int {
    if (a > b) {
        return b
    }
    return a
}

func longestPalindrome(s string) string {
    if s == "" {
        return ""
    }
    
    // construct the string of size 2 * len(s) + 1
    // with separator
    splitted_s := strings.Split(s, "")
    
    // Note: extra special letters '@' and '#' are used here
    // to avoid having to add if conditions to check if
    // 0 < i + palindromes[i] < size because @ and # are
    // not characters present in the input string and @ != #
    // so it will break the loop in the worst situation where
    // the while loop go until either # or @
    text := "@|" + strings.Join(splitted_s, "|") + "|#"
    
    // initialize slice
    palindromes := make([]int, len(text))
    
    size := len(palindromes) - 1
    center, rightmost := 0, 0
    
    maxLength, bestPosition := 1, 1
    
    // start at 1 and end at len(palindromes) - 1 to avoid
    // looping over the extra special chars
    for i := 1; i < size; i++ {
        if i < rightmost {
            // if current index lower than rightmost index
            // (rightmost index = 2*i)
            // 2 * center - i is the symmetric of current right index i
            // by the center index center
            palindromes[i] = min(palindromes[2*center - i], rightmost - i)
        }
        
        for text[i + palindromes[i] + 1] == text[i - palindromes[i] - 1] {
            palindromes[i] += 1
        }
        
        // update maxLength and bestPosition
        if palindromes[i] > maxLength {
            maxLength = palindromes[i]
            bestPosition = i
        }
        
        // update righmost position if i + palindromes[i] greater
        if palindromes[i] + i > rightmost {
            center, rightmost = i, palindromes[i] + i
        }
    }
    
    beg := (bestPosition - maxLength) / 2
    end := beg + maxLength
    
    return s[beg:end]
    
}
func intToRoman(num int) string {
    // '' for rune, "" for string
    units := map[int]rune{1: 'I', 5: 'V', 10: 'X'}
    tenth := map[int]rune{1: 'X', 5: 'L', 10: 'C'}
    centh := map[int]rune{1: 'C', 5: 'D', 10: 'M'}
    thousands := map[int]rune{1: 'M'}
    
    d := map[int]map[int]rune{1: units, 10: tenth, 100: centh, 1000: thousands}
    
    key := 1
    var res string = ""
    
    for num > 0 {
        figure := num % 10
        num = num / 10
        
        roman_digit := ""
        for figure > 0 {
            if figure == 9 {
                roman_digit += string(d[key][1]) + string(d[key][10])
                break
            } else if figure == 4 {
                roman_digit += string(d[key][1]) + string(d[key][5])
                break
            }
                
            if figure >= 5 {
                figure -= 5
                roman_digit += string(d[key][5])
            } else {
                figure -= 1
                roman_digit += string(d[key][1])
            }
        }
        
        key *= 10
        
        res = roman_digit + res
    }
    
    return res
}
class Solution {
public:
    string convertToBase7_v1(int num) {
        if (num == 0) return "0";
        
        string res = "";
        string sign = num < 0 ? "-" : "";
        int n = abs(num);
        
        while (n > 0) {
            res = to_string(n % 7) + res;
            n /= 7;
        }
        
        return sign + res;
        
    }
    
    string convertToBase7(int num) {
      if(num < 0) return "-" + convertToBase7(-num);
      return (num / 7 > 0) ? convertToBase7(num / 7) + to_string(num % 7) : to_string(num % 7);
    }
};
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        if (s.compare("") == 0) {
            return "";
        }
        
        int length = s.size();
        int nb_position = 2 * length + 1;
        
        vector<int> palindromes(nb_position);
        
        // initialize the elements
        palindromes[0] = 0;
        palindromes[1] = 1;
        
        int rightmost = 0, center = 0;
        int maxLength = 1, bestPosition = 1;
        
        for(vector<int>::size_type i = 0; i != palindromes.size(); i++) {
            if (i < rightmost) {
                palindromes[i] = min( (int) palindromes[2*center - i], (int) (rightmost - i));
            }
            
            while (((i + palindromes[i] < nb_position) && (i - palindromes[i] > 0)) &&
                  ( ((i + palindromes[i] + 1) % 2 == 0) ||
                   (s[(i + palindromes[i] + 1) / 2] == s[(i - palindromes[i] - 1) / 2]))) {
                palindromes[i] += 1;
            }
            
            // keep track of the longest palindrome
            if (palindromes[i] > maxLength) {
                maxLength = palindromes[i];
                bestPosition = i;
            }
            
            // update righmost
            if (i + palindromes[i] > rightmost) {
                center = i;
                rightmost = i + palindromes[i];
            }
        }
        
        int beg = (bestPosition - maxLength) / 2;
        
        return s.substr(beg, maxLength);
    }
};
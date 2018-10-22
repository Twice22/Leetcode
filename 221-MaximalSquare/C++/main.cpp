class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        if (matrix.empty()) {
            return 0;
        }
        
        int h = matrix.size();
        int w = matrix[0].size();
        
        int max_area = 0;
        
        vector<vector<int>> dp(h, vector<int>(w));
        
        for (size_t i = 0; i < w; ++i) {
            dp[0][i] = 1 ? matrix[0][i] == '1': 0;
            max_area = max(max_area, dp[0][i]);
        }
        
        for (size_t i = 0; i < h; ++i) {
            dp[i][0] = 1 ? matrix[i][0] == '1': 0;
            max_area = max(max_area, dp[i][0]);
        }
        
        for (size_t y = 1; y < h; y++) {
            for (size_t x = 1; x < w; x++) {
                if (matrix[y][x] == '0') { // need single quote!
                    dp[y][x] = 0;
                } else {
                    dp[y][x] = min(min(dp[y-1][x], dp[y][x-1]), dp[y-1][x-1]) + 1;
                }
                max_area = max(max_area, dp[y][x]);
            }
        }
        
        return max_area * max_area;
        
    }
};
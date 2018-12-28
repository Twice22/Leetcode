class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
        int r = A.size(), c = A[0].size();
        for (int y = 0; y < r; y++) {
            for (int x = 0; x < std::ceil( (float) c / 2.0); x++) {
                int temp1 = A[y][x], temp2 = A[y][c-1-x];
                A[y][x] = 1-temp2;
                A[y][c-1-x] = 1-temp1;
            }
        }
        
        return A;
            
    }
};
class Solution {
public:
    vector<string> createGrid(int m, int n) {
        vector<string> grid;
        string path;
        // ....
        // ....
        // ....
        // int obsCnt = 0;
        // int free = n;
        for(int i = 0; i < m; i++) {
            if(i == 0) {
                path = string(n, '.');
                grid.push_back(path);
            }
            else {
                string r = string(n - 1, '#');
                path = r + ".";
                grid.push_back(path);
            }
        }
        return grid;
        
    }
};
class Solution
{
public:
    vector<vector<int>> floodFill(vector<vector<int>> &image, int sr, int sc, int color)
    {
        if (image[sr][sc] == color)
            return image;
        queue<vector<int>> bfs;
        vector<int> position = {sr, sc};
        bfs.push(position);
        vector<int> current;
        vector<int> next;
        int same_color = image[sr][sc];
        image[sr][sc] = color;
        int row_size = image.size();
        int col_size = image[0].size();
        int direction[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        while (!bfs.empty())
        {
            current = bfs.front();
            bfs.pop();
            for (int i = 0; i < 4; i++)
            {
                next = {current[0] + direction[i][0], current[1] + direction[i][1]};
                int next_row = next[0];
                int next_col = next[1];
                if (next_row < 0 || next_row >= row_size || next_col < 0 || next_col >= col_size) // exceed limit
                    continue;
                if (image[next[0]][next[1]] == same_color)
                {
                    bfs.push(next);
                    image[next[0]][next[1]] = color;
                }
            }
        }
        return image;
    }
};
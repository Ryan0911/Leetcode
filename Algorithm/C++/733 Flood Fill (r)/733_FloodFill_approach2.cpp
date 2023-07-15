vector<int> move(int sr, int sc, int dir)
{
    switch (dir)
    {
    case 1: // top
        return {sr - 1, sc};
    case 2: // right
        return {sr, sc + 1};
    case 3: // bottom
        return {sr + 1, sc};
    case 4: // left
        return {sr, sc - 1};
    }
    return {};
};
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
        while (!bfs.empty())
        {
            current = bfs.front();
            bfs.pop();
            for (int i = 1; i <= 4; i++)
            {
                next = move(current[0], current[1], i);
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
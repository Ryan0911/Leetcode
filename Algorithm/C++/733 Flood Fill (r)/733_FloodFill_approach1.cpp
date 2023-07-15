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
    default:
        return {};
        break;
    }
}
class Solution
{
public:
    vector<vector<int>> floodFill(vector<vector<int>> &image, int sr, int sc, int color)
    {
        queue<vector<int>> bfs;
        int size = image.size();
        vector<vector<int>> footprint;
        vector<int> temp;
        for (int i = 0; i < size; i++)
        {
            for (int j = 0; j < image[i].size(); j++)
                temp.push_back(0);
            footprint.push_back(temp);
            temp.clear();
        }
        vector<int> position = {sr, sc};
        bfs.push(position);
        vector<int> current;
        vector<int> next;
        int same_color = image[sr][sc];
        image[sr][sc] = color;
        while (!bfs.empty())
        {
            current = bfs.front();
            bfs.pop();
            footprint[current[0]][current[1]] = 1;
            for (int i = 1; i <= 4; i++)
            {
                next = move(current[0], current[1], i);
                if ((next[0] < 0 || next[0] >= image.size()) || ((next[1] < 0 || next[1] >= image[0].size())))
                    continue;
                if (image[next[0]][next[1]] == same_color && footprint[next[0]][next[1]] == 0)
                {
                    bfs.push(next);
                    image[next[0]][next[1]] = color;
                }
            }
        }
        return image;
    }
};
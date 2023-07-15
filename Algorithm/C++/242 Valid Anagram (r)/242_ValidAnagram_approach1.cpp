class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        int s_table[128] = {0};
        int t_table[128] = {0};
        int size = s.size();
        for (int i = 0; i < size; i++)
        {
            s_table[(s[i] - '0')]++;
        }
        size = t.size();
        for (int i = 0; i < size; i++)
        {
            t_table[(t[i] - '0')]++;
        }
        for (int i = 0; i < 128; i++)
            if (s_table[i] != t_table[i])
                return false;
        return true;
    }
};
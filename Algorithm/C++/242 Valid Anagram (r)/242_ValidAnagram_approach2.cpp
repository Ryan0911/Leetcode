class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        int table[128] = {0};
        int size = s.size();
        if (size != t.size())
            return false;
        for (int i = 0; i < size; i++)
        {
            table[(s[i] - '0')]++;
        }
        for (int i = 0; i < size; i++)
        {
            table[(t[i] - '0')]--;
        }
        for (int i = 0; i < 128; i++)
            if (table[i] != 0)
                return false;
        return true;
    }
};
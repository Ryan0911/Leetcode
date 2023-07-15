class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        int table[26] = {0};
        int size = s.size();
        if (size != t.size())
            return false;
        for (int i = 0; i < size; i++)
        {
            table[(s[i] - 'a')]++;
        }
        for (int i = 0; i < size; i++)
        {
            table[(t[i] - 'a')]--;
        }
        for (int i = 0; i < 26; i++)
            if (table[i] != 0)
                return false;
        return true;
    }
};
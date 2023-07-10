class Solution
{
public:
	bool isValid(string s)
	{
		map<char, char> pairs = {{')', '('}, {'}', '{'}, {']', '['}};
		stack<char> parentheses;
		int size = s.size();
		if (size % 2 != 0)
			return false;
		for (int i = 0; i < size; i++)
		{
			if (pairs.find(s[i]) == pairs.end())
			{ // 左括號
				parentheses.push(s[i]);
			}
			else
			{ // 右括號
				if (parentheses.empty() || parentheses.top() != pairs[s[i]])
					return false;
				parentheses.pop();
			}
		}
		if (parentheses.empty())
			return true;
		return false;
	}
};
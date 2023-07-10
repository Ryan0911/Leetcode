class Solution
{
public:
	bool isPalindrome(string s)
	{
		int left = 0;
		int right = s.size() - 1;
		while (left < right)
		{
			// 跳過非字母、數字的字符
			while ((s[left] < 97 || s[left] > 122) && (s[left] < 48 || s[left] > 57) && (s[left] < 65 || s[left] > 90))
			{
				if (left == right)
					return true;
				left++;
			}
			while ((s[right] < 97 || s[right] > 122) && (s[right] < 48 || s[right] > 57) && (s[right] < 65 || s[right] > 90))
			{
				if (left == right)
					return true;
				right--;
			}
			// 大寫轉小寫
			if (s[left] >= 65 && s[left] <= 90)
				s[left] += 32;
			if (s[right] >= 65 && s[right] <= 90)
				s[right] += 32;
			if (s[left] == s[right])
			{
				left++;
				right--;
			}
			else
				return false;
		}
		return true;
	}
};
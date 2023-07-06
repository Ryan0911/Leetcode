class Solution
{
public:
	vector<int> twoSum(vector<int> &nums, int target)
	{
		map<int, int> pairs;
		vector<int> ans;
		int find_target = 0;
		int size = nums.size();
		for (int i = 0; i < size; i++)
		{
			find_target = target - nums[i];
			if (pairs.find(nums[i]) == pairs.end())
			{
				pairs[find_target] = i;
			}
			else
			{
				ans.push_back(pairs[nums[i]]);
				ans.push_back(i);
				break;
			}
		}
		return ans;
	}
};
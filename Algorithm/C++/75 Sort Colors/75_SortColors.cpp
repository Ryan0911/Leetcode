class Solution
{
public:
	void sortColors(vector<int> &nums)
	{
		int size = nums.size();
		int red = 0;
		int blue = size - 1;
		int temp = 0;
		for (int i = 0; i <= blue; i++)
		{
			if (nums[i] == 0)
			{
				temp = nums[red];
				nums[red] = nums[i];
				nums[i] = temp;
				red++;
			}
			else if (nums[i] == 2)
			{
				temp = nums[blue];
				nums[blue] = nums[i];
				nums[i] = temp;
				blue--;
				i--;
			}
		}
	}
};
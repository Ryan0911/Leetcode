class Solution
{
public:
    int search(vector<int> &nums, int target)
    {
        int left = 0;
        int size = nums.size();
        int right = size - 1;
        int mid = 0;
        while (left <= right)
        {
            mid = (left + right) / 2;
            if (target == nums[mid])
            {
                return mid;
            }
            else if (target > nums[mid])
            {
                left = mid + 1;
            }
            else if (target < nums[mid])
            {
                right = mid - 1;
            }
        }
        return -1;
    }
};
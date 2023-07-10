class Solution
{
public:
	vector<vector<int>> insert(vector<vector<int>> &intervals, vector<int> &newInterval)
	{
		vector<vector<int>> output;
		int size = intervals.size();
		bool flag = false;
		for (int i = 0; i < size; i++)
		{
			if (flag == false)
			{
				if (intervals[i][1] < newInterval[0])
					output.push_back(intervals[i]);
				else if (intervals[i][0] > newInterval[1])
				{
					output.push_back(newInterval);
					output.push_back(intervals[i]);
					flag = true;
				}
				else if (intervals[i][0] <= newInterval[0] && intervals[i][1] <= newInterval[1]) // update newInterval
					newInterval[0] = intervals[i][0];
				else if (intervals[i][0] >= newInterval[0] && intervals[i][1] >= newInterval[1]) // update newInterval
					newInterval[1] = intervals[i][1];
				else if (intervals[i][0] <= newInterval[0] && intervals[i][1] >= newInterval[1]) // update newInterval
				{
					newInterval[0] = intervals[i][0];
					newInterval[1] = intervals[i][1];
				}
			}
			else
			{
				output.push_back(intervals[i]);
			}
		}
		if (flag == false)
			output.push_back(newInterval);
		return output;
	}
};
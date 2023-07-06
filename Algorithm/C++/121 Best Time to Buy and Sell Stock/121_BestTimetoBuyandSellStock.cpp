class Solution
{
public:
	int maxProfit(vector<int> &prices)
	{
		int size = prices.size();
		int max_profit = 0;
		int buy = prices[0];
		for (int i = 1; i < size; i++)
		{
			if (buy > prices[i])
				buy = prices[i];
			else if (max_profit < prices[i] - buy)
				max_profit = prices[i] - buy;
		}
		return max_profit;
	}
};
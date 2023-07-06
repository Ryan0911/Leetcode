# **121. Best Time to Buy and Sell Stock (Easy)**

## **LeetCode URL:**

> https://leetcode.com/problems/best-time-to-buy-and-sell-stock

## **Solution Date:**

> 2023/7/6

## **Problem Description:**

> 給予一個整數陣列 prices，陣列的 index i 則對應天數第 i 天，存放著第 i 天對應的股價，而此題需要找出在這段期間裡頭之**最大獲利值**。  
> **在此題中需要注意，是先買後賣**

## **Example:**

    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

## **Approach:**

> 此題主要在考 Dynamic Programming(DP)，DP 其最核心的精神就是將其答案記錄下來建表，避免大量的重複計算，用空間來換取時間。  
> 此題因其時間序列的特性，時間並不會逆著走。  
> 因此其解題方針可以朝向思考如何用一次 For Loop 走過整個陣列後就解出題目，將其想法簡單紀錄如下：

- 低買高賣，遇到更便宜的價格就將便宜價格記錄下來
- 將每一天的獲利紀錄下來，存取最大獲利值

> 因此在該題中，只需留下兩個變數進行紀錄，一個是紀錄最便宜的購買價格 buy，以及最大獲利值 max_profit，透過 for 迴圈逐一進行比較後回傳結果，如此一來即可在時間複雜度 O(N)內解決該題。

## **Code**

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

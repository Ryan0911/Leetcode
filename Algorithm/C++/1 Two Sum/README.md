# **1. Two Sum (Easy)**

## **LeetCode URL:**

> https://leetcode.com/problems/two-sum/

## **Solution Date:**

> 2023/7/6

## **Problem Description:**

> 給予一個整數陣列 nums，還有一個整數 target，需要回傳兩個陣列中的 index，而在陣列中對應於 index 的資料，兩個相加必須等於 target。
> 題目也表示，可以假設每個 input 只會有一個正解，同時也不可重複使用相同的 element

## **Example:**

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

## **Approach:**

> 這題只要利用 Hash Table 即可輕鬆解題，在 C++中可利用 map 的資料結構進行建表。  
> Hash Table 的資料結構特性為有一個 Key 和 Value，而 Key 可以想像就是存取一個陣列的 index，只是該 index 可以是字串、整數。而 Value 則是對應於 Key 底下所存放的資料，然後 Hash Table 也不需要像陣列需要宣告一個連續空間。在最糟的情況下，Hash Table 搜尋的時間複雜度為 O(n)，而理想上最好的情況是 O(1)。  
> 透過 Hash Table 的特性，我們可以依照給定的 nums 陣列，利用迴圈依序存取每個 element，最糟會在 O(n^2)的時間複雜度下解決問題，理想則是 O(n)。  
> **在每次迴圈中，首先拿 element 來搜尋 map 中是否有對應的 Key，若無，則將 target 與 element 相減做為 Key，而 Value 則是存在 nums 陣列中的 index。** > **如此一來，在一開始我們就會配對在 map 中有對應的組合可以滿足 target，若有則存入 ans 並跳出迴圈，回傳解答。**

## **Code**

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

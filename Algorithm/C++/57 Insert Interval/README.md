# **57. Insert Interval (Medium)**

## **LeetCode URL:**

> https://leetcode.com/problems/insert-interval/

## **Solution Date:**

> 2023/7/8

## **Problem Description:**

> 給予一個二維區間陣列 Intervals，其中每一個 index 裡的資料中都又分別存有一個 start 和 end 表示一個區間的開始與結束，另給予一個區間陣列 newInterval，也包含 start、end 兩個整數代表一個區間。
> 現在題目要求我們要將 newInterval 插入到 Intervals 中，其中 Intervals 要升冪排列，並且這個區間不可重疊(所以需要考慮合併陣列)

## **Example:**

    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

## **Approach:**

> 此題首要考量為 newIntervals 是否需要更新，若不需要更新，就可立即將 newIntervals 插入至回傳陣列(output)中，並將之後遍歷到的 Intervals item 一一插入至 output。  
> 此題需要考量到五個 case:
>
> > 1. 目前遍歷到的 item 區間皆小於 newInterval
> >    > 將目前的 item 直接插入 output
> > 2. 目前遍歷到的 item 區間介於 newInterval 的 start 數字之間
> >    > 將 newInterval 的 start 更新為該 item 的 start
> > 3. 目前遍歷到的 item 區間在 newInterval 的區間內
> >    > 不更新
> > 4. 目前遍歷到的 item 區間介於 newInterval 的 end 數字之間
> >    > 將 newInterval 的 end 更新為該 item 的 end
> > 5. 目前遍歷到的 item 區間超出 newInterval 的區間
> >    > 不更新，將 newInterval 插入 output，並將該 item 插入 output，此後遍歷到的每個 item 皆直接插入答案即可

## **Code**

    class Solution {
    public:
        vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
            vector<vector<int>> output;
            int size = intervals.size();
            bool flag = false;
            for (int i = 0; i < size; i++) {
                if (flag == false) {
                    if (intervals[i][1] < newInterval[0])
                        output.push_back(intervals[i]);
                    else if (intervals[i][0] > newInterval[1])
                    {
                        output.push_back(newInterval);
                        output.push_back(intervals[i]);
                        flag = true;
                    }
                    else if (intervals[i][0] <= newInterval[0] && intervals[i][1] <= newInterval[1]) //update newInterval
                        newInterval[0] = intervals[i][0];
                    else if (intervals[i][0] >= newInterval[0] && intervals[i][1] >= newInterval[1]) //update newInterval
                        newInterval[1] = intervals[i][1];
                    else if (intervals[i][0] <= newInterval[0] && intervals[i][1] >= newInterval[1]) //update newInterval
                    {
                        newInterval[0] = intervals[i][0];
                        newInterval[1] = intervals[i][1];
                    }
                }
                else {
                    output.push_back(intervals[i]);
                }
            }
            if (flag == false)
                output.push_back(newInterval);
            return output;
        }
    };

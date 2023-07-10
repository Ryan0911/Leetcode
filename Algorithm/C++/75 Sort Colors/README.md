# **75. Sort Colors (Medium)**

## **LeetCode URL:**

> https://leetcode.com/problems/sort-colors/

## **Solution Date:**

> 2023/7/7

## **Problem Description:**

> 給予一個整數陣列，裡頭只有 0, 1, 2  
> 其中 0 代表紅色、1 代表白色、2 代表藍色  
> 現在需要將這串整數陣列進行由小到大的排序

## **Example:**

    Input: nums = [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]

## **Approach:**

> 此題若要單純寫一個排序的話並不難，難就難在 Follow up 的提示，是否可用**one-pass algorithm using only constant extra space**來解題。  
> 此題會用到雙指標的概念，分別指向起始點(red)與終點(blue)，接下來將分別以會遍歷到的 item {0, 1, 2}進行討論:
>
> > 1. 紅色(0)
> >    > 與 red 指向的位置進行交換，並將 red 指標向前一格。
> > 2. 白色(1)
> >    > 不動作。
> > 3. 藍色(2)
> >    > 與 blue 指向的位置進行交換，並將 for 迴圈的指針停留原地再比較一次以及 blue 指針向後退一格。至於為何要多一步停留的原因是因為我們並不知道與 blue 指針交換來的 item 是否為 0，所以必須要再比較一次。  
> >    > 當 i 超過 blue 時即代表我們整個 item 都遍歷過了，即可以停止。

## **Code**

    class Solution {
    public:
        void sortColors(vector<int>& nums) {
            int size = nums.size();
            int red = 0;
            int blue = size - 1;
            int temp = 0;
            for (int i = 0; i <= blue; i++) {
                if (nums[i] == 0) {
                    temp = nums[red];
                    nums[red] = nums[i];
                    nums[i] = temp;
                    red++;
                }
                else if (nums[i] == 2) {
                    temp = nums[blue];
                    nums[blue] = nums[i];
                    nums[i] = temp;
                    blue--;
                    i--;
                }
            }
        }
    };

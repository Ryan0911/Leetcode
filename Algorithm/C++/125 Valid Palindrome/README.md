# **125. Valid Palindrome (Easy)**

## **LeetCode URL:**

> https://leetcode.com/problems/valid-palindrome/

## **Solution Date:**

> 2023/7/10

## **Problem Description:**

> 給予一個字串 s，現在要將 s 內所有非字母數字的字元刪除後，將大寫字母轉成小寫，並檢查 s 是否是一個回文。  
> 回文定義: 字串從左邊開始讀跟右邊開始讀的答案是一樣的即是一個回文。

## **Example:**

    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

---

    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

## **Approach:**

> 此題要用到的概念會是 ASCII TABLE(如下圖)，ASCII TABLE 讓我們可以了解一個基本字元相對應的十進制整數。

> ![ASCII TABLE](https://www.asciitable.com/asciifull.gif)

<center>reference: https://www.asciitable.com/</center>

> 首先宣告 left、right 兩個分別指向起點和終點的指標，在來比對非字母、數字的部分，若指向的字元非單字、數字則跳過，再來將大寫轉成小寫(即 A~Z 與 a~z 相隔 32 的距離，直接將大寫字元+上 32 即可)，最後才做比對字元，一路向內做夾擠比對，即可解開這題。

## **Code**

    class Solution{
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

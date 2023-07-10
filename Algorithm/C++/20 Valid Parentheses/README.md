# **20. Valid Parentheses (Easy)**

## **LeetCode URL:**

> https://leetcode.com/problems/valid-parentheses/

## **Solution Date:**

> 2023/7/10

## **Problem Description:**

> 給予一個字串 s，裡頭只有 '{', '}', '[', ']', '(', ')' 三組括號的字元組合
> 現在需要在 s 中確認這組字串是否符合括號規則

## **Example:**

    Input: s = "()[]{}"
    Output: true

---

    Input: s = "(]"
    Output: false

## **Approach:**

> 此題最核心的地方會用到 stack，先進後出的概念，以最外圍的括號來說，左括號會最早遇到，而相配對的右括號會最晚出現。因此我們可以用這個資料結構，解決這個題目。  
> 以程式碼的部分簡單講解，當遇到左括號時，直接 push 到 stack 內，而遇到右括號時，則是去看配對的右括號是否成功，若不成功則 return false，反之則將配對的括號 pop 出 stack。
> 當跑完整個迴圈以後，只要確認 stack 內是否為空，若為空則代表配對括號成雙成對，即可 return true。
> 這題一開始可以先確認 size 是否為偶數，若為奇數則代表括號不可能成對，則可以直接 return false。

## **Code**

    class Solution
    {
    public:
        bool isValid(string s)
        {
            map<char, char> pairs = {{')', '('}, {'}', '{'}, {']', '['}};
            stack<char> parentheses;
            int size = s.size();
            if (size % 2 != 0)
                return false;
            for (int i = 0; i < size; i++)
            {
                if (pairs.find(s[i]) == pairs.end())
                { // 左括號
                    parentheses.push(s[i]);
                }
                else
                { // 右括號
                    if (parentheses.empty() || parentheses.top() != pairs[s[i]])
                        return false;
                    parentheses.pop();
                }
            }
            if (parentheses.empty())
                return true;
            return false;
        }
    };

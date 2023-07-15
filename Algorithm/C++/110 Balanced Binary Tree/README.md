# **110. Balanced Binary Tree (Easy)**

## **LeetCode URL:**

> https://leetcode.com/problems/balanced-binary-tree/

## **Solution Date:**

> 2023/7/11

## **Problem Description:**

> 給予一個 Binary Tree，檢查高度是否平衡，也就是任一節點其子樹的高度相差不高於一。

## **Example:**

![Binary Tree](https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg)

    Input: root = [3,9,20,null,null,15,7]
    Output: true

---

![Binary Tree](https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg)

    Input: root = [1,2,2,3,3,null,null,4,4]
    Output: false

## **Approach:**

> 此題可以使用深度優先搜尋演算法(DFS)將子樹相差的高度進行記錄，然而注意此題節點所儲存的資訊對於解題無用處，所以可將節點高度資訊儲存於 val 中，透過 DFS 走向最深處之後，一層一層的遞迴進行計算高度即可解題。

## **Code**

    void dfs(TreeNode* root, bool &flag){
        if(root == nullptr)
            return;
        root->val=0;
        dfs(root->left, flag);
        dfs(root->right, flag);
        int left = 0;
        int right = 0;
        if(root->left)
            left = root->left->val;
        if(root->right)
            right = root->right->val;
        if(abs(left-right) > 1){
            flag = false;
            return;
        }
        root->val = max(left, right)+1;
    }
    class Solution {
    public:
        bool isBalanced(TreeNode* root) {
            bool flag = true;
            dfs(root, flag);
            return flag;
        }
    };

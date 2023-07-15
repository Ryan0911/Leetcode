# **226. Invert Binary Tree (Easy)**

## **LeetCode URL:**

> https://leetcode.com/problems/invert-binary-tree/

## **Solution Date:**

> 2023/7/11

## **Problem Description:**

> 給予一個二元樹，將子樹節點都顛倒過來。

## **Example:**

![Invert Binary Tree](https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg)

    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]

---

![Invert Binary Tree](https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg)

    Input: root = [2,1,3]
    Output: [2,3,1]

## **Approach:**

> 此題會運用到 pointer & 深度優先演算法(DFS) 的概念，當到最底層時便顛倒指向左右子樹的指標，之後一層一層遞迴回去。

## **Code**

    void dfs(TreeNode* root){
        if(root==nullptr)
            return;
        dfs(root->left);
        dfs(root->right);
        TreeNode* temp = root->right;
        root->right = root->left;
        root->left = temp;
    }
    class Solution {
    public:
        TreeNode* invertTree(TreeNode* root) {
            dfs(root);
            return root;
        }
    };

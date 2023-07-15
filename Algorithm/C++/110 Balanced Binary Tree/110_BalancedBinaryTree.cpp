void dfs(TreeNode *root, bool &flag)
{
    if (root == nullptr)
        return;
    root->val = 0;
    dfs(root->left, flag);
    dfs(root->right, flag);
    int left = 0;
    int right = 0;
    if (root->left)
        left = root->left->val;
    if (root->right)
        right = root->right->val;
    if (abs(left - right) > 1)
    {
        flag = false;
        return;
    }
    root->val = max(left, right) + 1;
}
class Solution
{
public:
    bool isBalanced(TreeNode *root)
    {
        bool flag = true;
        dfs(root, flag);
        return flag;
    }
};
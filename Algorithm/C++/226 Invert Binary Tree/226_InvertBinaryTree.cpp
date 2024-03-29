struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
void dfs(TreeNode *root)
{
    if (root == nullptr)
        return;
    dfs(root->left);
    dfs(root->right);
    TreeNode *temp = root->right;
    root->right = root->left;
    root->left = temp;
}
class Solution
{
public:
    TreeNode *invertTree(TreeNode *root)
    {
        dfs(root);
        return root;
    }
};
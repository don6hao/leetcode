# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if None == p and None == q:
            return True
        if None == p and None != q:
            return False
        if None != p and None == q:
            return False
        if p.val != q.val:
            return False
        if False == self.isSameTree(p.left, q.left):
            return False
        if False == self.isSameTree(p.right, q.right):
            return False
        return True


tree = []
tree1 = []
tree.append(TreeNode(1));
tree.append(TreeNode(2));
tree.append(TreeNode(3));
tree.append(TreeNode(4));
tree.append(TreeNode(5))
tree.append(TreeNode(6));
tree.append(TreeNode(7));

tree1.append(TreeNode(1));
tree1.append(TreeNode(2));
tree1.append(TreeNode(3));
tree1.append(TreeNode(4));
tree1.append(TreeNode(5))
tree1.append(TreeNode(6));
tree1.append(TreeNode(7));
tree1.append(TreeNode(8));

#if 0
tree.append(TreeNode(5));
tree.append(TreeNode(6));
tree.append(TreeNode(5));
tree.append(TreeNode(6));

tree.append(TreeNode(7));
tree.append(TreeNode(8));
tree.append(TreeNode(7));
tree.append(TreeNode(8));
#endif

tree[0].left = tree[1];
tree[0].right = tree[2];
tree[1].left = tree[3];
tree[1].right = tree[4];
tree[2].left = tree[5];
tree[2].right = tree[6];

tree1[0].left = tree1[1];
tree1[0].right = tree1[2];
tree1[1].left = tree1[3];
tree1[1].right = tree1[4];
tree1[2].left = tree1[5];
tree1[2].right = tree1[6]

p = Solution();
print p.isSameTree(tree[0], tree1[0]);

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def CheckTree(lnode, rnode):
    if None == lnode and None == rnode:
        return True
    if None != lnode and None != rnode and lnode.val == rnode.val:
        if False == CheckTree(lnode.left, rnode.right):
            return False
        if False == CheckTree(lnode.right, rnode.left):
            return False
    else:
        return False
    return True

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if None == root:
            return True
        return CheckTree(root.left, root.right)

tree = []
tree.append(TreeNode(1))
tree.append(TreeNode(2))
tree.append(TreeNode(2))

tree.append(TreeNode(3))
tree.append(TreeNode(4))
tree.append(TreeNode(4))
tree.append(TreeNode(3))

tree.append(TreeNode(5))
tree.append(TreeNode(6))
tree.append(TreeNode(6))
tree.append(TreeNode(5))

tree.append(TreeNode(7))
tree.append(TreeNode(8))
tree.append(TreeNode(8))
tree.append(TreeNode(7))

tree[0].left = tree[1]
tree[0].right = tree[2]

tree[1].left = tree[3]
tree[1].right = tree[4]

tree[2].left = tree[5]
tree[2].right = tree[6]

tree[3].left = tree[7]
tree[3].right = tree[8]
tree[6].left = tree[9]
tree[6].right = tree[10]

tree[4].left = tree[11]
tree[4].right = tree[12]
tree[5].left = tree[13]
tree[5].right = tree[14]

p = Solution()
print p.isSymmetric(tree[0])

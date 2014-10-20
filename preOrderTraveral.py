# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if None == root:
            return []
        sequence = []
        tlist    = []
        tlist.append(root)
        sequence.append(root.val)
        node = root
        while True:
            if None != node.left:
                sequence.append(node.left.val)
                tlist.append(node.left)
                node = node.left
                continue
            elif None != node.right:
                sequence.append(node.right.val)
                tlist.append(node.right)
                node = node.right
                continue
            tmp = tlist.pop()
            if 0x00 == len(tlist):
                break;
            node = tlist[len(tlist)-1]
            if tmp == node.left:
                node.left = None
            elif tmp == node.right:
                node.right = None
        return sequence


tree = [];
tree.append(TreeNode(1));
tree.append(TreeNode(2));
tree.append(TreeNode(3));

tree.append(TreeNode(4));
tree.append(TreeNode(5))
tree.append(TreeNode(6));
tree.append(TreeNode(7));

tree[0].left = tree[1];
tree[0].right = tree[2];

tree[1].left = tree[3];
tree[1].right = tree[4];

tree[2].left = tree[5];
tree[2].right = tree[6];

p = Solution();
print p.preorderTraversal(tree[0])

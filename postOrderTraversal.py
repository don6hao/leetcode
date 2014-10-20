import time
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if None == root:
            return []
        node = root
        tlist = []
        sequence = []
        tlist.append(root)
        while True:
            if None != node.left:
                node = node.left
                tlist.append(node)
                continue
            elif None != node.right:
                node = node.right
                tlist.append(node)
                continue
            else:
                tmp = tlist.pop()
                sequence.append(tmp.val)
                if 0x00 == len(tlist):
                    break;
                node = tlist[len(tlist)-1]
                if node.left == tmp:
                    node.left = None
                elif node.right == tmp:
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
print p.postorderTraversal(tree[0])

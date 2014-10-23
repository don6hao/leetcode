# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if None == root:
            return []
        queue   = collections.deque()
        queue.append(root)
        rlist = []
        tmplist = []
        tmplist.append(root.val)
        rlist.append(tmplist)
        while 0x00 != len(queue):
            i = 0x00
            length = len(queue)
            tmplist = []
            while i < length:
                try:
                    node = queue.popleft()
                    if None != node.left:
                        queue.append(node.left)
                        tmplist.append(node.left.val)
                    if None != node.right:
                        queue.append(node.right)
                        tmplist.append(node.right.val)
                except IndexError:
                    break
                i += 1
            if 0 != len(tmplist):
                rlist.append(tmplist)
        return rlist


tree = []
tree.append(TreeNode(1));
tree.append(TreeNode(2));
tree.append(TreeNode(3));

tree.append(TreeNode(4));
tree.append(TreeNode(5))
tree.append(TreeNode(6));
tree.append(TreeNode(7));

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

p = Solution();
p.levelOrder(tree[0]);

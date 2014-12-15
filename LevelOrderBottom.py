import time
import copy
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#For example:
#Given binary tree {3,9,20,#,#,15,7},
    #3
   #/ \
  #9  20
    #/  \
   #15   7
#return its bottom-up level order traversal as:
#[
  #[15,7],
  #[9,20],
  #[3]
#]
class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def getLevelNodeList(self, nodeList):
        tmpList = []
        for node in nodeList:
            if None != node.left:
                tmpList.append(node.left)
            if None != node.right:
                tmpList.append(node.right)
        return tmpList

    def getLevelNodeValueList(self, nodeList):
        valList = []
        for node in nodeList:
            valList.append(node.val)
        return valList

    def levelOrderBottom(self, root):
        if None == root:
            return None
        resultList = []
        resultList.insert(0, [root.val])
        nodeList = []
        nodeList.append(root)
        while True:
            nodeList = self.getLevelNodeList(nodeList)
            if 0x00 == len(nodeList):
                break
            resultList.insert(0, self.getLevelNodeValueList(nodeList))
        return resultList

if __name__ == '__main__':
    tree = []
    tree.append(TreeNode(1));
    tree.append(TreeNode(2));
    tree.append(TreeNode(3));

    tree.append(TreeNode(4));
    tree.append(TreeNode(5))
    tree.append(TreeNode(6));
    tree.append(TreeNode(7));
    tree.append(TreeNode(8));
    tree.append(TreeNode(9));

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
    print p.levelOrderBottom(tree[0]);

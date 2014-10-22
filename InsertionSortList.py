import time
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if None == head or None == head.next:
            return head
        newlist = ListNode(0)
        newlist.next = head
        node = head
        while None != node.next:
            if node.val > node.next.val:
                prev = newlist
                while prev.next.val < node.next.val:
                    prev = prev.next
                tmp = node.next
                node.next = tmp.next
                tmp.next = prev.next
                prev.next = tmp
            else:
                node = node.next
        return newlist.next








listnode = []
listnode.append(ListNode(6))
listnode.append(ListNode(5))
listnode.append(ListNode(3))
listnode.append(ListNode(1))
listnode.append(ListNode(9))
listnode.append(ListNode(7))
listnode.append(ListNode(0))
listnode.append(ListNode(4))

listnode[0].next = listnode[1]
listnode[1].next = listnode[2]
listnode[2].next = listnode[3]
listnode[3].next = listnode[4]
listnode[4].next = listnode[5]
listnode[5].next = listnode[6]
listnode[6].next = listnode[7]
listnode[7].next = None

p = Solution()
node = listnode[0]
node = p.insertionSortList(listnode[0])
while None != node:
    print node.val
    node = node.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if None == head or None == head.next:
            return head
        mid = (head.val + head.next.val)/2
        if head.val > head.next.val:
            rhead, lhead = head, head.next
        else:
            rhead, lhead = head.next, head
        ltmp = lhead
        rtmp = rhead
        tmp  = head.next.next
        rcount, lcount = 0,0
        while None != tmp:
            if mid < tmp.val:
                rtmp.next = tmp
                rcount += 1
                rtmp = tmp
            elif mid > tmp.val:
                ltmp.next = tmp
                ltmp = tmp
                lcount += 1
            else:
                if lcount < rcount:
                    ltmp.next = tmp
                    ltmp = tmp
                    lcount += 1
                else:
                    rtmp.next = tmp
                    rtmp = tmp
                    rcount += 1
            tmp = tmp.next
        ltmp.next, rtmp.next = None, None

        rhead = self.sortList(rhead)
        lhead = self.sortList(lhead)

        tmp = lhead
        while tmp.next != None:
            tmp = tmp.next
        tmp.next = rhead
        return lhead



if __name__ == "__main__":
    list = []
    list.append(ListNode(26))
    list.append(ListNode(5))
    list.append(ListNode(37))
    list.append(ListNode(1))
    list.append(ListNode(61))
    list.append(ListNode(11))
    list.append(ListNode(59))
    list.append(ListNode(15))
    list.append(ListNode(48))
    list.append(ListNode(19))

    for i in range(len(list)-1):
        list[i].next = list[i+1]

    tmp = list[0]
    while True:
        if None == tmp:
            break
        print tmp.val
        tmp = tmp.next

    print '============================================'

    p = Solution()

    list_head = p.sortList(list[0])

    tmp = list_head
    while True:
        if None == tmp:
            break
        print tmp.val
        tmp = tmp.next

    print '*********************************************'

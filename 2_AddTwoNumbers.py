class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        return


ans = ListNode(0)
node = ans
temp = 0
while l1 is not None or l2 is not None or temp > 0:
    if l1 is not None:
        temp += l1.val
        l1 = l1.next
    if l2 is not None:
        temp += l2.val
        l2 = l2.next
    node.next = ListNode(temp % 10)
    node = node.next
    temp = temp // 10
return ans.next

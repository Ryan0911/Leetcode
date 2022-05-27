class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ans = ListNode()
        ans_p = ans
        while list1 and list2:
            if(list1.val <= list2.val):
                ans_p.next = list1
                ans_p = ans_p.next
                list1 = list1.next
            else:
                ans_p.next = list2
                ans_p = ans_p.next
                list2 = list2.next
        while list1:
            ans_p.next = list1
            ans_p = ans_p.next
            list1 = list1.next
        while list2:
            ans_p.next = list2
            ans_p = ans_p.next
            list2 = list2.next
        return ans.next  # 原來可以這樣寫...!

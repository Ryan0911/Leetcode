# **21. Merge Two Sorted Lists (Easy)**

## **LeetCode URL:**

> https://leetcode.com/problems/merge-two-sorted-lists/

## **Solution Date:**

> 2023/7/10

## **Problem Description:**

> 給予兩個裝有整數資料的 singly linked list，現在要將這兩個 singly linked list 接起來，且資料由小排到大，再將這個 singly linked list 做回傳。

## **Example:**

    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

---

    Input: list1 = [], list2 = []
    Output: []

## **Approach:**

> 基本上這題就是多宣告一個指向開頭的指標(head)以及一個暫存指標將兩個 singly linked list 比大小後改變指標節點，但要記得迴圈比較完其中一個 list 後還要再把另一個 list 的殘餘節點接起來之後相接後回傳 head 即可。  
> 另外有個小技巧就是，這邊測資有可能會給其中一個 list 為空，此時只要直接回傳另一個 list 即可，這樣會大大提升速度。

## **Code**

    class Solution {
    public:
        ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
            if (!list1)
                return list2;
            if (!list2)
                return list1;
            ListNode *head;
            if (list1->val <= list2->val) {
                head = list1;
                list1 = list1->next;
            }
            else {
                head = list2;
                list2 = list2->next;
            }
            ListNode *current = head;
            while (list1&&list2) {
                if (list1->val <= list2->val) {
                    current->next = list1;
                    list1 = list1->next;
                }
                else {
                    current->next = list2;
                    list2 = list2->next;
                }
                current = current->next;
            }
            if (list1)
                current->next = list1;
            else if (list2)
                current->next = list2;
            return head;
        }
    };

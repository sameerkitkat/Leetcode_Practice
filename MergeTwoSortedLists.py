'''
Merge two sorted linked lists and return it as a new sorted list.
The new list should be made by splicing together
the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''


 def mergeTwoLists(l1, l2):

        dummy = ListNode(-1)
        pointer = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                pointer.next = l1
                l1 = l1.next
            else:
                pointer.next = l2
                l2 = l2.next
            pointer = pointer.next

        if l1 is None:
            pointer.next = l2
        if l2 is None:
            pointer.next = l1

        return dummy.next

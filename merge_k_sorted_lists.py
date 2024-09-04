# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from heapq import heappop, heappush

        minHeap = []
        for head in lists:
            if head:
                heappush(minHeap, (head.val, head))
        
        dummy = tail = ListNode(0)
        while minHeap:
            val, node = heappop(minHeap)
            tail.next = node
            tail = tail.next
            if node.next:
                heappush(minHeap, (node.next.val, node.next))
        
        return dummy.next
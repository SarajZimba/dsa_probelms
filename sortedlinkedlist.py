class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        prev = head
        current = head.next
        
        while current:
            if prev.val == current.val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        
        return head

# Example usage:
# Create a sorted linked list: 1 -> 1 -> 2 -> 3 -> 3
node5 = ListNode(3)
node4 = ListNode(3, node5)
node3 = ListNode(2, node4)
node2 = ListNode(1, node3)
node1 = ListNode(1, node2)

#1 -> 1 -> 2 -> 3 -> 3

# Iteration 1
#node1

# Call the function to delete duplicates
solution = Solution()
result_head = solution.deleteDuplicates(node1)

# Print the result
current = result_head
while current:
    print(current.val, end=" -> ")
    current = current.next

print("Done")


#understanding and creating the linked list

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.val, end=" -> ")
#         current = current.next
#     # print("None")

# # class Solution:
# #     def deleteDuplicates(self, head:ListNode) -> ListNode:

# # Example usage:
# # Create a sorted linked list: 1 -> 1 -> 2 -> 3 -> 3
# node5 = ListNode(3)
# node4 = ListNode(3, node5)
# node3 = ListNode(2, node4)
# node2 = ListNode(1, node3)
# node1 = ListNode(1, node2)

# print(print_linked_list(node1))

#Creating the Linked list

# class ListNode:
#     def __init__(self, val=0, next=None) -> None:
#         self.val=val
#         self.next = next

# node3 = ListNode(3)
# node2 = ListNode(2, node3)
# node1 = ListNode(1, node2)
# # node2 = ListNode(2)
# # node
        
# def print_linked_list(node):
#     current = node

#     while current:
#         print(current.val, end= "->")

#         current = current.next

#     print("None")
# print_linked_list(node1)    
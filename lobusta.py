class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_linked_list(self):
        current = self.head
        while current:
            print(current.value, end="")
            if current.next:
                print("->", end="")
            current = current.next
        print()

def merge_sorted_lists(list1, list2):
    dummy = ListNode()  # Dummy node to simplify the code
    current = dummy

    while list1 is not None and list2 is not None:
        if list1.value < list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    # If one of the lists is not exhausted, append the remaining nodes
    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2

    result_list = LinkedList()
    result_list.head = dummy.next  # Skip the dummy node in the final result
    return result_list

# Example usage:
list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(4)

list2 = LinkedList()
list2.append(1)
list2.append(3)
list2.append(4)

merged_list = merge_sorted_lists(list1.head, list2.head)
print("Merged List:", end=" ")
merged_list.print_linked_list()


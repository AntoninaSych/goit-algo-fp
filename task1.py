class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev_node = None
    current_node = head
    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    return prev_node

def insertion_sort(head):
    dummy = ListNode(float('-inf'))
    current = head
    while current:
        prev, insert_node = dummy, dummy.next
        while insert_node and insert_node.value < current.value:
            prev, insert_node = insert_node, insert_node.next
        next_current = current.next
        prev.next = current
        current.next = insert_node
        current = next_current
    return dummy.next

def merge_sorted_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.value < l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 if l1 else l2
    return dummy.next

# Приклади використання:
# Створення однозв'язного списку: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Реверсування однозв'язного списку
reversed_head = reverse_linked_list(head)

# Сортування однозв'язного списку
sorted_head = insertion_sort(reversed_head)

# Об'єднання двох відсортованих списків
list1 = ListNode(1, ListNode(3, ListNode(5)))
list2 = ListNode(2, ListNode(4, ListNode(6)))
merged_head = merge_sorted_lists(list1, list2)
 # Виведення результатів
print("Результат реверсування однозв'язного списку:")
current = reversed_head
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")

print("\nРезультат сортування однозв'язного списку:")
current = sorted_head
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")

print("\nРезультат об'єднання двох відсортованих списків:")
current = merged_head
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")

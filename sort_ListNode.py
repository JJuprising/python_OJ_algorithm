class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sortLinkedList(head):
    # 如果链表为空或者只有一个值，直接输出
    if not head or not head.next:
        return head

    # 使用归并排序
    # 链表是一种单向线性数据结构，我们无法像数组那样直接通过索引来访问中间元素。
    # 因此采用快慢指针的方式将链表分割成两个近似相等长度的子链表
    def mergeSort(head):
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        # 快指针每次移动两步，而慢指针每次移动一步。当快指针到达链表尾部时，慢指针就会指向链表的中间节点。
        # 相当于通过这个步骤找出接近中间的节点然后讲链表分成两个独立的子链表
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        right_head = slow.next
        slow.next = None
        left_sorted = mergeSort(head)
        right_sorted = mergeSort(right_head)

        # 合并有序链表
        dummy = ListNode()
        current = dummy
        while left_sorted and right_sorted:
            if left_sorted.val < right_sorted.val:
                current.next = left_sorted
                left_sorted = left_sorted.next
            else:
                current.next = right_sorted
                right_sorted = right_sorted.next
            current = current.next
        current.next = left_sorted or right_sorted

        return dummy.next

    return mergeSort(head)


def createLinkedList(input_str):
    values = map(int, input_str.split())
    head = ListNode()
    current = head
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return head.next


def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()


input_str = input()
head = createLinkedList(input_str)
sorted_head = sortLinkedList(head)
printLinkedList(sorted_head)

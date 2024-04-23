"""
合并k个升序列表

思想，因为每个链表都是有序的，因此对他们进行排序，每次取最小的放进去就好了
建立小根堆
"""
import heapq
import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


ListNode.lt = lambda self, other: self.val < other.val


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        # 虚拟头结点
        dummy = ListNode(-1)
        p = dummy

        # 优先级队列
        pq = []
        for head in lists:
            if head:
                heapq.heappush(pq, (head.val, head)) # 往pq内建立小根堆
        print("---")
        print_priority_queue(pq)
        print("---")
        # traverse_linked_lists(pq)
        while pq:
            # 获取最小节点 接到结果链表中

            node = heapq.heappop(pq)[1]  # heapq.heappop()是从堆中弹出并返回最小的值,取1指头节点
            # far=heapq.heappop(pq)[0]
            # print(node.val,far.val)
            p.next = node
            if node.next:
                heapq.heappush(pq, (node.next.val, node.next))
            # p前进
            p = p.next
            # print_priority_queue(pq)
        return dummy.next


# 生成链表数组
def generate_random_linked_list(length):
    if length == 0:
        return None
    head = ListNode(random.randint(1, 100))  # 随机生成头节点的值
    curr = head
    for _ in range(length - 1):
        value = random.randint(1, 100)  # 随机生成节点的值
        new_node = ListNode(value)
        curr.next = new_node
        curr = new_node
    return head


# 输出优先级队列
def print_priority_queue(pq):
    while pq:
        element = heapq.heappop(pq)
        print(element)


def traverse_linked_lists(linked_lists):
    for i, linked_list in enumerate(linked_lists):
        print(f"Linked List {i + 1}: ", end="")
        curr = linked_list
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")


length = 5  # 链表数组的长度
linked_lists = []

for _ in range(length):
    linked_list = generate_random_linked_list(random.randint(1, 10))  # 随机生成链表的长度
    linked_lists.append(linked_list)

traverse_linked_lists(linked_lists)
s = Solution()
re=s.mergeKLists(linked_lists)

# traverse_linked_lists(re)

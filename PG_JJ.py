"""
链表排序

思想 拆分完后 各自排序，再每部分合并从新排序

快慢指针找中点

这个方法过不了 看2
"""

# 链表节点
class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

def merge(l1,l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.val<=l2.val:
        # l1放最前 后面继续成链
        l1.next=merge(l1.next,l2)
        return l1
    else:
        l2.next=merge(l1,l2.next)
        return l2
# def merge_sort(node,len):
#     # 找链表中间
#     if node is None or node.next is None or len is 0:
#         return node
#
#     slow=node
#     mid_loc=len//2
#     print(f"mid_loc:{mid_loc}")
#     for i in range(mid_loc): # 中点
#         slow=slow.next
#
#     mid=slow.next
#     slow.next=None # 断开
#
#     # 左右子链归并排序
#     left=merge_sort(node,mid_loc)
#     right=merge_sort(mid,len-mid_loc)
#
#     return merge_sort(left,right)
def merge_sort(head):
    if head is None or head.next is None:
        return head

    slow = head
    fast = head.next

    # 找到链表的中点
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    left = merge_sort(head)
    right = merge_sort(mid)

    return merge(left, right)
def print_list(node):
    while node.next:
        print(node.val,end=' ')
        node=node.next

    print(node.val,end='')

if __name__=="__main__":
    # 读取构造链表
    nums = input().split()
    head = ListNode(int(nums[0]))
    curr = head
    for num in nums[1:]:
        curr.next = ListNode(int(num))
        curr = curr.next
    # print_list(head)

    new=merge_sort(head)

    print_list(new)

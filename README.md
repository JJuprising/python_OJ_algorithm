# 参考
https://labuladong.gitee.io/algo/home/

# 基础知识
## 数据结构基本操作

 数组遍历

```python
def traverse(arr: List[int]):
    for i in range(len(arr)):
        # 迭代访问 arr[i]
```

链表，迭代递归

```python
# 基本的单链表节点
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def traverse(head: ListNode) -> None: # -> None 是类型注释的一部分，用于说明函数的返回类型。
    p = head
    while p is not None:
        # 迭代访问 p.val
        p = p.next

def traverse(head: ListNode) -> None:
    # 递归访问 head.val
```

二叉树 递归

```python
# 基本的二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def traverse(root: TreeNode):
    traverse(root.left) # 递归遍历左子树
    traverse(root.right) # 递归遍历右子树
    
def traverse(root):
    # 前序位置
    traverse(root.left)
    # 中序位置
    traverse(root.right)
    # 后序位置
```

## 链表
快慢指针找中点
```python
"""
链表排序

思想 拆分完后 各自排序，再每部分合并从新排序

快慢指针找中点
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
    while node:
        print(node.val,end=' ')
        node=node.next
if __name__=="__main__":
    # 读取构造链表
    nums=list(map(int,input().split()))
    head=ListNode(int(nums[0])) # 记录头结点
    curr=head # 工作指针
    len=len(nums)
    for num in nums[1:]: # 从1之后开始赋值，第0个已经在头结点了
        curr.next=ListNode(int(num))
        curr=curr.next
    # print_list(head)
    print()
    new=merge_sort(head,len)

    print_list(new)

```

### 合并k个有序链表

小根堆，面试常考题，

```python
"""
合并k个升序列表

思想，因为每个链表都是有序的，因此对他们进行排序，每次取最小的放进去就好了
建立小根堆
"""
import heapq
import random
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
```

### 单链表的倒数第k个节点

巧妙思想

如何一次遍历链表就到倒数第k个节点呢

用p1先走k，然后设置一个新的p2指向头节点，和p2一起走

当p2走到末尾，p1也就到倒数第k个了

```python
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 预防删除头结点的 虚拟节点的重要性
        # 如果是直接从head开始，应对不了规模为1删除为1的，或者是删除的是头结点的情况
        newnode=ListNode(-1)
        newnode.next=head
        p1=newnode
        p2=newnode
        for i in range(n):
            p1=p1.next
        
        # p2开始遍历，直至p1到尾
        # if p1==None:
        #     return None
        while p1.next :
            p1=p1.next
            p2=p2.next
        
        # 删除第n个，即下一个
        p2.next=p2.next.next
        return newnode.next
```

### 单链表的中点

快慢指针法

```python
def middleNode(head:ListNode):
	# 快慢指针初始化指向head
    slow=head
    fast=head
    # 快指针走向末尾
    while fast and fast.next:# fast判断下一轮直接走出界的情况
        slow=slow.next # 走一步
        fast=fast.next.next # 走两步
    # 慢指针指向中点
    return slow 
```

### 链表是否有环

力扣第 142 题「[环形链表 IIopen in new window](https://leetcode.cn/problems/linked-list-cycle-ii/)」

![image-20240313162945782](C:\Users\chan\AppData\Roaming\Typora\typora-user-images\image-20240313162945782.png)

###  两个链表是否相交

太巧妙了！
a，b长度可能不同，但是让p1走完a然后走b，p2走完b走a，就能同时达到公共区域
第一次相等的那一刻就是连接点

```python
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1,p2=headA,headB
        while p1!=p2:
            if p1==None:
                p1=headB
            else:
                p1=p1.next
            if p2==None:
                p2=headA
            else:
                p2=p2.next
        return p1
```

## 数组

### 快慢指针技巧
删除重复项
巧妙，利用快慢指针，fast扫到一个新的直接赋值给slow
fast直是在最开始多1，速度是同步的
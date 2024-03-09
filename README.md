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
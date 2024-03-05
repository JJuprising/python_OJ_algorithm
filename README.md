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


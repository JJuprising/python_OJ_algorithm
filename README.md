# 参考
https://labuladong.gitee.io/algo/home/

```python
# 找到数组中的最大值及其索引 速度更快
    max_num = max(nums)
    max_idx = nums.index(max_num) 
```



# 基础知识

## 模板

### 输入输出





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

### 二分法
167 两数组之和 输入有序数组
给你一个下标从 1 开始的整数数组 numbers ，该数组已按 非递减顺序排列  ，请你从数组中找出满足相加之和等于目标数 target 的两个数。如果设这两个数分别是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.length 。

以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。

你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。

```python
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 非递减排序就可以用类似二分法
        lenth=len(numbers)
        left,right=0,lenth-1
        while left!=right:
            sum=numbers[left]+numbers[right]
            if sum==target:
                return [left+1,right+1]
            if sum<target:
                left+=1
            else:
                right-=1
        return [-1,-1]
```

5 最长回文子串
核心：对每个字符向两边扩散，注意区分奇偶数情况
```python
def longestPalindrome(s: str) -> str:
    res = ""
    for i in range(len(s)):
        # 以 s[i] 为中心的最长回文子串
        s1 = palindrome(s, i, i)
        # 以 s[i] 和 s[i+1] 为中心的最长回文子串
        s2 = palindrome(s, i, i + 1)
        # res = longest(res, s1, s2)
        res = res if len(res) > len(s1) else s1
        res = res if len(res) > len(s2) else s2
    return res

def palindrome(s, l, r):
    while (l >= 0 and r < len(s) and s[l] == s[r]):
        l -= 1
        r += 1
    return s[l+1:r]
```

## 二叉树
动归/DFS/回溯算法都可以看做二叉树问题的扩展，只是它们的关注点不同：

动态规划算法属于分解问题的思路，它的关注点在整棵「子树」。
回溯算法属于遍历的思路，它的关注点在节点间的「树枝」。
DFS 算法属于遍历的思路，它的关注点在单个「节点」。

层序遍历
```python
def levelTraverse(root: TreeNode):
    if not root:
        return
    
    q = deque()
    q.append(root)

    # 从上到下遍历二叉树的每一层
    while q:
        sz = len(q)
        # 从左到右遍历每一层的每个节点
        for i in range(sz):
            cur = q.popleft()
            # 将下一层节点放入队列
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
```

### 前中序构造

理解前中序数组的结构

![img](https://labuladong.online/algo/images/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%B3%BB%E5%88%972/4.jpeg)

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 存索引

val2Index={}
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        for i in range(len(inorder)):#这里和leftSize对应
            val2Index[inorder[i]]=i
        return self.build(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1)
    def build(self,preorder,prestart,preend,inorder,instart,inend):
        if prestart>preend:
            return None
        rootVal=preorder[prestart]
        root=TreeNode(rootVal) # 构造头
        index=val2Index.get(rootVal)
        leftSize=index-instart
        root.left=self.build(preorder,prestart+1,prestart+leftSize,inorder,instart,index-1)
        root.right=self.build(preorder,prestart+leftSize+1,preend,inorder,index+1,inend)

        return root
        
```

### 中序后序

![image-20240406013906501](C:\Users\chan\AppData\Roaming\Typora\typora-user-images\image-20240406013906501.png)

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
var2Index={}
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        for i in range(len(inorder)): #这里和rightSize对应
            var2Index[inorder[i]]=i
        return self.build(postorder,len(postorder)-1,0,inorder,0,len(inorder)-1)
    def build(self,postorder,poststart,postend,inorder,instart,inend):
        if poststart<postend:
            return None
        # if instart > inend:
        #     return None

        rootVal=postorder[poststart]
        root=TreeNode(rootVal)
        index=var2Index.get(rootVal)
        rightSize=inend-index

        root.right=self.build(postorder,poststart-1,poststart-rightSize,inorder,index+1,inend)
        root.left=self.build(postorder,poststart-rightSize-1,postend,inorder,instart,index-1)
        return root

```

### 前序后序

```python
var2Index={}
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        for i in range(len(postorder)):
            var2Index[postorder[i]]=i
        return self.build(preorder,0,len(preorder)-1,postorder,len(postorder)-1,0)
    def build(self,preorder,prestart,preend,postorder,poststart,postend):
        if prestart>preend:
            return None
        if prestart==preend:
            return TreeNode(preorder[prestart])
        rootVal=preorder[prestart]
        root=TreeNode(rootVal)
        leftrootVal=preorder[prestart+1]
        #直接折半
        index=var2Index.get(leftrootVal)
        leftSize=index-postend+1
        root.left=self.build(preorder,prestart+1,prestart+leftSize,postorder,index,postend)
        root.right=self.build(preorder,prestart+leftSize+1,preend,postorder,poststart-1,index+1)
        return root
```



## 动态规划

斐波那契，dp数组降到1维，动态变化三个值即可
```python
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        if n==1:
            return 1
        dp_i=1
        dp_ii=1
        dp_iii=1
        for i in range(2,n):
            dp_iii=dp_i+dp_ii
            dp_i=dp_ii
            dp_ii=dp_iii
        return dp_iii
```

### 最长递增子序列

**既然是递增子序列，我们只要找到前面那些结尾比 3 小的子序列，然后把 3 接到这些子序列末尾，就可以形成一个新的递增子序列，而且这个新的子序列长度加一**。

```python
for (int j = 0; j < i; j++) {
    if (nums[i] > nums[j]) {
        dp[i] = Math.max(dp[i], dp[j] + 1);
    }
}
```


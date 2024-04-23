class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        # 扫描到一个大于等于x的，记录前一个节点位置
        # 接着扫描所有小于x的，摘链上链
        phead=head
        ptar=None
        pfather=head
        while phead.next:
            if phead.next.val>=x and not ptar:
                ptar=phead
                # 下一个位置就是要插入的
            if ptar:
                # 说明找到了大于等于x的
                if phead.val<x:
                    # 摘链
                    pfather.next=phead.next
                    # 上链
                    phead.next=ptar.next
                    ptar.next=phead
                    ptar=phead # 移动插入位
                    phead=pfather# 扫描指针归位

            pfather=phead
            phead=phead.next

        return head

if __name__=="__main__":
    s=Solution()
    
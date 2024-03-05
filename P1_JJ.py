# 最大二叉树

# 构造数
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.right=right
        self.left=left


# 解题函数
def construct_tree(nums):
    # 接受一个数组
    if not nums: # 如果为空 返回none
        return None

    # 最大二叉树，先找出目前数组最大值和对应索引
    max_num=max(nums)
    max_index=nums.index(max_num)

    # 构建根节点
    root=TreeNode(max_num)

    # 递归构建左右树
    root.left=construct_tree(nums[:max_index]) # 左树由当前最大值的左边所有数构成
    root.right=construct_tree(nums[max_index+1:])# 右树由当前最大值的右边所有数构成
    return root

# 输出函数
def preOrder(root):
    # 遍历树
    if root:
        # 前序遍历
        print(root.val,end=' ')
        # 叶子节点就不用输出自己下面两个空子节点了，不理解可以注释掉这部分对比输出结果
        if not root.left and not root.right:
            return
        preOrder(root.left)
        preOrder(root.right)
    else:
        print("null",end=' ')



if __name__ == "__main__":
    # 从标准输入获取输入数据
    nums = list(map(int, input().split()))
    root=construct_tree(nums)
    preOrder(root)


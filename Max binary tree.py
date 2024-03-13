class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def constructMaximumBinaryTree(nums):
    if not nums:
        return None

    max_val = max(nums)
    max_index = nums.index(max_val)

    root = TreeNode(max_val)

    root.left = constructMaximumBinaryTree(nums[:max_index])
    root.right = constructMaximumBinaryTree(nums[max_index+1:])
    return root


def preorderTraversal(root):
    if root:
        print(root.val,end=" ")
        if not root.left and not root.right:
            return
        preorderTraversal(root.left)
        preorderTraversal(root.right)
    else:
        print("null",end=" ")

if __name__ == "__main__":
    nums = list(map(int,input().split(" ")))
    root = constructMaximumBinaryTree(nums)
    preorderTraversal(root)

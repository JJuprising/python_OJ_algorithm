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
    if max_index > 0:
        root.left = constructMaximumBinaryTree(nums[:max_index])
    if max_index < len(nums) - 1:
        root.right = constructMaximumBinaryTree(nums[max_index + 1:])

    return root


def preorderTraversal(root):
    if not root:
        return []
    if not root.left and not root.right:
        return [str(root.val)]
    left = preorderTraversal(root.left) if root.left else ["null"]
    right = preorderTraversal(root.right) if root.right else ["null"]
    return [str(root.val)] + left + right


if __name__ == "__main__":
    nums = [3, 2, 1, 6, 0, 5]
    root = constructMaximumBinaryTree(nums)
    result = preorderTraversal(root)
    print(result)

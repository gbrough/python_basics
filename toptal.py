#Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
      if root == None:
        return 0
      if root.val >= low and root.val <= high:
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
      else:
        return self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

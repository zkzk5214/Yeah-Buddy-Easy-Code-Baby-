# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def reConstructBinaryTree(self, Preorder, Inorder):
        if not Preorder or not Inorder:
            return None
        root = TreeNode(Preorder.pop(0))  # removes the root(the first) from the list and returns the removed item.
        index = Inorder.index(root.val)  # root 在 Inoder 中的 index
        root.left = self.reConstructBinaryTree(Preorder[:index], Inorder[:index])
        root.right = self.reConstructBinaryTree(Preorder[index:], Inorder[index+1:])
        return root

# Preorder {1,2,4,7,3,5,6,8} after pop {2,4,7,3,5,6,8}
# Inorder {4,7,2,1,5,3,8,6}
# root.val = 1  index = 3
# root.left = ... ({2,4,7}，{4,7,2})
# root.right = ...({3,5,6,8},{5,3,8,6})

# sub-left 1
# Preorder {2,4,7} after pop {4,7}
# Inorder {4,7,2}
# (sub-)root.val = 2  index = 2
# root.left = ... ({4,7}，{4,7})
# root.right = ...({},{})

# left self 2
# Preorder {4,7} after pop {7}
# Inorder {4,7}
# (sub-)root.val = 4  index = 0
# root.left = ... ({},{})
# root.right = ...({7},{})

#     1
#    / \
#   2    3
#  /    / \
# 4    5   6
#  \       /
#   7     8

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def height(node):
    if not node:
        return -1
    return max(height(node.left), height(node.right)) + 1

def size(node):
    if not node:
        return 0
    return size(node.left) + size(node.right) + 1

def isBalanced(node):
    if not node:
        return True
    left_height = height(node.left)
    right_height = height(node.right)
    if abs(left_height - right_height) > 1:
        return False
    return isBalanced(node.left) and isBalanced(node.right)

def isProper(node):
    if not node:
        return True
    if (node.left and not node.right) or (node.right and not node.left):
        return False
    return isProper(node.left) and isProper(node.right)

# Implementations for 'isFull' and 'isComplete' would be similar but with their respective conditions.

class TreeNode:
       def __init__(self,data):
              self.data=data
              self.left=None
              self.right=None

root = TreeNode(10)

root.left = TreeNode(5)
root.right = TreeNode(20)

root.left.left = TreeNode(3)
root.left.right = TreeNode(7)

root.right.right = TreeNode(30)              

def preOrder(root):
       if root is None:
         return
       print(root.data, end=" ")
       preOrder(root.left)
       preOrder(root.right)

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)       

def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")        



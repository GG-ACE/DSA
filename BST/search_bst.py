class BstNode:
  def __init__(self,data, left, right):
    self.data,self.left, self.right = data, left, right
    
  def search_bst(tree: BstNode, key: int) -> Optional[BstNode]:
    return ( tree if not tree or tree.data == key else search_bst(tree.left,key) if key < tree.data else search_bst(tree.right,key))
  # use of recursion to find the key in BST, base conditon then left or right scenario

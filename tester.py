import AVLTree

tree = AVLTree.AVLTree()
tree.insert(9, "")
tree.insert(5, "")
tree.insert(6, "")
tree.insert(4, "")
tree.insert(11, "")
print(tree.avl_to_array())
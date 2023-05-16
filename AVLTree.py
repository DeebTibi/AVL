# username - complete info
# id1      - complete info
# name1    - complete info
# id2      - complete info
# name2    - complete info


"""A class represnting a node in an AVL tree"""
from printree import *

class AVLNode(object):
    """Constructor, you are allowed to add more fields.
	
	@type key: int or None
	@param key: key of your node
	@type value: any
	@param value: data of your node
	"""

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1
        self.size = 0
        self.bf = 0

    """changes values of node to non virtual
    """

    def set_not_virtual(self):
        virtual_node = AVLNode(None, None)
        self.left = virtual_node
        self.right = virtual_node
        virtual_node.set_parent(self)
        self.height = 0
        self.size = 1

    """returns the key
    
	@rtype: int or None
	@returns: the key of self, None if the node is virtual
	"""
    def get_key(self):
        return self.key if self.is_real_node() else None

    """returns the value
    
	@rtype: any
	@returns: the value of self, None if the node is virtual
	"""
    def get_value(self):
        return self.value if self.is_real_node() else None

    """returns the left child
    
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	"""

    def get_left(self):
        return self.left

    """returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	"""

    def get_right(self):
        return self.right

    """returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""

    def get_parent(self):
        return self.parent

    """returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""

    def get_height(self):
        return self.height

    """returns the size of the subtree

	@rtype: int
	@returns: the size of the subtree of self, 0 if the node is virtual
	"""

    def get_size(self):
        return self.size

    """returns the size of the subtree

    @rtype: int
    @returns: the balance factor of the subtree of self, 0 if the node is virtual
    """

    def get_bf(self):
        return self.bf

    """sets key

	@type key: int or None
	@param key: key
	"""

    def set_key(self, key):
        self.key = key
        return None

    """sets value

	@type value: any
	@param value: data
	"""

    def set_value(self, value):
        self.value = value
        return None

    """sets left child

	@type node: AVLNode
	@param node: a node
	"""

    def set_left(self, node):
        self.left = node
        return None

    """sets right child

	@type node: AVLNode
	@param node: a node
	"""

    def set_right(self, node):
        self.right = node
        return None

    """sets parent

	@type node: AVLNode
	@param node: a node
	"""

    def set_parent(self, node):
        self.parent = node
        return None

    """sets the height of the node

	@type h: int
	@param h: the height
	"""

    def set_height(self, h):
        self.height = h
        return None

    """sets the size of node

	@type s: int
	@param s: the size
	"""

    def set_size(self, s):
        self.size = s
        return None

    """sets the size of node

    @type bf: int
    @param bf: the balance factor
    """

    def set_bf(self, bf):
        self.bf = bf
        return None

    """returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""

    def is_real_node(self):
        return self.height != -1


"""
A class implementing an AVL tree.
"""


class AVLTree(object):
    def __repr__(self): # no need to understand the implementation of this one
        if not self.get_root():
            return "#"
        out = ""
        for row in printree(self.root): # need printree.py file
            out = out + row + "\n"
        return out

    """
	Constructor, you are allowed to add more fields.  

	"""

    def __init__(self):
        self.root = None

    # add your fields here

    """searches for a node in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: node corresponding to key.
	"""

    def search(self, key):
        curr_node = self.root
        while curr_node.is_real_node():
            if curr_node.key == key:
                return curr_node
            elif curr_node.key > key:
                curr_node = curr_node.left
            elif curr_node.key < key:
                curr_node = curr_node.right
        return None

    """inserts val at position i in the dictionary

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: any
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

    def insert(self, key, val):
        num_of_operations = 0
        inserted_node = AVLNode(key, val)
        inserted_node.set_not_virtual()
        if not self.root:
            self.root = inserted_node
            return 0
        parent = self.root
        # insertion
        while parent.is_real_node():
            parent.set_size(parent.get_size() + 1)
            if parent.key > key:
                parent = parent.get_left()
            elif parent.key < key:
                parent = parent.get_right()
        parent = parent.get_parent()
        if parent.key > key:
            parent.set_left(inserted_node)
        else:
            parent.set_right(inserted_node)
        inserted_node.set_parent(parent)
        # balancing
        while parent is not None:
            new_height = max(parent.get_left().get_height(), parent.get_right().get_height()) + 1
            new_bf = parent.get_left().get_height() - parent.get_right().get_height()
            parent.set_bf(new_bf)
            if abs(new_bf) < 2 and new_height == parent.get_height():
                return num_of_operations
            elif abs(new_bf) < 2 and new_height != parent.get_height():
                parent.set_height(new_height)
                num_of_operations += 1
                parent = parent.get_parent()
            else:
                if parent.get_bf() == 2 and parent.get_left().get_bf() == 1:
                    self.right_rotate(parent, parent.get_parent())
                    num_of_operations += 1
                elif parent.get_bf() == 2 and parent.get_left().get_bf() == -1:
                    self.left_right_rotate(parent)
                    num_of_operations += 2
                elif parent.get_bf() == -2 and parent.get_right().get_bf() == 1:
                    self.right_left_rotate(parent)
                    num_of_operations += 2
                elif parent.get_bf() == -2 and parent.get_right().get_bf() == -1:
                    self.left_rotate(parent, parent.get_parent())
                    num_of_operations += 1
                return num_of_operations

    """deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
    def delete(self, node: AVLNode):
        physically_deleted = None
        virtual_node = AVLNode(None, None)
        num_of_operations = 0
        if not node.right.is_real_node() and not node.left.is_real_node():
            physically_deleted = node.parent
            if node is self.get_root():
                self.root = None
                return 0
            if node.parent.left is node:
                node.parent.left = virtual_node
                virtual_node.parent = node.parent
            else:
                node.parent.right = virtual_node
                virtual_node.parent = node.parent
        elif not node.right.is_real_node() or not node.left.is_real_node():
            physically_deleted = node.parent
            if node is self.get_root():
                if node.right.is_real_node():
                    self.root = node.right
                else:
                    self.root = node.left
                self.root.set_size(1)
                self.root.set_height(0)
                self.root.set_bf(0)
                return 0
            if node.parent.left is node:
                if (node.left.is_real_node()):
                    node.parent.left = node.left
                    node.left.parent = node.parent
                else:
                    node.parent.left = node.right
                    node.right.parent = node.parent
            else:
                if (node.left.is_real_node()):
                    node.parent.right = node.left
                    node.left.parent = node.parent
                else:
                    node.parent.right = node.right
                    node.right.parent = node.parent
        else:
            successor = self.successor(node)
            physically_deleted = successor.parent
            if successor.parent.left is successor:
                successor.parent.left = successor.right
                successor.right.parent = successor.parent
            else:
                successor.parent.right = successor.right
                successor.right.parent = successor.parent
            successor.left = node.left
            successor.right = node.right
            successor.parent = node.parent
            node.left.parent = successor
            node.right.parent = successor
            if node is self.get_root():
                successor.parent = None
                self.root = successor
        node = physically_deleted
        while node is not None:
            new_height = max(node.left.height, node.right.height) + 1
            new_bf = node.left.get_height() - node.right.get_height()
            new_size = node.left.size + node.right.size + 1
            node.set_size(new_size)
            node.set_bf(new_bf)
            if abs(new_bf) < 2 and new_height == node.height:
                return num_of_operations
            elif abs(new_bf) < 2 and new_height != node.height:
                node.set_height(new_height)
                num_of_operations += 1
                node = node.parent
            else:
                if node.get_bf() == 2 and (node.left.get_bf() == 1 or node.left.get_bf() == 0):
                    self.right_rotate(node, node.parent)
                    num_of_operations += 1
                elif node.get_bf() == 2 and node.left.get_bf() == -1:
                    self.left_right_rotate(node)
                    num_of_operations += 2
                elif node.get_bf() == -2 and node.right.get_bf() == 1:
                    self.right_left_rotate(node)
                    num_of_operations += 2
                elif node.get_bf() == -2 and (node.right.get_bf() == -1 or node.right.get_bf() == 0):
                    self.left_rotate(node, node.parent)
                    num_of_operations += 1
                node = node.parent

    """returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
    def avl_to_array(self):
        result = []
        self.__in_order_rec(self.root, result)
        return result

    def __in_order_rec(self, node, arr):
        if node.is_real_node():
            self.__in_order_rec(node.left, arr)
            arr.append((node.key, node.value))
            self.__in_order_rec(node.right, arr)

    """returns the number of items in dictionary 
    
    @rtype: int
    @returns: the number of items in dictionary 
    """
    def size(self):
        return self.get_root().get_size()

    """splits the dictionary at a given node

	@type node: AVLNode
	@pre: node is in self
	@param node: The intended node in the dictionary according to whom we split
	@rtype: list
	@returns: a list [left, right], where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""
    def split(self, node):
        tr = AVLTree()
        tr.root = node.get_right()
        tl = AVLTree()
        tl.root = node.get_left()
        while node.get_parent() is not None:
            if node.get_parent().get_right() is node:
                to_add = AVLTree()
                to_add.root = node.get_parent().get_left()
                to_add.join(tl, node.get_parent().get_key(), node.get_parent().value)
                tl = to_add
            elif node.get_parent.get_left() is node:
                to_add = AVLTree()
                to_add.root = node.get_parent().get_right()
                tr.join(to_add, node.get_parent().get_key(), node.get_parent().get_value())
            node = node.get_parent()
        return [tl, tr]

    """joins self with key and another AVLTree

	@type tree: AVLTree 
	@param tree: a dictionary to be joined with self
	@type key: int 
	@param key: The key separting self with tree
	@type val: any 
	@param val: The value attached to key
	@pre: all keys in self are smaller than key and all keys in tree are larger than key,
	or the other way around.
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
    def join(self, tree, key, val):
        left_right_height_diff = self.get_root().get_height() - tree.get_root().get_height()
        new_root = AVLNode(key, val)
        node = None
        if left_right_height_diff > 1:
            # Traverse down the left tree until difference is not greater than zero
            node = self.get_root()
            if self.get_root().get_key() < key:
                while node.get_height() > tree.get_root().get_height():
                    node = node.get_right()
                node.get_parent().set_right(new_root)
                new_root.set_parent(node.get_parent())
                node.set_parent(new_root)
                new_root.set_left(node)

                new_root.set_right(tree.get_root())
                tree.get_root().set_parent(new_root)
            else:
                while node.get_height() > tree.get_root().get_height():
                    node = node.get_left()
                node.get_parent().set_left(new_root)
                new_root.set_parent(node.get_parent())
                node.set_parent(new_root)
                new_root.set_right(node)

                new_root.set_left(tree.get_root())
                tree.get_root().set_parent(new_root)
        elif left_right_height_diff < -1:
            # Traverse down the right tree until the difference is -1 or 0
            node = tree.get_root()
            if tree.get_root().get_key() < key:
                while node.get_height() > self.get_root().get_height():
                    node = node.get_right()
                node.get_parent().set_right(new_root)
                new_root.set_parent(node.get_parent())
                node.set_parent(new_root)
                new_root.set_left(node)

                new_root.set_right(self.get_root())
                self.get_root().set_parent(new_root)
            else:
                while node.get_height() > self.get_root().get_height():
                    node = node.get_left()
                node.get_parent().set_left(new_root)
                new_root.set_parent(node.get_parent())
                node.set_parent(new_root)
                new_root.set_right(node)

                new_root.set_left(self.get_root())
                self.get_root().set_parent(new_root)
        else:
            if tree.get_root().get_key() < key:
                new_root.set_left(tree.get_root())
                tree.get_root().set_parent(new_root)
                new_root.set_right(self.get_root())
                self.get_root().set_parent(new_root)
            else:
                new_root.set_right(tree.get_root())
                tree.get_root().set_parent(new_root)
                new_root.set_left(self.get_root())
                self.get_root().set_parent(new_root)


        # Now we connected the trio and we just traverse up fixing AVL criminals
        self.root = new_root
        self.root.set_bf(new_root.get_left().get_height() - new_root.get_right().get_height())
        self.root.set_height(max(new_root.get_left().get_height(), new_root.get_right().get_height()) + 1)
        self.root.set_size(self.get_root().get_size() + tree.get_root().get_size() + 1)
        node = self.root.get_parent()

        while node is not None:
            new_height = max(node.left.height, node.right.height) + 1
            new_bf = node.left.get_height() - node.right.get_height()
            new_size = node.left.size + node.right.size + 1
            node.set_size(new_size)
            node.set_bf(new_bf)
            if abs(new_bf) < 2 and new_height != node.height:
                node.set_height(new_height)
            else:
                if node.get_bf() == 2 and (node.left.get_bf() == 1 or node.left.get_bf() == 0):
                    self.right_rotate(node, node.parent)
                elif node.get_bf() == 2 and node.left.get_bf() == -1:
                    self.left_right_rotate(node)
                elif node.get_bf() == -2 and node.right.get_bf() == 1:
                    self.right_left_rotate(node)
                elif node.get_bf() == -2 and (node.right.get_bf() == -1 or node.right.get_bf() == 0):
                    self.left_rotate(node, node.parent)
            self.root = node
            node = node.parent


        return abs(left_right_height_diff)



    """compute the rank of node in the self

	@type node: AVLNode
	@pre: node is in self
	@param node: a node in the dictionary which we want to compute its rank
	@rtype: int
	@returns: the rank of node in self
	"""
    def rank(self, node):
        less_eq = node.get_left().get_size() + 1
        while node.get_parent() is not None:
            if node.get_parent().get_right() is node:
                less_eq += (node.get_parent().get_left().get_size() + 1)
            node = node.get_parent()
        return less_eq



    """finds the i'th smallest item (according to keys) in self

	@type i: int
	@pre: 1 <= i <= self.size()
	@param i: the rank to be selected in self
	@rtype: int
	@returns: the item of rank i in self
	"""
    def select(self, i):
        n = self.get_root()
        r = n.get_left().get_size() + 1
        while True:
            if r > i:
                n = n.get_left()
            elif r == i:
                return n
            else:
                n = n.get_right()
                i = i - r
            r = n.get_left().get_size() + 1

    """returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
    def get_root(self):
        return self.root

    """ performs a right rotation on a triplet of nodes
    @type node: AVLNode
    @param node: the node which is an AVL criminal.
    @returns: the new root after the rotation
    """
    def right_rotate(self, node, parent):
        new_root = node.get_left()
        new_root_right = node
        new_root_right.set_parent(new_root)
        new_root_right.set_left(new_root.get_right())
        new_root_right.get_left().set_parent(new_root_right)
        new_root.set_right(new_root_right)
        if parent:
            new_root.set_parent(parent)
            parent.left = parent.left if parent.left is not node else new_root
            parent.right = parent.right if parent.right is not node else new_root
            parent.set_height(max(parent.get_left().get_height(), parent.get_right().get_height()) + 1)
            parent.set_bf(parent.get_left().get_height() - parent.get_right().get_height())
            parent.set_size(parent.get_left().get_size() + parent.get_right().get_size() + 1)
        else:
            self.root = new_root
            new_root.parent = None
        node.set_height(1 + max(node.left.get_height(), node.right.get_height()))
        new_root.set_height(1 + max(new_root.left.get_height(), new_root.right.get_height()))
        node.set_size(1 + node.left.get_size() + node.right.get_size())
        new_root.set_size(1 + new_root.left.get_size() + new_root.right.get_size())
        node.set_bf(node.left.get_height() - node.right.get_height())
        new_root.set_bf(new_root.left.get_height() - new_root.right.get_height())
        return new_root

    """ performs a left rotation on a triplet of nodes
    @type node: AVLNode
    @param node: the node which is an AVL criminal
    @returns: the new root after the rotation
    """
    def left_rotate(self, node, parent):
        new_root = node.get_right()
        new_root_left = node
        new_root_left.set_parent(new_root)
        new_root_left.set_right(new_root.get_left())
        new_root_left.get_right().set_parent(new_root_left)
        new_root.set_left(new_root_left)
        if parent:
            new_root.set_parent(parent)
            parent.left = parent.left if parent.left is not node else new_root
            parent.right = parent.right if parent.right is not node else new_root
            parent.set_height(max(parent.get_left().get_height(), parent.get_right().get_height()) + 1)
            parent.set_bf(parent.get_left().get_height() - parent.get_right().get_height())
            parent.set_size(parent.get_left().get_size() + parent.get_right().get_size() + 1)
        else:
            self.root = new_root
            new_root.parent = None
        node.set_height(1 + max(node.left.get_height(), node.right.get_height()))
        new_root.set_height(1 + max(new_root.left.get_height(), new_root.right.get_height()))
        node.set_size(1 + node.left.get_size() + node.right.get_size())
        new_root.set_size(1 + new_root.left.get_size() + new_root.right.get_size())
        node.set_bf(node.left.get_height() - node.right.get_height())
        new_root.set_bf(new_root.left.get_height() - new_root.right.get_height())
        return new_root

    """ performs a left rotation and then right rotation
    @type node: AVLNode
    @param node: the node which is an AVL criminal
    """

    def left_right_rotate(self, node):
        child = node.get_left()
        self.left_rotate(child, node)
        self.right_rotate(node, node.get_parent())

    """ performs a right rotation and then left rotation
    @type node: AVLNode
    @param node: the node which is an AVL criminal
    """

    def right_left_rotate(self, node):
        child = node.get_right()
        self.right_rotate(child, node)
        self.left_rotate(node, node.get_parent())

    """ get successor of a node in tree
    @type node: AVLNode
    @param node: the node to find the successor of
    @returns: the successor of node
    """
    def successor(self, node):
        if node.right.is_real_node:
            curr_node = node.right
            while (curr_node.left.is_real_node()):
                curr_node = curr_node.left
            return curr_node
        parent = node.parent
        while parent is not None and node is parent.right:
            node = parent
            parent = node.parent
        return parent


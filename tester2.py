import random
import AVLTree

BASE = 1500
I = [1,2,3,4,5,6,7,8,9,10]

def get_left_max(t:AVLTree.AVLTree):
    curr = t.get_root().get_left()
    while curr.is_real_node():
        curr = curr.get_right()
    return curr.get_parent()

for i in I:
    arr1 = [i for i in range(BASE * 2**i)]
    random.shuffle(arr1)

    t1, t2 = AVLTree.AVLTree(), AVLTree.AVLTree()
    for k in arr1:
        t1.insert(k, 0)
        t2.insert(k, 0)

    max_left = get_left_max(t2)
    randNode = t1.search(random.choice(arr1))

    (_, join_cost_max, num_of_joins_max, max_join_max) = t2.split(max_left)
    (_, join_cost_rand, num_of_joins_rand, max_join_rand) = t1.split(randNode)

    print(f"-=-=-=-=- I = {i} =-=-=-=-=-=-")
    print(f"average join cost for random: {join_cost_rand/num_of_joins_rand}")
    print(f"max join cost for random: {max_join_rand}")
    print("")
    print(f"average join cost for max in left subtree: {join_cost_max/num_of_joins_max}")
    print(f"max join cost for max in left subtree: {max_join_max}")





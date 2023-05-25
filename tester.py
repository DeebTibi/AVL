import FingerTree
import random
BASE = 1500
I = [1,2,3,4,5]

def create_arr3(n):
    start, end = 0, 300
    res = []
    while end <= n:
        tmp = [i for i in range(end - 1, start - 1, -1)]
        res = res + tmp
        start = end
        end = end + 300
    return res

for i in I:
    length = BASE * 2 ** i
    keys1 = [i for i in range(length - 1, -1, -1)]
    keys2 = [i for i in range(length)]
    keys3 = create_arr3(length)
    random.shuffle(keys2)

    f1 = FingerTree.AVLTree()
    f2 = FingerTree.AVLTree()
    f3 = FingerTree.AVLTree()

    oper1 = 0
    repl1 = 0
    for k in keys1:
        operations = f1.insert(k, 0)
        repl = f1.size() - f1.rank(f1.search(k))
        oper1 += operations
        repl1 += repl

    oper2 = 0
    repl2 = 0
    for k in keys2:
        operations = f2.insert(k, 0)
        repl = f2.size() - f2.rank(f2.search(k))
        oper2 += operations
        repl2 += repl


    oper3 = 0
    repl3 = 0
    for k in keys3:
        operations = f3.insert(k, 0)
        repl = f3.size() - f3.rank(f3.search(k))
        oper3 += operations
        repl3 += repl

    print(f"======== RESULTS I = {i} ===============")
    print(f"Test 1) Replacements: {repl1}      Operations: {oper1}")
    print(f"Test 2) Replacements: {repl2}      Operations: {oper2}")
    print(f"Test 3) Replacements: {repl3}      Operations: {oper3}")


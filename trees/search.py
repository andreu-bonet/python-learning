class TreeNode:
    def __init__(self, data):
        self.data = data
        self.childrens = []


l0 = TreeNode(0)
l1 = TreeNode(1)
l2 = TreeNode(2)
l3 = TreeNode(3)
l4 = TreeNode(4)
l5 = TreeNode(5)
l6 = TreeNode(6)
l7 = TreeNode(7)

l0.childrens = [l1, l2, l3]
l1.childrens = [l4, l5]
l2.childrens = [l6]
l3.childrens = [l7]


def bfs(llista):
    if not llista:
        return
    for element in llista:
        print(element.data, end=", ")
    level_childrens = []
    for element in llista:
        level_childrens += element.childrens
    bfs(level_childrens)


def dfs(tree):
    print(tree.data, end=", ")
    for children in tree.childrens:
        dfs(children)


print("BFS: ", end="")
bfs([l0])
print()

print("DFS: ", end="")
dfs(l0)
print()

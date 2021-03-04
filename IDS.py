#This code is been implemented USING GRAPH 1
#Name: Sarthak Vaghela
#Student No.: 110005362

adj_lst = {
    "S" : ["A", "B"],
    "A" : ["B", "D"], 
    "B" : ["C", "D"],
    "C" : ["G", "D"],
    "D" : ["G"], 
    "G" : []
} 

'''adj_list = {
    "A":["B", "D", "S"],
    "B":["C", "D", "S"],
    "C":["B", "D", "G"],
    "D":["A", "B", "C", "G"],
    "G":["C", "D"],
    "S":["A", "B"]

}'''
dfs_traversal_output = []

print("The traversal path is shown below: ")

p = list()


def ndfs(cnode,dnation,adj_lst,mdepth,clist):
    print(cnode)
    clist.append(cnode)
    if cnode==dnation:
        return True
    if mdepth<=0:
        p.append(clist)
        return False
    for node in adj_lst[cnode]:
        if ndfs(node,dnation,adj_lst,mdepth-1,clist):
            return True
        else:
            clist.pop()
    return False

print(dfs_traversal_output)

def iterativeDDFS(cnode,dnation,adj_lst,mdepth):
    for i in range(mdepth):
        clist = list()
        if ndfs(cnode,dnation,adj_lst,i,clist):
            return True
    return False

if not iterativeDDFS("S","G",adj_lst,5):
    print("p is not available")
else:
    print("The exact path is: ")
    print(p.pop())
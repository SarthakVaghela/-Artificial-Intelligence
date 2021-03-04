#This code is done for GRAPH A ONLY
#Name: Sarthak Vanrajsinh Vaghela
#Std Num: 110005362
adj_l = {
    "A":["B", "D"],
    "B":["C", "D"],
    "C":["D", "G"],
    "D":["G"],
    "G":[],
    "S":["A", "B"]

}
'''adj_l = {
    "A":["B", "D", "S"],
    "B":["C", "D", "S"],
    "C":["B", "D", "G"],
    "D":["A", "B", "C", "G"],
    "G":["C", "D"],
    "S":["A", "B"]

}'''

c = {}
p = {}
output = []

for node in adj_l.keys():
    c[node] = "W"
    p[node] = None
    trav_time = [-1, -1]

def dfs_u(u):
    c[u] = "G"
    output.append(u)

    for v in adj_l[u]:
        if c[v] == "W":
            p[v] = u
            dfs_u(v)
    c[u] = "B"

dfs_u("S")
print("The traversal path is: ")
print(output)    

#The below section helps us to find the exact path
v = "G"
path = []

while v is not None:
    path.append(v)
    v = p[v]
path.reverse()
print("The exact path is: ")
print (path)
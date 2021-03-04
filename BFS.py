#this code is FOR GRAPH A
#Name : Sarthak Vanrajsinh Vaghela
#std num: 110005362

from queue import Queue

adj_list = {
    "A":["B", "D"],
    "B":["C", "D"],
    "C":["D", "G"],
    "D":["G"],
    "G":[],
    "S":["A", "B"]

}

'''adj_list = {
    "A":["B", "D", "S"],
    "B":["C", "D", "S"],
    "C":["B", "D", "G"],
    "D":["A", "B", "C", "G"],
    "G":["C", "D"],
    "S":["A", "B"]

}'''

vi = {}
p = {}
output = []
q = Queue()

for node  in adj_list.keys():
    vi[node] = False
    p[node] = None

s = "S"
vi[s] = True
q.put(s)
while not q.empty():
    u = q.get()
    output.append(u)

    for v in adj_list[u]:
        if not vi [v]:
            vi[v] = True
            p[v] = u
            q.put(v)

print("The traversal path is: ")
print(output)


#shortest path of from any node from source node
v = "G"
path = []

while v is not None:
    path.append(v)
    v = p[v]
path.reverse()
print("The exact path is: ")
print (path)












from dgraphclass import *
from tkinter import *
root = Tk()

w = Canvas(root, width=800, height=600)
w.pack()

widgetlist = []

g1 = Dgraph()

coords = []
vertices_save = {}
alphab = [i for i in range(50)]

def createcoor(event):
    coords.append((event.x, event.y))

    if len(coords) == 1:
        btn = Button(root, text=alphab[0], bg='white', command=lambda j=alphab[0]: clickbutton(j))
        btn.place(x=coords[0][0], y=coords[0][1])
        widgetlist.append(btn)
        vertices_save[alphab[0]] = (coords[0][0], coords[0][1])
        g1.addnode(alphab[0])
        del alphab[0]

    if len(coords) == 1:
        del coords[0]

w.bind("<Button-1>", createcoor)

entry3 = Entry(root)
entry3.pack(side=RIGHT)
label3 = Label(root, text='Distance entry')
label3.pack(side=RIGHT)

connecter = []
distsT = {}

def clickbutton(a):
    connecter.append(a)
    if len(connecter) == 2:
        g1.addarrow((connecter[0], connecter[1]), int(entry3.get()))
        x1 = vertices_save[connecter[0]][0]
        y1 = vertices_save[connecter[0]][1]
        x2 = vertices_save[connecter[1]][0]
        y2 = vertices_save[connecter[1]][1]
        w.create_line(x1, y1, x2, y2)
        distsT[(connecter[0], connecter[1])] = Label(root, text='{}'.format(g1.dists[(connecter[0], connecter[1])]))
        distsT[(connecter[0], connecter[1])].place(x=(x1 + x2)/2,y=(y1 + y2)/2+10)
        del connecter[0]
        del connecter[0]

def dijkstra(graph,begin):
    unvist = []
    distances = {}
    prev = {}
    for vertex in graph.nodes:
        distances[vertex] = 100000000
        prev[vertex] = None
        unvist.append(vertex)
    distances[begin] = 0
    while unvist:
        u = min(unvist,key=lambda x: distances[x])
        unvist.remove(u)
        for node in graph.neighbors_of(u):
            alt = distances[u] + graph.getLength(u, node)
            if alt < distances[node]:
                distances[node] = alt
                prev[node] = u
    return distances, prev

entry4 = Entry(root)
entry4.pack(side=RIGHT)
label4 = Label(root, text='Begin node of Dijkstra')
label4.pack(side=RIGHT)

def dijkstraexec():
    a, b = dijkstra(g1,int(entry4.get()))
    print(a)
    print(b)

btn2 = Button(root, text='Run Dijkstra', command=dijkstraexec)
btn2.pack(side=LEFT)

root.mainloop()
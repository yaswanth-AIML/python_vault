print("Hello! I am Your treasure_hunt Robot")
print("LETS Find treasure together")
map_room = {
    'A':['B','C'],
    'B':['D'],
    'C':['D'],
    'D':['G'],
    'G':[]
}
print("Our map:")
print("           A (START)")
print("          / \\")
print("         B   C")
print("          \\ /")
print("           D")
print("           |")
print("           G (TREASURE)")
def dfs(start, goal):
    order=[]
    visited=set()
    def explore(room):
        if room in visited:
            return False
        visited.add(room)
        order.append(room)
        if room==goal:
            return True
        for j in map_room[room]:
            if explore(j):
                return True
        return False
    explore(start)
    return order
order=dfs('A','G')
print("DFS CHECKED ROOMS:",order)
print("NUMBER OF ROOMS:",len(order))

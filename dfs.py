door_cost={
    ('A','B'):1,
    ('B','D'):1,
    ('A','C'):5,
    ('D','G'):1,
    ('C','D'):1,
}
def cost(path):
    total=0
    for i in range(len(path)-1):
        door=(path[i],path[i+1])
        total+=door_cost[door]
    return total
path1=['A','B','D','G']
path2=['A','C','D','G']
cost1=cost(path1)
cost2=cost(path2)
print("COST OF PATH 1 IS:",cost1)
print("COST OF PATH 2 IS:",cost2)
if cost1<cost2:
    best_path=path1
    best_cost=cost1
else:
    best_path=path2
    best_cost=cost2
print("BEST PATH IS :",best_path)
print("BEST COST IS:",best_cost)
print("\n" + "-" * 40)
print("RESULTS")
print("-" * 40)

print("Cheapest Path :", best_path)
print("Cost :", best_cost)

print("-" * 40)

print("\nWhat we learned:")
print(". BFS checks the nearest rooms first.")
print(". DFS explores one path deeply first.")
print(". Uniform Cost Search finds the cheapest path.")

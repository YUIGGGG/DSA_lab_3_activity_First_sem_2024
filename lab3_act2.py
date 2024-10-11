list1 = [1, 2, 3]
list2 = ["mark", "alice", "john"]

for list1, list2 in zip(list1, list2):
    print(list1, f'"{list2}"')

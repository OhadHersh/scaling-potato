import pandas as pd
file = open(input("Enter a file path: "), 'r')
task = input("Enter a task: ").lower()
if task == 'sort':
    a = (file.read().lower().split())
    print (sorted(pd.Series(a).drop_duplicates().tolist()))
if task == 'rev':
    for i in file.read().splitlines():
        print(i[::-1])
if task == 'last':
    num_of_lines = int(input("Enter a number: "))
    lines = file.read().splitlines()
    print("\n".join(lines[-num_of_lines:]))
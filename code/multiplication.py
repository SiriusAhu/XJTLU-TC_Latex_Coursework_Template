# 9*9 multiplication table

ROW = 9
COL = 9

for i in range(1, ROW+1):
    for j in range(1, COL+1):
        print(f"{i}*{j}={i*j}", end="\t")
    print("")
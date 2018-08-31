array1=[[1,2],[2,3],[],[2,4],[6],[9]]
for x in (array1):
    if len(x) == 0:
        array1.remove(x)
        print(array1)
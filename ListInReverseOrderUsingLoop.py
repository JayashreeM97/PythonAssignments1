# 5.Print list in reverse order using a loop
list=[10,20,30,40,50,60,70]
newList=[]
for i in list:
    newList=[i]+newList
print(newList)
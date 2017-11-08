outlist = []
for i in list(range(2000,3201)):
    if ((i % 7) == 0):
        if ((i % 5) != 0):
            outlist.append(i)
print(outlist)
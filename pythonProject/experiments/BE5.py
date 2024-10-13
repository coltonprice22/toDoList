waitingList = ['sen', 'ben', 'john']
waitingList.sort()

for i,j in enumerate(waitingList):
    row = f'{i+1}.{j.capitalize()}'
    print(row)
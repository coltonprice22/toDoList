filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

filenamesList = []
for i in filenames:
    i = i.replace('.','-',1)
    print(i)

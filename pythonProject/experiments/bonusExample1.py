exitVar = 0
while exitVar == 0:
    bookTitle = input("insert book title: ")
    bookChar = len(bookTitle)
    print('characters: ',bookChar,'\n')
    if bookChar <= 100:
        exitVar = 1
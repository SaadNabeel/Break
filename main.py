st1=input("Enter any string:")
ch=input("Enter a character to search:")
for c in st1:
    if c==ch:
        print(ch,"found")
        break
    else:
        print(ch,"not found")
#File Handling
b = input("Enter file name : ")
fo = open(b , "a")
a = input("Enter Text :")
fo.write(a)
fo.close()


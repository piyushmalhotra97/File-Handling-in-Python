fo = open("Hello1.txt" , "a+")
fo.write("hello")
fo.seek(2,0)
a = fo.read()
print(a)
fo.close()

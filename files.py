f = open ("test.txt")
f = open ("C:\Users\KC\OneDrive\Desktop\Demo\PythonDemo")
f = open ("test.txt", mode='r', encoding='utf-8')
f.close()

try:
    f = open("text.txt", encoding= 'utf-8')
finally:
    f.close()

with open("test.txt", 'w', encoding='utf-8') as f:
    f.write("my first file\n")

f = open("test.txt", 'r', encoding='utf-8')
f.read(4) #read the first 4 data
'This'
f.read() #read in the rest till end of file
f.tell() #get the current file position
f.seek(0)

print(f.read())

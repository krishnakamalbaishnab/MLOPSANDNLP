with open('test.txt','r') as file:
    content = file.read()
    print(content)


#let's read the content of the file line by line

with open('test.txt','r') as file:
    for line in file:
        print(line)

#let's remove the extra space between the lines using stip functions
        print(line.strip())
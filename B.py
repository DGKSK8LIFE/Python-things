with open("B-large-practice.in") as f:
    content = f.readlines()
content = [x.strip() for x in content] 
print(content)

i = 0
print("content[0-5]: ", content[1:6])
with open("B-large-practice.out", "w") as f:
    for x in content[1:]:
        print(x)
        x = x.split(" ")
        print(x)
        x = x[-1::-1]
        print(x)
        x = ' '.join(x)
        print(x)
       
        i += 1
        f.write('Case #' + str(i) + ': ' + x + '\n')
        
        
        
     




a = 7
b = 8
c = 0
d = 1
print(a,b,c,d)

def playWithAandB(a, b): 
    global c
    c = a+b 
    d = a-b 
    print(a,b,c,d) 
    return c + d

a = 6      
c = playWithAandB(a,d) + b - c

def playWithCandD(c, d): 
    a = c-d 
    global b
    b = c+d 
    print(a,b,c,d) 
    return a - b
    
c = 2
a = playWithCandD(c,b) - a + d

d = playWithAandB(d,c) - playWithCandD(a,b) + c - d

print(a,b,c,d)

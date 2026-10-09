# # A = [20, 30, 40, 50, 60]
# # print(type(A))
# # A[0] = 67
# # print(A[0])
# # print(A[1])
# # print(A[2])
# # print(A[3])

# # b = (10,20,30,40)

# # print(b)
# # print(type(b))

for i in range(1,4):
    for j in range(1,10):
        print("*" , end=" ")
    print()

for i in range(1,6):
    for j in range(1,6):
        print(j , end=" ")
    print("\n")

num = 1
for i in range(1,6):
    for j in range(1,6):
        print(num ," ", end=" ")
        num += 1
    print("\n")

for i in range(1,10):
    for j in range(i):
        print("* " , end=" ")
    print("\n")

for i in range(1,10):
    for j in range(i):
        print(i , end=" ")
    print("\n")

num = 0
for i in range(1,10):
    for j in range(i):
        print(num * 5, end=" ")
        num +=1
    print("\n ")



for i in range(1, 6):    
    for j in range(i):        
        print("*", end=" ")    
    print()

print("* * * * * * ")



for i in range(5, 0, -1):    
     for j in range(i):        
        print("*", end=" ")    
     print()

for i in range(5, 0, -1):    
     for j in range(i):        
        print(j+1, end=" ")    
     print()

num = 0

for i in range(1,6):    
    for j in range(5-i):        
        print(" ", end=" ")    
    for k in range(2*i-1):    
     print("*", end=" ")  
    print()

for i in range(5,0,-1):    
    for j in range(5-i):        
        print(" ", end=" ")    
    for k in range(2*i-1):    
     print("*", end=" ")  
    print()
   

for i in range(6) :
    print(i)
    if (i == 3) :
        break

    

for i in range(6) :
    print (i)
    if (i == 3) :
        continue

    

for i in range(6) :
    if (i == 3) :
        pass

    print (i)

for i in range(1, 6):    
    for j in range(i):                             
        print((i + j) % 2, end=" ")
    print()




n = int(input("Введите n\n"))

one = [1] * n
com = []
print(one)

for i in range(0, int(n/2)):
    one[i] += 1
    one.pop()
    print(one)

    com.append(one)



#print(one)

#one[1] +=1
#com.append(one)
    
#print(one)

#print(com)

#for i in range(0, int(n/2)):
 #   composition[i] +=1
  #  composition.pop()
   # result.append(composition[i])
    #print(composition)



#while (composition[0] + composition[1] != n):
 #   composition[0] +=1
  #  result.append(composition)
   # composition.pop()

    #print(composition)

#print(result)

    

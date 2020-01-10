str = input("Введиет строку\n")

def Parentheses (str, open = len(str), close = 0):
        
    if (str.find('(', 0, open) !=-1)  and (str.rfind(')', close, len(str)) !=-1):
       
       left = str.rfind('(',0 , open)
       right = str.find(')',close, len(str))
                
       return str[ left + 1 : right ] #, Parentheses(str, left, right)
     
    pass
    
    

print(Parentheses(str))

#print(str.find('*'))
#print(str.rfind('('))




def test(expression:str,oparetor:dict):
        for char in expression:
            if (char not in oparetor.keys()) and  (not char.isalnum()) and (char not in ["(",")"]):
                print(f"syntax error  element  in {char} ")
                return False
        for i in range(len(expression)+1):
            if not ((expression[i]  in  oparetor.keys())or  (expression[i].isalnum) ):
                print(f"syntax error  element {i+1} ")
                return False
            if  (expression[i]  in oparetor.keys()):
                print(f"syntax error in element {i+1}")
                return False
            if (not expression[i].isalnum()) and (expression[i] not in oparetor.keys()):
                print(f"syntax error in element {i+2}")
                return False
            if expression[i] in oparetor.keys()  and expression[i+1] in oparetor.keys():
                print(f"syntax error in element {i+2}")
                return False
            if expression[i].isalnum()  and expression[i+1].isalnum():
                print(f"syntax error in element {i+2}")
                return False
            if (expression[i] in oparetor.keys()  and expression[i+1] ==')') or expression[0]  in oparetor.keys() or expression[-1]  in oparetor.keys() :
                print( f"syntax error in element {i+2}") 
                return False
            return True

def posfix(expression:str):
    oparetor = {'>': 1, '=': 1, '&': 2, '|': 2, '!': 3}
    stack = []
    result = ''
   


    for char in expression:
        if char.isalnum():
            result += char
        
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()  
 
            
        else:
            
            while stack and stack[-1] != '(' and oparetor[char] <= oparetor.get(stack[-1], 0):
                result += stack.pop()
            stack.append(char)

    while stack:
        result += stack.pop()

    return result

if __name__=="__main__":

    seq= input("Please enter: ")


        
    print("Normal  : ",seq)
    print(" \n\n Postfix : ",posfix(seq))
    
# print(f'result : {int(str(seq))}')
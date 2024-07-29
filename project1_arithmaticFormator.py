# Arithmatic Formator

# Functions

def arithmetic_arranger(list,display_answers=False):
    if len(list)> 5: # condition1_many problems
        return 'Error: Too many problems.'
    else:
        first_line=""
        second_line=""
        dash_line=""
        answer_line=""
        for problem in list:
            try:
                operands,operator =seperation(problem) # function call
                answer=str(total(operands,operator)) # function answer call
            except ValueError:
                return seperation(problem)
             
            #Arrangement
            width = max(len(operands[0]), len(operands[1])) + 2
            
            first_line += operands[0].rjust(width) + "    "
            second_line += operator + " " + operands[1].rjust(width - 2) + "    "
            dash_line += "-" * width + "    "
            answer_line += answer.rjust(width) + "    "
        
        arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + dash_line.rstrip() 
        if display_answers:
            arranged_problems += "\n" + answer_line.rstrip()
    
    return arranged_problems
        
        
            
def seperation(problem):
    
    parts=problem.split()
    
    operands=[]
    operator=0
    
    #print(parts)
    for part in parts:# seperation 
        if part in ('+','-'):
            operator=part
        elif part in ('*','/'): # conditon2_operator
            return "Error: Operator must be '+' or '-'."
            
        else:
            try:
                int(part)  # Condition3_integer
                if len(part) > 4: # condition4_length of integer
                    return ('Error: Numbers cannot be more than four digits.')
                      
                else:
                    operands.append(part)
            except ValueError: 
                return 'Error: Numbers must only contain digits.'
                
        
    return operands,operator
            
            
def total(operands,operator):
    total=0
    if operator=='+':
        total = int(operands[0]) + int(operands[1])
    elif operator=='-':
        total = int(operands[0]) - int(operands[1])
    return total      


    
    


#problem -tests
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))

print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"], True))
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"], True))

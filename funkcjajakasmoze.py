import re

def transform(formula):
    a = ''
    if "->" in formula:
        a =  "~( "+formula[0]+" ) v "+formula[-1]
    
    elif "<->" in formula:
        a = "( ~( "+formula[0], " ) v "+formula[-1]+" ) & ( ~( "+formula[-1]+") v"+formula[0]+" )"
    
    elif "~" in formula and "&" in formula:
        a = "~( "+ formula[0]+ " ) v ~( "+ formula[-1]+ " )"
    
    elif "~" in formula and "v" in formula:
        a = "~( "+ formula[2]+ " ) & ~( "+ formula[-2]+ " )"
    
    elif "~~" in formula:
        a = formula.replace('~~','')
    
    elif re.search('([a-z()]+)&([a-z()]+)v', formula):
        a = "( "+formula[1]+" v "+ formula[6]+ " ) & ( "+ formula[3]+ " v "+ formula[6]+ " )"
    
    elif re.search('([a-z()]+)v([a-z()]+)&', formula):
        a = "( "+ formula[1]+ " & "+ formula[6]+ " ) v ( "+ formula[3]+ " & "+ formula[6]+ " )"
    
    elif "v" in formula and formula[0] == formula[-1]:
        a = formula[0]
    
    elif "&" in formula and formula[0] == formula[-1]:
        a = formula[0]
    
    elif "v~" in formula and "&" in formula and formula[1] == formula[4]:
        a = formula[7]
    
    elif "&~" in formula and "v" in formula and formula[1] == formula[4]:
        a = formula[7]

    else: 
        a = formula
    return a
    
def transform2(formula):
    a = ''
    if "->" in formula:
        a =  "~( "+formula[0]+" ) v "+formula[-1]
    
    elif "<->" in formula:
        a = "( ~( "+formula[0], " ) v "+formula[-1]+" ) & ( ~( "+formula[-1]+") v"+formula[0]+" )"
    
    elif "~" in formula and "&" in formula:
        a = "~( "+ formula[0]+ " ) v ~( "+ formula[-1]+ " )"
    
    elif "~" in formula and "v" in formula:
        a = "~( "+ formula[2]+ " ) & ~( "+ formula[-2]+ " )"
    
    elif "v" in formula and formula[0] == formula[-1]:
        a = formula[0]
    
    elif "&" in formula and formula[0] == formula[-1]:
        a = formula[0]
    
    elif "v~" in formula and "&" in formula and formula[1] == formula[4]:
        a = formula[7]
    
    elif "&~" in formula and "v" in formula and formula[1] == formula[4]:
        a = formula[7]

    else: 
        a = formula
    return a

print("Hello, give the A part of the formula: ")

A = input()

print("Now give the operator: ")

operator = input()

print("Now give B part of the formula: ")

B = input()

if(len(A) < 3):
    b = transform(B)
    print(A, operator, b)
    table = [A, operator, b]
    ans = transform2(table)
    print(ans)
else:
    a = transform(A)
    b = transform(B)
    print( a , operator, b )
    table = [a, operator, b]
    ans = transform2(table)
    print(ans)

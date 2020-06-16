import re

def transform(formula):

    if "->" in formula:
        print("~( ", formula[0], " ) v", formula[3])
    
    elif "<->" in formula:
        print("( ~( ", formula[0], " ) v ", formula[-1], " )& ( ~( ", formula[-1], ") v", formula[0], " )")
    
    elif "~" in formula and "&" in formula:
        print("~( ", formula[0], " ) v ~( ", formula[-1], " )")
    
    elif "~" in formula and "v" in formula:
        print("~( ", formula[2], " ) & ~( ", formula[-2], " )")
    
    elif "~~" in formula:
        print(formula.replace('~~',''))
    
    elif re.search('([a-z()]+)&([a-z()]+)v', formula):
        print("( ", formula[1], " v ", formula[6], " ) & ( ", formula[3], " v ", formula[6], " )")
    
    elif re.search('([a-z()]+)v([a-z()]+)&', formula):
        print("( ", formula[1], " & ", formula[6], " ) v ( ", formula[3], " & ", formula[6], " )")
    
    elif "v" in formula and formula[0] == formula[-1]:
        print(formula[0])
    
    elif "&" in formula and formula[0] == formula[-1]:
        print(formula[0])
    
    elif "v~" in formula and "&" in formula and formula[1] == formula[4]:
        print(formula[7])
    
    elif "&~" in formula and "v" in formula and formula[1] == formula[4]:
        print(formula[7])

    else: 
        print(formula)

print("Hello, give the A part of the formula: ")

A = input()

print("Now give the operator: ")

operator = input()

print("Now give B part of the formula: ")

B = input()

if(len(A) < 3):
    print(A, operator, end=" ")
    transform(B)
else:
    transform(A)
    print(operator, end=" ")
    transform(B)

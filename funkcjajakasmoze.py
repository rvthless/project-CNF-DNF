def transform(formula):

    if(formula[1] == "-" and formula[2] == ">"):
        print("~(", formula[0], ") v ", formula[3])
    
    elif "<->" in formula:
        print("( ~(", formula[0], ") v ", formula[-1], ") & ( ~(", formula[0], ") v ", formula[-1], " )")
    
    elif(formula[0:3] == "~" and formula[5:8] == "&"):
        print("~(", formula[4], ") v ~(", formula[8], ")")
    
    elif(formula[0] == "~" and formula[5] == "v"):
        print("~(", formula[4], ") & ~(", formula[6], ")")
    
    elif(formula[0:2] == "~~"):
        print(formula[2])
    
    elif(formula[2:5] == "&" and formula[7] == "v"):
        print("( ", formula[1], " v ", formula[8], " ) & ( ", formula[5], " v ", formula[8], " )")
    
    elif(formula[2] == "v" and formula[5:8] == "&"):
        print("( ", formula[1], " & ", formula[8], " ) v ( ", formula[3], " & ", formula[8], " )")
    
    elif(formula[1] == "v" and formula[0] == formula[2]):
        print(formula[0])
    
    elif(formula[1] == "&" and formula[0] == formula[2]):
        print(formula[0])
    
    elif(formula[2:6] == "v~" and formula[8:11] == "&"):
        print(formula[11])
    
    elif(formula[2:8] == "&~" and formula[10] == "v"):
        print(formula[11])

    else: 
        print(formula)

print("Hello, give the A part of the formula: ")

A = input()

print("Now give the operator: ")

operator = input()

print("Now give B part of the formula: ")

B = input()

if(len(A) < 3 and len(B) < 3):
    full = A + ' ' + operator + ' ' + B
    transform(full)
elif(len(A) < 3):
    print(A, operator, end=" ")
    transform(B)
else:
    transform(A)
    print(operator, end=" ")
    transform(B)

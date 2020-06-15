def transform(formula):
    
    x = formula.split()
    
    if "->" in x:
        print("NOT(", formula[0], ") OR ", formula[-1])
        
    if "<->" in x:
        print("( NOT(", formula[0], ") v ", formula[-1], ") AND ( NOT(", formula[-1], ") v ", formula[0], " )")
    
    if "NOT" and "AND" in x:
        print("NOT(", formula[4], ") v NOT(", formula[8], ")")
    
    else:
        print(formula)


print("Hello, give the A part of the formula: ")

A = input()

print("Now give the operator: ")

operator = input()

print("Now give B part of the formula: ")

B = input()


transform(A)
print(operator, end=" ")
transform(B)

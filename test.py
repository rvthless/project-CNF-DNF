import re
def transform(formula):
    
    x = formula
    
    if "->" in x:
        print("~(", formula[0], ") v ", formula[-1])
        
    if "<->" in x:
        print("( ~(", formula[0], ") v ", formula[-1], ") ^ ( ~(", formula[-1], ") v ", formula[0], " )")
    
    if "~" and "^" in x:
        print("~(", formula[4], ") v ~(", formula[8], ")")
    
    if "~~" in x:
        print(x.replace('~~',''))
    
    if "^" in x:
        
    
    else:
        print(formula)


print("Hello, give the A part of the formula: ")

b = input()

table = re.split(r'[^->*,"<->","AND","NOT","OR",(*,*)]', b)

table2 = re.split(r'["->","<->","AND","NOT","OR"]', b)

table3 = re.split(r'[(*,*),\b]', b)


print(table)
print(table2)
print(table3)

transform(table3[0])

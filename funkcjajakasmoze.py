print("Hello, give the A part of the formula: ")

A = input()

print("Now give the operator: ")

operator = input()

print("Now give B part of the formula: ")

B = input()

formula = B

if(formula[1] == "-" and formula[2] == ">"):
    print("NOT(", formula[0], ") v ", formula[3])
    
if(formula[1] == "<" and formula[2] == "-" and formula[3] == ">"):
    print("( NOT(", formula[0], ") v ", formula[4], ") AND ( NOT(", formula[4], ") v ", formula[0], " )")
    
if(formula[0:3] == "NOT" and formula[5:8] == "AND"):
    print("NOT(", formula[4], ") v NOT(", formula[8], ")")
    
if(formula[0:3] == "NOT" and formula[5] == "v"):
    print("NOT(", formula[4], ") AND NOT(", formula[6], ")")
    
if(formula[0:6] == "NOTNOT"):
    print(formula[6])
    
if(formula[2:5] == "AND" and formula[7] == "v"):
    print("( ", formula[1], " v ", formula[8], " ) AND ( ", formula[5], " v ", formula[8], " )")
    
if(formula[2] == "v" and formula[5:8] == "AND"):
    print("( ", formula[1], " AND ", formula[8], " ) v ( ", formula[3], " AND ", formula[8], " )")
    
if(formula[1] == "v"):
    print(formula[0])
    
if(formula[1:4] == "AND"):
    print(formula[0])
    
if(formula[2:6] == "vNOT" and formula[8:11] == "AND"):
    print(formula[11])
    
if(formula[2:8] == "ANDNOT" and formula[10] == "v"):
    print(formula[11])

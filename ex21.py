def add(a,b):
    print "ADDING %d+%d"%(a,b)
    return a+b

def subtract(a,b):
    print "SUBTRACT %d-%d"%(a,b)
    return a-b

def multiply(a,b):
    print "MULTIPLY %d*%d"%(a,b)
    return a*b

def divide(a,b):
    print "DIVIDE %d/%d"%(a,b)
    return a/b

print "please input the expressions:"
x1=raw_input()
sign1=raw_input()
x2=raw_input()

if sign1=='+':
    add(x1,x2)

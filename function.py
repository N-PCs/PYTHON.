#function
# eg: print , type ,input  , len , bin ..
#all this functions are library functions i.e they are available in library and can be accessed at any time 

# since all the library functions can't be used for every task
# so we create our own functions
# syntax to create function
#def function_name(parameters):
#                 body / conditions
#return

def hello():
    print("hello")
    
def oddevens(a):
    if a%2==0:
        print("even number")
    else:
        print("odd number")
""" OR """  #''' ''' is used for multiline comments

def oddeven():                     #function definition
    a=int(input("enter a number"))
    if a%2==0:
        print("even number")
    else:
        print("odd number")
        

        

##Airthmetic program
##--Create function for multiply number with constant number 3 and
##result should be 9.

def mult(x):
    constant=3
    assert x==3,"Wrong value of x."
    return x*constant
print(mult(3))

##--Create a function for Adding two numbers and result should be 4

def add(a,b):
    Add_res=a+b
    assert (Add_res==4),"Wrong values of either a or b."
    return Add_res
print(add(1,3))

##--Create function for adding numbers of data structure "List",Result
##should be 12
numbers=[1,2,3,6]
def sumoflist(somelist):
    sum_num=0
    for element in somelist:
        sum_num += element
    return sum_num
numbers=[1,2,3,6]
print(sumoflist(numbers))


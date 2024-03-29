# Write a function is_triangular that meets the specification below. 
# A triangular number is a number obtained by the continued summation 
# of integers starting from 1. For example, 1, 1+2, 1+2+3, 1+2+3+4, etc.,
#  corresponding to 1, 3, 6, 10, etc., are triangular numbers.

# def is_triangular(k):
#     """
#     k, a positive integer
#     returns True if k is triangular and False if not
#     """
#     #YOUR CODE HERE

# Paste your entire function, including the definition, in the box below. 
# Do not leave any debugging print statements.

def is_triangular(k):
    x=1
    summ=1
    while True:
        if summ==k:
            return True
        elif summ>k:
            return False
        elif summ<k:
            x+=1
            summ+=x
        else: 
            print (summ,k,x)
            break
print(is_triangular(1))
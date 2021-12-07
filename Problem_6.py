# *** review what a docstring is and how it effects help()

# Write a function that satisfies the following docstring:

# def largest_odd_times(L):
#     """ Assumes L is a non-empty list of ints
#         Returns the largest element of L that occurs an odd number 
#         of times in L. If no such element exists, returns None """
#     # Your code here
# For example, if

# largest_odd_times([2,2,4,4]) returns None
# largest_odd_times([3,9,5,3,5,3]) returns 9
# Paste your entire function, including the definition, in the box below. 
# Do not leave any debugging print statements.


def largest_odd_times(L):
    x=-1
    L=sorted(L)
    for i in range (0,len(L)):
        y=L[x]
        if L.count(y)%2!=0:
            return(L[x])
        elif i==len(L)-1 and L.count(y)%2==0:
            return(None)
        x-=1
print(largest_odd_times([2,2,4,4,10,10,10,1]))

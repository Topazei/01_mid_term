# Suppose x = "pi" and y = "pie". The line of code x, y = y, x will
# swap the values of x and y, resulting in x = "pie" and y = "pi".
# True  [ ]
# False [ ]

#--------------------------------------------------------------------

# Suppose x is an integer in the following code:
def f(x):
    while x > 3:
        f(x+1)

# For any value of x, all calls to f are guaranteed to never terminate.
# True  [ ]
# False [ ]

#--------------------------------------------------------------------

# A Python program always executes every line of code written at least once.
# True  [ ]
# False [ ]

#--------------------------------------------------------------------

# Suppose you have two different functions that each assign a variable called x.
#  Modifying x in one function means you always modify x in the other function for any x.

# True  [ ]
# False [ ]

#--------------------------------------------------------------------

# The following code will enter an infinite loop for all values of i and j.
while i >= 0:
    while j >= 0:
        print(i, j)

# True  [ ]
# False [ ]

#--------------------------------------------------------------------

# *** cover this

# Assume f() is defined. In the statement a = f(), a is always a function.
# True  [ ]
# False [ ]

#--------------------------------------------------------------------

# *** cover this

# Consider the following function.
def f(x):
    a = []
    while x > 0:
        a.append(x)
        f(x-1)

# A new object of type list is created for each recursive invocation of f.
# True  [ ]
# False [ ]

#--------------------------------------------------------------------

# A tuple can contain a list as an element.
# True  [ ]
# False [ ]

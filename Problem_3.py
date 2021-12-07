# Examine the following code snippet:

stuff  =[ ( "iBoy", "iGirl", "iQ", "iC","iPaid","iPad") ]
for thing in stuff:
    if thing == 'iQ':
        print("Found it")

# Select all the values of the variable "stuff" that will make the 
# code print "Found it".


# ["iBoy", "iGirl", "iQ", "iC","iPaid","iPad"] yes
# ("iBoy", "iGirl", "iQ", "iC","iPaid","iPad") yes
# [ ( "iBoy", "iGirl", "iQ", "iC","iPaid","iPad") ] NO
# ( [ "iBoy", "iGirl", "iQ", "iC","iPaid","iPad" ], ) NO
# ["iQ"] YES
# "iQ" NO


# *** upper() and lower()

# Write a Python function that takes in a string and prints out a version 
# of this string that does not contain any vowels, according to the 
# specification below. Vowels are uppercase and lowercase 
# 'a', 'e', 'i', 'o', 'u'.

# For example, if s = "This is great!" then print_without_vowels 
# will print Ths s grt!. If s = "a" then print_without_vowels 
# will print the empty string .

# def print_without_vowels(s):
#     '''
#     s: the string to convert
#     Finds a version of s without vowels and whose characters appear in the 
#     same order they appear in s. Prints this version of s.
#     Does not return anything
#     '''
#     # Your code here

#def print_without_vowels(s):
#     x=0
#     s=s.lower()
#     for b in s:
#         print (b)
#         if b=="a" or b=="i" or b=="u" or b=="o" or b=="e":
#             n=s[0:x]+s[x+1:]
#             print(n)
#         print(x)
#         x+=1
#     print (n)

# print_without_vowels("HEllo")



# def print_without_vowels(s):
    # x=0
# s="hello"
# for b in s:
#     print(b)


def print_without_vowels(s):
    s=s.lower()
    n=""
    x=0
    for b in s:
        if b!="a" and b!="i" and b!="u" and b!="o" and b!="e":
            n+=s[x]
        x+=1
    print(n)
print_without_vowels('SOS')

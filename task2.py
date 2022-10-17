#Program to reverse a string iteratively and recursively

#Reverses the string iteratively
def reverseI(string):
    #length of the string
    strlen = len(string)
    #empty string
    nstr = ''
    i = strlen - 1
    while i >= 0:
        nstr += string[i]
        i -= 1
    return nstr

#recursive function to reverse a string
def reverseR(string):
    #base case
    #if the length of the string is equal to 0 return the string
    if len(string) == 0:
        return string
    #else recursively call the reverse function to slice part of the string 
    #except for the first character and add the first character to the end of the sliced string
    else:
        return reverseR(string[1:]) + string[0]

string = input("Enter a word: ")
choice = input("Reverse string iteratively(I) or recursivel(R): ")

#if choice is r or R then the string is reversed recursively
if choice == "R" or choice == "r":
    print(reverseR(string))

#else if choice is i or I the string is reversed iteratively
elif choice == "I" or choice == "i":
    print(reverseI(string))

#Program to find the most frequent integer in an array

#function to find the most frequent integer in an array
#set gets the unique value in the list
#max finds the element of the array that has the most occurences
def mostOcc(numbers):
    return max(set(numbers), key=numbers.count)

list1 = [1, 2, 2, 3, 3, 3]

print("Most frequent integer:", mostOcc(list1))


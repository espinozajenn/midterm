# Write a function called divisible_by_7. 
# This function must take an integer as a parameter.
# This function must return True if the passed integer
# is divisible by 7 or false if not.
# Note: you should not prompt the user for input. 
def divisible_by_7(x):
    if  % 7 ==0:
        return True
    return False 

# Write a function called compare_it that takes two parameters. 
# You should first test if both parameters are integers.
# If not, return False
# Then you should test if the parameters are equal.
# If they are not, return False
# Finally, test if the parameters are greater than zero.
# If they are not, return False.
# If all of these tests pass, return True.
def compare_it(x,y): 
    # test they're integers (negative test)
    if not isinstance(x, int) and not isinstance (y,int):
    return False
    # test if equal (negative test)
    if not x == y
    return False
    # test if they're greater than zero (negative test)
    if x < = 0 and y < =0:
    return False
    # all tests pass 
    return True 

# Write a function called keyword_counter that takes three parameters
# Parameter one should be a list of words.
# The second should be set to None by default, and could hold a string to search.
# The third should be set to None by default, and could hold a filename to search.
# If a string and a filename are both passed to the program, the program should 
# return None.
# If the function is passed a string in the second parameter, then it should
# search the string.
# If the function is passed a filename in the third parameter, then it should
# read the file and search the contents of the file.
# Unless the function is passed both a string and a filename, your function 
# must return a dictionary with the keywords as the key and the count of 
# occurrences of that keyword as the value as follows:
# output = {'word': 3, 'second': 4} 
# assuming word is one of the search words and occurs 3 times. 
# Since this is tricky, I've given you the code to read from a file that you'll
# need to include in your function.
# NOTE: Your test should not be case sensitive so if
# one of the words is "fish" your function should count 
# "fish", "Fish", "FISH" or any other combination of 
# capitalization as an occurrence. 
def keyword_counter(words, search_string = None, filename = None):
    if (search_string == None and filename == None) or (search_string !=N
        return None
   # search a string for words and count them.
   for i in range (len(words)):
        counter = text.count (words [i])

    if seach_string !=None: 
        text = search_string

        else:
            with open(file_name, "r") as f:
                 text = f.read().replace("\n", " ")

    output = dict()

    for word in words: 
        word = word.lower()
        output[word] = text.count(word)
        
    return = output 





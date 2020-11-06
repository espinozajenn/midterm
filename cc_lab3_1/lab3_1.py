# As you work through this file, make sure that you are on the correct
# tab level. I've included all of your TODO's inside of functions for tests.
# This means everything needs to be tabbed over 1 level, at least. 

def sums():
   
   # Initialize a variable called first_sum and store the sum of 
   # 2 and 2
   first_sum = 2 + 2
   # Store to first_sum the value of first_sum times 10
   first_sum = first_sum * 10 
   # Initialize a variable called secret and assign it the value 
   # of first_sum plus 2
   secret = first_sum +2
   return secret

def string_manip(first_name):

   # Initialize a variable called name and assign it the 
   # parameter.
   name = first_name
   #Use builtin string functions and slices to replace None with 
   # the appropriate manipulation of your name. I've done the first one.
   all_caps = name.upper() 
   all_lowercase = name.lower()
   first_five_letters = name[:5]
   last_two_letters = name[-2:]

   return [all_caps, all_lowercase, first_five_letters, last_two_letters]

def greeter_bot():

   # Use the input() function to prompt the user for their name.
   # Then assign the value to a variable called name and print a greeting.
   # I have started it for you, but you need to modify the input and 
   # print functions.
   # Hint: to get the test to pass, the greeting should be "Hello, input name"
   fname = input("Hey, buddy, what is your name? ") 
   print("Hello, {}!" .format(fname)


def temp_calculator():

   # Write code that prompts the user for a temperature in degrees
   # fahrenheit and prints the equivalent temperature in degrees celsius.
   # The formula is C = (F - 32) * (5/9). 
   f = input("What is the temperature that you want to convert?")
   c = (f - 32) * (5/9)
   print(c)

def equitable_bill_splitter():
   
   # Read the following code and add comments to each line explaining what
   # it does. To write a comment, begin the line with an octothorpe (hashtag, #)
   # prompt the user for how many people are paying 
   people = int(input("How many people are paying? "))
   # create a list to store the salaries
   salaries = []
   # create a variable to store a total salary.
   total = 0
   
   # prompt all of the users for their salaries
   for i in range(people):
      # prompt user 1 for salary
      sal = int(input("What is the salary of person {}?".format(i+1)))
      # add the salary to the total
      total += sal
      # add the salary as an addition value in the list
      salaries.append(sal)
   
   # prompt users for total bill
   total_bill = int(input("How much is the bill? "))
   
   # for each of the salaries, do something
   for j in range(len(salaries)):
      # print person j + 1 should pay person j's percent of total salary times bill rounded to 2 decimals
      print("Person {} should pay ${}\n".format(j + 1, round((total_bill * (salaries[j]/total)), 2)))

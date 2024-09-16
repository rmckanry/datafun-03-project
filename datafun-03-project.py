'''
NOTE: Because of all the travel I modified an in class activity that I think fulfills the requirements with the changes I made.
(1) Prompt the user to enter a string of their choosing. Output the string.
(2) Complete the get_num_of_characters() function, which returns the number of characters in the user's string. We encourage you to use a for loop 
in this function.
(3) Enable the get_num_of_characters() function to return the results.
(4) Extend the program further by implementing the output_without_whitespace() function. output_without_whitespace() outputs the string's 
characters except for whitespace (spaces, tabs).
(5) Call the output_without_whitespace() function in main().
'''

#Imports
import logging

def get_num_of_characters(inputStr):
   #Function return number of characters in a string
   numChars = 0;
   
   #Loop to count char number
   for i in inputStr:
      numChars += 1
      
   #get length with function len()
   print("Use of len function. Number of characters is: ", len(inputStr))
   
   #Return value to main
   return numChars
   

def output_without_whitespace(inputStr):
   #Function removes any white space from string
   print('String with no whitespace:', end = " ")
   
   #Loop to find and remove whitespace (spaces and tabs
   for i in range(len(inputStr)):
      if not inputStr[i].isspace():
         print(inputStr[i], end = "")
         
   print('\n', end = "")


def main():
    
   # Configure logging - change level to DEBUG and re-run, to ERROR and rerun 
   logging.basicConfig(
    filename='text_analysis.log', 
    level=logging.INFO, 
    filemode='w', 
    #format='%(name)s'
   )
   # Get a configured logger instance and name it logger
   logger = logging.getLogger()
   
   #Enter and print string
   userStr = input('Enter a sentence or phrase:\n')
   
   logger.info("You entered:")
   #logger.info("You entered:", userStr)
   
   print('\nYou entered:', userStr)

   #Call function to get string length
   numChars =  get_num_of_characters(userStr)
   print('\nNumber of characters:', numChars)

   #Call function to remove white space
   output_without_whitespace(userStr)
   
if  __name__ == "__main__":
    main()
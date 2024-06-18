# Base code for the Induction day Random number bias task
import random  # adds the random library into the software

''' 
Random Library Bias Assessment

This is the base code for you to fill out and complete. 

The Challenges to complete:

Completed in this code 
1: Ask the user how many times they want to roll the dice, roll the dice that many times and report the results back. 

Not in this code:
2. Ask the user how many repeats of the test to do as well as the number of times to roll. Report the results

3. Assess the results to say which number is the highest, by how much, the smallest number, and if you can, 
if you feel the library is bias. 
'''


'''This is just an example solution, NOT by any means the best and intended as a guide and a prompt'''


def main():  # main subroutine in which the code should be added
    results = [0, 0, 0, 0, 0, 0]  # Created a list to store the results
    rolls = int(input("How many times would you like to roll? "))  # Takes in user input, as an integer, for rolls
    for i in range(0, rolls):  # launchers the iteration for the rolls
        num = random.randint(1, 6)  # generates the dice roll
        results[num-1] += 1  # accesses the list to increment the number
    print("The roles have concluded, here are the results")  # post rolls message
    for i in range(len(results)):  # starts iteration to print results
        print("The number ", str(i+1), " was rolled ", str(results[i]))  # formats results nicely


if __name__ == '__main__':  # standard way of starting code
    main()  # calls main to start the code

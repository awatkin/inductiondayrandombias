# Base code for the Induction day Random number bias task
import random  # adds the random library into the software

''' 
Random Library Bias Assessment

This is the base code for you to fill out and complete. 

The Challenges to complete:

Completed in this code 
1: Ask the user how many times they want to roll the dice, roll the dice that many times and report the results back. 

2. Ask the user how many repeats of the test to do as well as the number of times to roll. Report the results

3. Assess the results to say which number is the highest, the smallest number, The difference between highest and 
lowest and if you can, tell me if you feel the library is bias. 
'''


'''This is just an example solution, NOT by any means the best and intended as a guide and a prompt'''


def main():  # main subroutine in which the code should be added
    results = [0, 0, 0, 0, 0, 0]  # Created a list to store the results
    rolls = int(input("How many times would you like to roll? "))  # Takes in user input, as an integer, for rolls
    repeats = int(input("How many times would you like to repeat? "))
    for j in range(0, repeats):
        temprolls = [0, 0, 0, 0, 0, 0]
        high = 0
        for i in range(0, rolls):  # launchers the iteration for the rolls
            num = random.randint(1, 6)  # generates the dice roll
            temprolls[num-1] += 1  # accesses the list to increment the number
        print("The rolls set ", str(j), " concluded")  # post rolls message
        for i in range(len(temprolls)):  # starts iteration to print results
            if temprolls[i] > temprolls[high]:  # compares the current hightest roll
                high = i
            # print("The number ", str(i+1), " was rolled ", str(temprolls[i]))  # formats results nicely
        results[high] += 1  # increments the appropriate index
    print("The rolls and repeats have completed here are the results")
    # prints out the overall results
    h = 0  # temp variable to store the highest number index
    l = 0  # temp variable to store the lowest number index

    for i in range(0, len(results)):  # iteration to determine the high, low and print
        if results[i] > results[h]:  # Looking for the highest
            h = i  # updating the index in h for new highest
        if results[i] < results[l]:  # looking for the lowest
            l = i  # updating the indexin l for the new lowest
        print("The number ", str(i + 1), " was the highest number in ", str(results[i]), " of the repeats")  # print

    print(str(h+1), " is the highest number, with ", str(results[h]), " rolls")  # output for highest
    dist = results[h] - results[l]  # calcs the distance
    print(" The distance between the highest and lowest was ", str(dist))  # output
    percent = dist/repeats*100  # calc % difference
    if percent > 5.0:  # selection based on output
        print("There is some bias towards the highest number")
    else:
        print("There is no real bias in the library")
    print("The % difference between high and low is ", str(percent))
    print(str(l+1), " is the lowest number, with ", str(results[l]), " rolls")  # output the lowest num


if __name__ == '__main__':  # standard way of starting code
    main()  # calls main to start the code

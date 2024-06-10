#!usr/bin/env/python

### --- IMPORTS --- ###

#our two main imports from other files
from art import logo, vs
from game_data import data
#import our clear func
from os import system, name
#importing random so we can choose a random piece of data / time for stalling
import random, time

### --- FUNCTIONS --- ###

#as always we want a clear console func
def clear():
    """
    clears the console
    """
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#format data
def format_data(data_raw):
    """formats the data into a readable format, omitting the numbers so you have to guess
    """
    #data = "name, a profession from country"
    data = f"{data_raw['name']} a {data_raw['description']} from {data_raw['country']}"
    return data

#check the data to ensure it#s higher or lower
def check_data(a, b):
    """run a data check here 
    """
    #if data 2's count is higher than a then return higher
    if b['follower_count'] > a['follower_count']:
        return 'higher'
    #else return lower
    else:
        return 'lower'

#reset func to prevent retyping   
def reset():
    """resets the game / next round
    """
    time.sleep(1)
    clear()

### --- VARIABLES --- ###

#we want our continue func for the while loop :) and a score
cont = True
score = 0

#get our data with random
data_raw_1 = random.choice(data)
data_raw_2 = random.choice(data)

### --- MAIN --- ###

#we run a data check here to ensure that the data we have gotten is accurate
data_return = check_data(data_raw_1, data_raw_2)
#print our logo, vs, data
print(f"{logo}\nA: {format_data(data_raw_1)}\n{vs}\nB: {format_data(data_raw_2)}\n")
#ask for a guess
guess = input("Is Option B higher or lower?: ").lower()
#while loop time!
while cont == True:
    #if our guess contains what we want and is equal to data return
    if guess == 'higher' and guess == data_return or guess == 'lower' and guess == data_return:
        #they were correct!
        print(f"A: {data_raw_1['follower_count']}, B: {data_raw_2['follower_count']}")
        print(f"You got it right! It was {guess}")
        #we add to the score!
        score +=1
        #once the if statement gets it right we need to change data 2 to data 1
        data_raw_1 = data_raw_2
        #then select a new random data raw 2
        data_raw_2 = random.choice(data)
        #then we run the check again so it is not using old data
        data_return = check_data(data_raw_1, data_raw_2)
        #clear the console
        time.sleep(2)
        clear()
        #then we play again.
        print(f"{logo}\nA: {format_data(data_raw_1)}\n{vs}\nB: {format_data(data_raw_2)}\n")
        guess = input("Is Option B higher or lower?: ").lower()
    #if the guess contains what we want but does NOT == data return
    elif guess == 'higher' and guess != data_return or guess == 'lower' and guess != data_return:
        #let user know
        print(f"A: {data_raw_1['follower_count']}, B: {data_raw_2['follower_count']}")
        print(f"You were wrong :( It was not {guess}")
        #if it's wrong we want to print off a final score and reset
        print(f"Your final score was {score}")
        time.sleep(2)
        print("Thank you for playing and goodbye!")
        reset()
        cont = False
    #if the guess does not contain what we want, warn user, reset
    elif 'higher' not in guess or 'lower' not in guess:
        print("You can only use higher or lower, sorry about that")
        time.sleep(2)
        print("Goodbye")
        reset()
        cont = False

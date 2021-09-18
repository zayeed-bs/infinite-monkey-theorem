import math
import string
import time
import random

def generate_phrase(strlen):
    characters = string.ascii_lowercase + " "
    phrase = ""
    
    for i in range(strlen):
        phrase += characters[random.randrange(27)]
          
    return phrase

def main():
    attempts = 0
    goal_phrase = input("Enter the phrase you want to achieve:")
    initial_probability = round((pow((1/27), len(goal_phrase)) * 100), 10)
    print(f'The probability of it happening in the first try is {initial_probability}%')
    time.sleep(5)
    
    while True:
        attempted = generate_phrase(len(goal_phrase))
        attempts += 1
        print(f"Attempt: {attempts}. Phrase:{attempted}")
        
        if attempted == goal_phrase.lower():
            print(f"It took {attempts} attempts!")
            probability = round((pow((1/27), len(goal_phrase)) * 100 * attempts), 3)
            print(f'The probability of it happening in the this try is {probability}%.')
            
            if probability > 100:
                print('Late than usual,')
            else:
                print('Luckier than usual.')
                
            break
        
        

main()
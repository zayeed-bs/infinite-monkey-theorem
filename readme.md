# The Infinite Monkey Theorem

The infinite monkey theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type any given text, such as the complete works of William Shakespeare. In fact, the monkey would almost surely type every possible finite text an infinite number of times. However, the probability that monkeys filling the entire observable universe would type a single complete work, such as Shakespeare's Hamlet, is so tiny that the chance of it occurring during a period of time hundreds of thousands of orders of magnitude longer than the age of the universe is extremely low (but technically not zero). The theorem can be generalized to state that any sequence of events which has a non-zero probability of happening, at least as long as it hasn't occurred, will almost certainly eventually occur. 

**- Source: Wikipedia**


**This is a simulation of the theorem using python.**

## How it Works

### Generating the string:
We can generate the phrase randomly with some simple steps. First, we have all the possible characters in a variable. We can do this by adding `string.ascii_lowercase` and `' '`(whitespace) together in a string.
  
Then we can initiate a for loop for the generated phrase, for each iteration we pick a random character from the character string and add it to the generated one. The number of iteration(s) depends on the length parameter of the function. After we have finished iterating, we return the generated phrase as a string.
  
```Python
def generate_phrase(strlen):
  characters = string.ascii_lowercase + " "
  phrase = ""

  for i in range(strlen):
      phrase += characters[random.randrange(27)]

  return phrase
```

### Calculating and generating until it matches:
We take the phrase as input from the user. We can then calculate the probability of the phrase generating in the very first try by raising 1/27 to the power of the length of the goal phrase. We can then multiply it by 100 and round it to get a nice percentage.

__NOTE:__ **This simulation only simulates the lowercase letters and blank space. The goal phrase is automatically converted into lowercase.**

```Python
attempts = 0
  goal_phrase = input("Enter the phrase you want to achieve:")
  initial_probability = round((pow((1/27), len(goal_phrase)) * 100), 10)
  print(f'The probability of it happening in the first try is {initial_probability}%')
  time.sleep(5)
```

After that, we start an infinite while loop. Here we increment the attempts variable by 1 for each iteration. We then generate a phrase which is compared with the goal phrase. If it is the same as the goal phrase, we calculate the probability again which will be different.

The way we calculate the probability is pretty simple, we just multiply the initial percentage with the number of attempts. We can print it in the console with a percentage in the end now.

Here, the probability can be more than 100%. So we check for the value and if it is greater than 100%, we print `Unluckier than usual.` in the console. Alternatively, we print `Luckier than usual.` in the console if it is lower than 100%. `Average` is printed when it is 100%.

Finally we break the loop.

```Python
while True:
    attempts += 1
    attempted = generate_phrase(len(goal_phrase))
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
        
```
  
  
# Number Guessing Game

A game where users guess a randomly generated number.

## Used Liberaries

We use import random liberary to select a random nomber

```python
import random
```

## Program

```number = random.randint(1,100) 


while guess != number : # != means doesn't equal to.
  guess = 0 
  guess = int(input('Enter Guess : '))

  if (guess > number) :
    print('Enter lower number')

  elif (guess < number) :
    print('Enter higher number')

  else:
    print('Congratulations you are right!')
```

## Contributing

This project is done by Rajesh Wanekar
You can connect with me [![Linkedin](https://i.sstatic.net/gVE0j.png) LinkedIn](https://www.linkedin.com/in/rajesh-wanekar-747b6b256)

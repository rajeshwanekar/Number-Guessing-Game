# -*- coding: utf-8 -*-
"""Number Guessing Game.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19mz1H_jIpIKTnNbyCG8MqfgW6ukm0sdM
"""

#Number Guessing Game – A game where users guess a randomly generated number.

import random

number = random.randint(1,100) #random.randint(1,100) means that take ranint from random module. we can set numbers range in the brackets


while guess != number : # != means doesn't equal to.
  guess = 0 #guess = 0 doesn't interfare in this program most of the time. The value of guess changes as per users choice. we just kept it to define variable. we can remove it.
  guess = int(input('Enter Guess : '))

  if (guess > number) :
    print('Enter lower number')

  elif (guess < number) :
    print('Enter higher number')

  else:
    print('Congratulations you are right!')


#!/usr/bin/python

import sys

#denomination list set up per read.me for correct change amounts
# denominations = [1, 5, 10, 25, 50]

def making_change(amount, denominations):
  #base cases
  print(amount)
  if amount == 0:
    return 0
  if amount < 0:
    return 0
  if len(denominations) == 0 and amount > 0: 
    return 0
  else:
    #recursive function call 
    return making_change((amount-denominations[-1]), denominations) + making_change(amount, denominations[:1])
    

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")

'''
First we need to make a list that includes all of the denominations of money available to us.
***Just notice that the test file has the denominations set up already, so I am still going
to do it, but I might not have had to*** 
And we'll store it in a variable that can then be passed in to the making_change function.
Our base cases will be if the amount that is given us is zero, we'll return a zero - we
obviously can't make change from nothing. And we also have to take into account that if
the amount given us is a negative number we'll also return zero, for very similar reasons as
above.
Oh and if we no longer have any change with which to give change with (if denominations list
is empty) but the amount of money the patron gave us is larger than zero
we will also have to return zero, because we don't have change to give them.
Okay, now for the hard part, I think that in order to make the change we're going to have
to recursively call the making_change function and at the same time use it to decrement
the amount of change we still have in our available denominations.
'''
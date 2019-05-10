#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  output = []
  #create a list of all possible outcomes
  plays = [["rock"], ["paper"], ["scissors"]]
  #var for the current play to be saved in
  stack = []
 
  stack.append([])
  

  while len(stack) > 0:

    #take the first element out of the stack
    current_play = stack.pop(0)
    #check to see if the current play has the correct number of rounds
    if n == 0 or len(current_play) == n:
      #if the above condition passes we put the elemnet back in the stack
      stack.insert(0,current_play)
      return stack
    else:
      #otherwise we play another round and append it to the stack
      for play in plays:
        stack.append(current_play + play)
  



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

'''
So I know from the read.me that we will need to create a list of the possible outcomes.
There will have to be a way for the current play to be added to a variable or list that contains
all of the other plays that have happened and also the ones in the future. 
n is equal to the number of rounds that are being played, and the output should print out
all of the outcomes for n rounds. This could be handled with nested recursive functions.
Base case should be if n is 0 or the current play is 0.
'''
#!/usr/bin/python

import argparse

def find_profit(s, b):
  return s - b

def find_max_profit(prices):
  # current_min_price_so_far = 1000
  # max_profit_so_far = 0
  # for i in prices:
  #   if i < current_min_price_so_far:
  #     current_min_price_so_far = i
  #   else:
  #     return current_min_price_so_far
  # for i in prices:
  #   profit = find_profit(i, current_min_price_so_far)
  #   if profit > max_profit_so_far:
  #     max_profit_so_far = profit
  # return max_profit_so_far
  # current_min_price_so_far = 999999
  # max_profit_so_far = 0
  # for i in prices:
    
  #   if i < current_min_price_so_far:
  #     current_min_price_so_far = i
  #     print("This is the current min price")
  #     print(current_min_price_so_far)
  #   if i > current_min_price_so_far:
  #     profit = find_profit(i, current_min_price_so_far)
  #     print("This is the profit of current i")
  #     print(profit)
  #     if profit > max_profit_so_far:
  #       max_profit_so_far = profit

  # return max_profit_so_far

  max_profit_so_far = -9999999999
  for i in range(0, len(prices)-1):
   
    for x in range(i + 1, len(prices)-1):
      current_profit = find_profit(prices[x], prices[i])
      if current_profit > max_profit_so_far:
        print("New max profit created", current_profit)
        max_profit_so_far = current_profit
  print("Found max profit", max_profit_so_far)      
  return max_profit_so_far  


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))


  '''
  So, given the hint, if we create a var for the current-min-price (which would rep the buy) 
  and just kept subtracting it from the other ints in the array and would continually save
  over the max_profit_so_far var with any number that was larger than it previously it would
  represent the buy and sell prices, and therefore tell us the max profit.
  However, we'd also have to compare the int saved to the var
  current_min_price with the other ints in the array to make sure none of them are smaller,
  if they are, they'd have to be saved in the current_min_price instead of the previous int

  first we'd have to declare our variables to keep track of things to compare...
  current_min_price_so_far = 0
  max_profit_so_far = 0
  
  then we'd have to loop through the array to compare the ints to one another
  if i in arr < current_min_price_so_far
    then we'd save it's value
    current_min_price_so_far = arr[i]
  then we'd have to do another loop through the array to subtract the ints saved
  in the current_min_price_so_far variable from the other ints to get the max_profit var
  if arr[i] - current_min_price_so_far > max_profit_so_far
    max_profit_so_far = arr[i] - current_min_price_so_far

  added thought - maybe a helper function that does the subtracting is a good idea?
  find_profit(i, current_min_price_so_far)
    return i - current_min_price_so_far

  The above doesn't work because I didn't take into account that you have to buy a stock before
  you can sell it, therefore, the buy price (current_min_price_so_far)
  has to come before the sell price - I think a nested loop might work for this

  So, after running through a couple code changes I decided that maybe I didn't need to save
  the current_min var because it seemed to be nothing I needed to take into consideration.
  Instead, I decided to nest loops where the first index would be compared to all others and
  that would repeat in succession in order to find the max profit by comparing the profit
  gained by performing my profit helper function and that is how the code is now.
  '''
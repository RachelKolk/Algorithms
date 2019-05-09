#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution


def cookie_combos(array, index, cookies, reducedCookies, total_ways):
  global total_ways2
  # Starting condition
  if (reducedCookies < 0):
    return 
  
  # Eat all cookies
  if (reducedCookies == 0):
    if index == cookies:
      total_ways2 = 1 + total_ways2
      print(total_ways2)
      return total_ways
    else:
      total_ways2 = index + total_ways2
      print(total_ways2)
      return total_ways
    return total_ways
  
  # Find the previously eaten cookie
  prevCookie = 1 if(index == 0) else array[index -1]

  # Next we start from the previous number of cookies
  
  for k in range(prevCookie, cookies + 1):
    
    if k <= 3:
      array[index] = k

      # recursive call with reduced number
      found = cookie_combos(array, index + 1, cookies, reducedCookies - k, total_ways)
      if found != None:
        total_ways = total_ways + found




def eating_cookies(n, cache=None):
  array = [0] * n
  global total_ways2
  total_ways = 0 
  # find our cookie combos
  cookie_combos(array, 0, n, n, total_ways)
  return total_ways2

# def eating_cookies(n, cache=None):
  # #baseline
  # if n <= 0:
  #   return
  # #save n as cache length
  # cache = [0] * n
  # print("Printing cache")
  # print(cache)
  # #create variable for storing our permutation number
  # possible_ways = 0
  # while len(cache) > 0:
    
  #   print(cache)
  #   if cache / 3:
  #     print("Divisible by 3")
  #     possible_ways = cache // 3
  #     cache = cache % 3
  #     print("With remainder", cache)
      
  #     print("possible ways count currently at", possible_ways)
  #   if cache / 2:
  #     cache = cache % 2
  #     possible_ways += 1
  #   if cache / 1:
  #     cache = cache % 1
  #     possible_ways +=1
  # if cache == 0:
  #   return possible_ways

total_ways2 = 0
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
    
  else:
    print('Usage: eating_cookies.py [num_cookies]')

'''
Because Cookie Monster is limited to eating at max only 3 cookies at a time, 
and at min 1 cookie at a time, I think that we could take the 
example from the read.me and infer that if we use the total number of cookies present
and save it as a cache we could then alter it using the
amount of cookies he can eat at a time using a while loop.
The permutations or ways in which he could eat them would have to be saved in a variable
that is returned by the function.
Also if there are 0 or negative numbers of cookies that should be our baseline because
he can't eat cookies if they're not there.
The problem is that the permutations could get really big and I'm trying to wrap my head 
around how I can account for all of them. 

like with 5 cookies it could be
1 + 1 + 1 + 1 + 1
1 + 1 + 1 + 2
2 + 1 + 1 + 1
1 + 2 + 1 + 1
1 + 1 + 2 + 1
1 + 3 + 1
3 + 1 + 1
1 + 1 + 3
2 + 2 + 1
1 + 2 + 2
2 + 1 + 1
2 + 3
3 + 2

But if I look at this broken out like this...it means that 1, 2, or 3 could sit at any one
index of a number if it were made into an object in the cache, therefore I think that
you could recursively loop through it using 1, 2, or 3 as the value and keep a count of
the possible outcomes.
However, we'd then have to account for the fact that 3 would never be able to be in the last
index because by then it would make the cookie count too high. (As can be seen in my mocked up
example above, the sum of the individual values have to add up to the cookie count.)
I am trying to figure out how I would go about figuring out how to get the correct index number
for the last possible place 3 could be.
I think that in this case I should just start with the 1, since it will be able to be in all
of the index positions. And then work my way up.
'''
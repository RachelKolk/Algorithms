#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  divisors = []
  for a in recipe:
    found = 0
    for z in ingredients:
      if a == z:
        divisors.append((ingredients[z]//recipe[a]))
        print(z,":", ingredients[z],"recipe needs",a,":", recipe[a])
        print("Appending divisors")
        print(divisors)
        found = 1
    if found == 0:
      divisors.append(0)
  return min(divisors)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))


'''
For this algorithm, I want to compare the dictionaries key value pairs and see how many
times the recipe quantities will divide into the ingredients quantities.
I think I will start by saving each dictionary as its own variable and listing out its items.
Then I will loop through the variables and compare their items to make sure there is enough
ingredients comparatively for the recipe by dividing their values and finding the common divisor.
If I save those divisors in an array of their own I could then just sort through it to find the
smallest int and that would be the amount of times a recipe could be made with the
provided ingredients
'''
"""
Project Euler: Problem 2: Even Fibonacci Numbers
Each new term in the Fibonacci sequence is generated by adding the previous two terms
"""

def fiboEvenSum(n):
  # You can do it!
  # to count the number from 3 because variable nombres begin with 2 numbers
  compteur = 3 
  nombres = [1,2]
  liste_fibonacci = nombres[:] # copie of the list called 'nombres'

  while compteur <=n:
  	resultat = sum(nombres)
  	liste_fibonacci.append(resultat) # add the result of variable 'resultat' to the Fibonacci list
  
  	del nombres[0] # delete the first occurence of 'nombres' list
  	nombres.append(resultat) # add the result of variable 'resultat' to the 'nombres' list

  	compteur = compteur + 1 # add 1 to the counter of the while loop
  print('List of Fibonacci numbers you asked for the',n,
        'first numbers :\n\n',liste_fibonacci)

fiboEvenSum(10)

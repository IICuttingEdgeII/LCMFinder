def primeNumbers(n):
  prime = [True for i in range(n + 1)]
  p = 2
  while (p * p <= n):

      # If prime[p] is not changed, then it is
      # a prime
      if (prime[p] == True):

          # Update all multiples of p
          for i in range(p * 2, n + 1, p):
              prime[i] = False
      p += 1
  return [i for i, val in enumerate(prime) if val == True and i not in {0, 1}]

def primeFactors(number, factors, prime_numbers):
  if number == 1:
    return factors
  for i in prime_numbers:
    if number % i == 0:
      if i not in factors:
        factors[i] = 1
      else:
        factors[i] += 1
      number /= i
  return primeFactors(number, factors, prime_numbers)

def highestExponent(dict1, dict2):
  highest_exponent = {}
  for key in dict1.keys():
    if key in dict2.keys():
      highest_exponent[key] = max(dict1[key], dict2[key])
    else:
      highest_exponent[key] = dict1[key]
  for key in dict2.keys():
    if key not in highest_exponent:
      highest_exponent[key] = dict2[key]
  return highest_exponent
    
def LCM(numbers, prime_numbers): 
  factorsDict = {}
  for index, number in enumerate(numbers):
    factorsDict = highestExponent(primeFactors(number, {}, prime_numbers), factorsDict) 
  LCM = 1
  for key in factorsDict.keys():
    LCM *= (key ** factorsDict[key])
  return LCM


def main():
  numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
  prime_numbers = primeNumbers(max(numbers))
  print(LCM(numbers, prime_numbers))


main()

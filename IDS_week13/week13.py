n_vowels = 0
for i in 'azcbobobegghakl':
  if i in ['a','e','i','o','u']:
    print(i)
    n_vowels +=1
print(n_vowels)

test_str = 'azcbobobegghakl'
n_char = len(test_str)
print(n_char)
for i in range(12):
  print(test_str[i:i+3])

test_str = 'azcbobobegghak'
n_char = len(test_str)
n_bobs = 0
for i in range(n_char - 2):
    #print(test_str[i:i+3])
    if test_str[i:i+3] == 'bob':
        n_bobs += 1
print(n_bobs)

x = list(range(1, 101))
N = len(x)
x_bar = sum(x) / N
sse = 0
for xi in x:
  # error = xi - x_bar
  squared_error = (xi - x_bar)**2
  sse += squared_error # sse = sse + squared_error
sample_mse = sse / (N-1)
sample_stdev = sample_mse**(0.5)
print(sample_stdev)

def get_fahrenheit(x):
    """
    Transform a Celsius degree into  Farenheit scale
    """
    fah = x * 9/5 + 32
    return fah
get_fahrenheit(32)

def get_bmi(height, weight):
    """
    Calculate BMI based on height and weight
    """
    height = height / 100
    bmi = weight / height**2
    return bmi
get_bmi(180, 77)

def is_prime(x):
  """
  Retuen True if x is a prime, or return False
  """
  divisors = []
  for i in range(1, x+1):
    if x % i ==0:
      divisors.append(i)
  n_divisors = len(divisors)
  return n_divisors == 2
is_prime(11)
is_prime(9)
is_prime(51)
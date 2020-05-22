x = int(input("請輸入起始的正整數：")) 
y = int(input("請輸入終止的正整數："))
for i in range(x, y+1):
  print(i)

x = int(input("請輸入起始的正整數：")) 
y = int(input("請輸入終止的正整數："))
odds = [] # 空的list
for i in range(x, y+1):
  mod = i % 2
  if mod == 1:
    odds.append(i)
print(odds)

user_int = int(input("請輸入一個正整數："))
divisors = [] # 因數分解
for i in range(1, user_int+1):
  if user_int % 1 == 0:
    divisors.append(i)
print(divisors)
n_divisors = len(divisors)
if n_divisors == 2 :
  print("{}是質數".format(user_int))
else:
  print("{}不是質數".format(user_int))

# random 產生 1 個隨機數
import random

random.randint(1, 1000)
# random 產生 100 個隨機數
random_integers = [] # 隨機數
for i in range(100): # 產生個數
  rand_int = random.randint(1, 1000) # 範圍
  random_integers.append(rand_int)
print(random_integers)
print(len(random_integers))
# 找出第一大與第一小的數字
print(max(random_integers))
print(min(random_integers))
# 找出第二大與第二小的數字
rand_int_unique = set(random_integers)
rand_int_unique_list = list(rand_int_unique)
print(rand_int_unique_list)
rand_int_unique_list.sort()
print(rand_int_unique_list[1]) # second min
print(rand_int_unique_list[-2]) # second max

squared = []
for i in range(10):
  squared.append(i**2)
print(squared)

squared = [i**2 for i in range(10)] 
print(squared)

odds_squared = []
for i in range(10):
  if i % 2 == 1:
    odds_squared.append(i**2)
print(odds_squared)

odds_squared =[i**2 for i in range(10) if i % 2 == 1]
print(odds_squared)

random_integers = [random.randint(1, 100) for i in range(10)]
is_odd_ints = []
for i in random_integers:
  if i % 2 == 1:
    is_odd_ints.append(True)
  else:
    is_odd_ints.append(False)
print(random_integers)
print(is_odd_ints)

random_integers = [random.randint(1, 100) for i in range(20)]
is_odd_ints = [True if i % 2 == 1 else False for i in random_integers]
print(random_integers)
print(is_odd_ints)

avengers_ratings = [8.1, 7.3, 8.5, 8.8] 
recommendations = [i for i in avengers_ratings if i >= 8] 
print(recommendations)

avengers = ["The Avengers", "Avengers: Age of Ultron", "Avengers: Infinity War", "Avengers: Endgame"]
for idx, movie in enumerate(avengers):
    print("第 {} 部上映的復仇者聯盟電影:{}".format(idx+1, movie))

years = [2012, 2015, 2018, 2019]
for year, movie in zip(years, avengers):
    print("{}上映的年份是{}".format(movie, year))

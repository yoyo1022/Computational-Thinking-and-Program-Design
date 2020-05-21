primes_list = [2, 3, 5, 7, 11]
primes_list[-1] = 13 # update
print(primes_list)

primes_list.insert(-1, 11) # increase length
print(primes_list)

primes_list.pop()
print(primes_list)

x = 0.25
print(type(x))
print(x.as_integer_ratio())
print(type(x.as_integer_ratio()))

def where_are_you_from(city, country):
    return city, country

print(where_are_you_from("Taipei", "Taiwan"))
print(type(where_are_you_from("Taipei", "Taiwan")))

my_city, my_country = where_are_you_from("Taipei", "Taiwan")
print(my_city)
print(my_country)

living_area = input("請輸入您的居住縣市:")
living_cost = None
if living_area == '臺北市':
    living_cost = 17005
elif living_area == '新北市':
    living_cost = 15500
elif living_area == '桃園市':
    living_cost = 15281
elif living_area == '臺中市':
    living_cost = 14596
elif living_area == '臺南市':
    living_cost = 12388
elif living_area == '高雄市':
    living_cost = 13099
elif living_area == '非六都之縣市':
    living_cost = 12388
elif living_area == '金門縣連江縣':
    living_cost = 11648

if living_cost is None:
    print("請重新輸入居住縣市")
else:
    print("{}的每人每月最低生活費為{:,}".format(living_area, living_cost))

living_cost_dict = {
    '臺北市': 17005,
    '新北市': 15500,
    '桃園市': 15281,
    '臺中市': 14596,
    '臺南市': 12388,
    '高雄市': 13099,
    '非六都之縣市': 12388,
    '金門縣連江縣': 11648
}
living_area = input("請輸入您的居住縣市:")
try:
    living_cost = living_cost_dict[living_area]
    print("{}的每人每月最低生活費為{:,}".format(living_area, living_cost))
except KeyError:
    print("請重新輸入居住縣市")

primes_list = [2, 3, 5, 7, 11]
I = iter(primes_list)
next(I)

I = iter(living_cost_dict.keys())
next(I)

I = iter(living_cost_dict.items())
next(I)

for i in range(1, 101, 1):
    print(i)
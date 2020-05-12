lucky_num_0 = 7
lucky_num_1 = 24
lucky_num_2 = 5566
lucky_numbers = [7, 24, 5566]

sat = "Saturday"
sun = "Sunday"

weekend = ["Saturday", "Sunday"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

print(len(lucky_numbers))
print(len(weekend))
print(len(weekdays))

my_fav_weekday = "Friday"
print("My favorite weekday is {}.".format(my_fav_weekday))

print(lucky_numbers)
lucky_numbers.append(87)
print(lucky_numbers)

print(lucky_numbers)
lucky_numbers.pop()
print(lucky_numbers)

my_fav_group = lucky_numbers.pop()
print(lucky_numbers)
print(my_fav_group)

print(weekdays[0])
print(weekdays[1])
print(weekdays[2])
print(weekdays[3])
print(weekdays[4])

i = 0
while i < 5:
    print(weekdays[i])
    i += 1

i = 0
while i < 2:
    print(weekend[i])
    i += 1

i = 0
while i < len(weekend):
    print(weekend[i])
    i += 1

i = 0
while i < len(weekdays):
    print(weekdays[i])
    i += 1

print(weekdays[-1])
print(weekdays[-2])
print(weekdays[-3])
print(weekdays[-4])
print(weekdays[-5])

i = -1
while i >= -5:
    print(weekdays[i])
    i -= 1

weekdays[0:3:1]

weekdays[0:5:2]

weekdays[::2]
current_Celsius = 25
Fahrenheit = current_Celsius*9/5+32
print(Fahrenheit)

current_Fahrenheit = 77
Celsius = (Fahrenheit-32)*5/9
print(Celsius)

shaq_weight = 147
shaq_height = 216
shaq_bmi = shaq_weight/(shaq_height/100)**2
print(shaq_bmi)

ross_said = """Let's put aside the fact that you "accidentally" pick up my grandmother's ring."""
print(ross_said)

city = input("請輸入城市: " )
weather = input("請輸入天氣: " )
print("我在{}，天氣{}".format(city, weather))

name = input("請輸入姓名: ")
shaq_height = eval(input("請輸入身高: "))
shaq_weight = eval(input("請輸入體重: "))
shaq_bmi = shaq_weight/(shaq_height/100)**2
print("{}的身體質量指數為：{:.2f}".format(name,shaq_bmi)) 
print("{}是否過重：{}".format(name,shaq_bmi > 30))

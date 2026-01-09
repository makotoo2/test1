import sys

new_age = input("年齢を入力してください: ")
try:
    age = int(new_age)
except ValueError:
    print("年齢は整数で入力してください")
    sys.exit()

if age < 0:
    print("不正な年齢です")
elif age >= 18:
    print("成年です")
else:
    print("未成年です")

if age <= 3:
    print("乳児です")

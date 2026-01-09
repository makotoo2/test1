# くじ引きプログラム
# 3~6の数字を入力して、当選番号と一致したら「当たり」、違ったら「ハズレ」
import datetime
from datetime import date

# 当選番号を設定（3と4が当たり）
winning_numbers = [3, 4]

# ユーザーに3~6の数字を入力させる
number = int(input("3~6の数字を入力してください: "))

# 入力値が3~6の範囲にあるか確認
if number < 3 or number > 6:
    print("3~6の数字を入力してください")
else:
    # 当選番号と比較
    if number in winning_numbers:
        print("当たり！")
    else:
        print("ハズレ")

# 今日の日付から季節名を表示する関数を定義
def display_season():
    seasons = ["spring", "summer", "autumn", "winter"]
    today = datetime.date.today()
    month = today.month
    if month in [3, 4, 5]:
        index = 0
    elif month in [6, 7, 8]:
        index = 1
    elif month in [9, 10, 11]:
        index = 2
    else:
        index = 3
    print(seasons[index])
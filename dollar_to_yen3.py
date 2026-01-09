def dollar_to_yen(dollar, rate=130):
    yen = dollar * rate
    return yen
    
dollar = 5
yen = dollar_to_yen(dollar, 120)
print(f"{dollar}ドルは{yen}円です")
dollar = 10
yen = dollar_to_yen(dollar)
print(f"{dollar}ドルは{yen}円です")

n = int(input())
countings = []
count = {
    "0": 0,
    "khong": 0,
    "mot": 1,
    "1":1,
    "hai": 2,
    "2": 2,
    "ba": 3,
    "3": 3,
    "bon": 4,
    "4": 4,
    "nam": 5,
    "5": 5,
    "sau": 6,
    "6": 6,
    "bay": 7,
    "7": 7,
    "8": 8,
    "tam": 8,
    "chin": 9,
    "9": 9,
    "muoi" : 10,
    "10" : 10
}

def calcMoney(count):
    price = 1.0
    moneys = 0.0
    if count >= 20:    
        while (count > 7 and round(price, 1) > 0.5):
            moneys += 7 * price
            count -= 7
            price -= 0.1
        
        moneys += count * price
    else:
        moneys = count * price
    return round(moneys, 1)

for i in range(n):
    temp = input().lower().split()
    countings.append(temp[len(temp) - 1])
res = 0

for counting in countings:
    res += count[counting]
print(res, calcMoney(res))


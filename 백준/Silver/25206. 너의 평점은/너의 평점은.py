dict_score = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0.0
}

g=0
m=0

for i in range(20):
    _, graduate,  mark= input().split()
    if mark=='P':
        continue
    graduate = float(graduate)
    g += graduate
    m+=dict_score[mark]*graduate

if g==0:
    print(0)
else:
    print(round(m/g, 6))
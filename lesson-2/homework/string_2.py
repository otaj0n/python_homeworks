# 2 Extract car names from this text: txt = 'LMaasleitbtui'

txt = 'LMaasleitbtui'

cars = ['Malibu', 'Lasetti', 'Damas']

approved = []
cnt = 0
for car in cars:
    for i in car.lower():
        if i in txt.lower():
            cnt += 1
            if cnt == len(car):
                approved.append(car)

print(approved)


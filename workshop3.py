money = 0
j = int(input("บอสสั่งให้เก็บเงินกี่ร้าน"))
for i in range(j):
    h = float(input(f"เก็บเงินจากร้านที่ {i+1} " ))
    money += h
print("บอสได้เงินรวมมา",money)

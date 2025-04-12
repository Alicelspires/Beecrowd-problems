v = float(input())

i = 0
array_money = [100, 50, 20, 10, 5, 2]
array_cents = [100, 50, 25, 10, 5, 1]

print("NOTAS:")

while i < 6:
    divide = v // array_money[i]
    print(f"{int(divide)} nota(s) de R$ {array_money[i]}.00")
    v %= array_money[i]
    i += 1

print("MOEDAS:")
v = round(v * 100)
j = 0

while j < 6:
    divide = int(v // array_cents[j])
    print(f"{divide} moeda(s) de R$ {array_cents[j]/100:.2f}")
    v -= divide * array_cents[j]
    j += 1
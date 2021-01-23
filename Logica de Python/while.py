# repetição while

x = 0
while x <= 5:
    # Quando ele achar a palavra continue ele pula pro proximo laço
    if x == 3:
        x = x+1
        continue
    # Quando ele achar o break ele sai fora do laço
    if x == 5:
        break
    print(x)
    x = x+1
print('Acabou')

z = 0
y = 0

while z < 10:
    y=0
    while y<5:
        print(f'Z vale {z} e Y vale {y}')
        y+= 1
    z+= 1

print('Acabou')
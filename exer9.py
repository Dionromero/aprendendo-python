num = int(input('Digite um numero para ver sua tabuada...:'))

print('-' * 12)
for i in range(1,11):
    print(num, 'X' , i , '=' , num * i)
print('-' * 12)
n = float(input('Please enter your number: '))
if n % 2 !=0:
    print("Weird")

elif n % 2 == 0:
   if 2<=n <=5:
      print(f'{n} is Not Weird')
   elif 6<=n <=20:
      print(f'{n} is Weird')
   elif n>20:
      print(f'{n} is Not Weird')

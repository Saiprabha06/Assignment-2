#Task-1 Check if Number is Even or Odd
num=int(input("Enter a number: "))

if num % 2==0:
    print(num, ' is an even number')
else:
    print(num, ' is an odd number')


#Task 2: Sum of Integers from 1 to 50 Using a Loop
number = (1,51)
sum = 0
for i in range(1,51):
    sum += i
print('The sum of number from 1 to 50 is:', sum)
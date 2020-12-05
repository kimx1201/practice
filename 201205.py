#  3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.
hrs = input("Enter Hours:")
h = float(hrs)
xx = input("Enter the Rate:")
x = float(xx)
if h <= 40:
 	print( h  * x)
elif h > 40:
	print(40* x + (h-40)*1.5*x)


    score = input("Enter Score: ")

score = input("Enter Score: ")
s =  float(score)
x = 'Error'
if s >= 0.9:
	x = 'A'
elif s >=0.8:
	x='B'
elif s >=0.7:
	x='C'
elif s >= 0.6:
	x='D'
elif s < .6:
	x ='F'
else:
	x ="Out of Range"
print (x)

largest = None 
smallest = None 
while True: 
  num = input("Enter a number: ") 
  if num == "done" : 
    break 
  try: 
    num1 = int(num) 
  except: 
    print("Invalid input") 
    continue 
  if largest is None or num1 > largest:
    largest = num1 
  if smallest is None or num1 < smallest:
    smallest = num1 

print("Maximum is", largest) 
print("Minimum is", smallest)
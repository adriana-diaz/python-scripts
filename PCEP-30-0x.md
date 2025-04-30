# My labs of my PCEP-30-0x certificacion in Cisco 🤖

## 2.4.7   LAB   Variables
![image](https://github.com/user-attachments/assets/dd66604f-ec6d-4941-bc2d-6e1ef14ed26c)

## LAB   The print() function and its arguments
![image](https://github.com/user-attachments/assets/f35c71e3-daed-4293-9d25-31a303db8bd7)

## LAB   Python literals - strings
![image](https://github.com/user-attachments/assets/627f1352-ce23-47a0-b88f-cfbac99454eb)

## LAB   Variables ‒ a simple converter
![image](https://github.com/user-attachments/assets/561c7abb-b965-415e-9afa-a1e69a2264fd)

## LAb Type casting (type conversions)
![image](https://github.com/user-attachments/assets/0f3df01c-1763-48a5-8a7f-9358db50affd)

##  LAB   Variables ‒ Questions and answers
![image](https://github.com/user-attachments/assets/f0fe1e65-a375-486c-b9b4-882e2dd91eb3)

##  LAB  find the largest of several numbers and print it out.
![image](https://github.com/user-attachments/assets/69b0a527-37f9-4b61-8a55-7b9815c5eb4f)

##  LAB  Comparison operators and conditional execution
![image](https://github.com/user-attachments/assets/f919c3e3-854b-4a88-a756-8918ce1cc6f5)

##  LAB   Essentials of the if-elif-else statement
![image](https://github.com/user-attachments/assets/311e2fee-a9b3-44d6-8bab-5c34e7021f70)

year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
	if year % 4 != 0:
		print("Common year")
	elif year % 100 != 0:
		print("Leap year")
	elif year % 400 != 0:
		print("Common year")
	else:
		print("Leap year")
	

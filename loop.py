
#for loop
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I love {fruit}")

#while loop
count = 1

while count <= 5:
    print(f"Count: {count}")
    count += 1

#loop controls: break and continue

for number in range(1,10): #loop through number 1 to 9
    if number == 5:
        print("braking the loop at 5")
        break #exit the loop when the number is 5
    elif number %2 == 0:
        print(f"Skipping {number} because it's even")
        continue # skip the rest of  the loop body for even numbers
    print(f"Processing number : {number}")

#nested loop
for i in range (1,4): #outer loop
    for j in range(1,4): #inner loop
        print(f"Outer loop: {i}, Inner loop: {j}")
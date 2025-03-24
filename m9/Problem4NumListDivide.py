# Haseeb Abidi
# Date: 3/23/25
# Problem 4: Append values divisible by 10 to a list using a while loop

tens = []
counter = 0

while counter <= 50:
    if counter % 10 == 0:
        tens.append(counter)
    counter += 1

print("Values divisible by 10:", tens)

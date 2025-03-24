#Haseeb Abidi
#last edited 2/6/2025
#its coverting KMH to MPH

200#!/usr/bin/env python
kmh = int(input("Enter km/h: ")) #we get imput from the user as string and we use "int" method to convert string to integer.
mph =  0.6214 * kmh
print("Speed:", kmh, "KM/H = ", mph, "MPH")
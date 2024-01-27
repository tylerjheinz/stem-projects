userTemp = input("Enter Temperature in Fahrenheit: ")
fahrTemp = int(userTemp)
celciusTemp = (fahrTemp - 32) * 5 / 9
print("Temperature in Celcius is: ", celciusTemp)

print("Debug: celciusTemp =", celciusTemp, "fahrTemp =", fahrTemp)

if celciusTemp < 0:
    print("Woof, das chilly")

elif fahrTemp > 95:
    print("I refuse to work in these conditions. I'm calling my lawyer.")

else:
    print("Be chill brah")

# Mad Libs Program

bodyPart = input("Enter a body part: ")
color = input("Enter a color: ")
shape = input("Enter a shape: ")
favoriteArea = input("Who is your favorite camp area (Don't worry, we're not jealous): ")
time = input("What time is it in your story? ")
temperature = input("Was it hot or cold? ")

if temperature == "hot":
    print("It was a sweaty day...")
elif temperature == "cold":
    print("It was a chilly day...")

print("It was ", time, "and the sky was ", color, ". I was at ", favoriteArea, "working on requirements, when the building suddenly turned", shape, "!")
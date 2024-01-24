# Mad Libs Program

storyBodies = [
    "Testing. %s, %s, %s, %s, %s, %s",
    "Testing. %s, %s, %s, %s, %s, %s",
    "Testing. %s, %s, %s, %s, %s, %s"
]

def questions():
    """
    In this function, we'll be getting the actual words that we will use to madlib the story. 
    They're also variables, but when we make them using the input() function, we can ask the user what they want them to be.
    """
    bodyPart = input("Enter a body part: ")
    color = input("Enter a color: ")
    shape = input("Enter a shape: ")
    favoriteArea = input("Who is your favorite camp area (Don't worry, we're not jealous): ")
    time = input("What time is it in your story? ")
    weather = input("What was the weather ")

    return bodyPart, color, shape, favoriteArea, time, weather



def madlibs():
    print("Welcome to Madlibs!\nSelect a story:")
    """
    This is called a list. Lists are made by defining a name for the list (in this case, 'stories'), and using brackets '[]' to open and close them
    Inside these brackets, you can define variables, which can be accessed by using an index, or a number.
    Python indexes from 0, so to access your first variable in the list, we could do: 
    print(stories[0])
    Which would return: "Off to The Waterfront"
    """
    storyTitles = ["Off to The Waterfront", "Trading Post Blues", "Frisbee Fumble"]
    # For loops may seem scary, but this one is just saying "For every 'i'tem in the range of (however many stories are in the list), execute this code"
    for i in range(len(storyTitles)):
        # And this line below, is just printing out the index plus one, a period, and then the title of the story.
        # The i + 1 is just so instead of 0., it will say 1., and so forth.
        print(str(i + 1) + ". " + storyTitles[i])

    storyChoice = int(input("> ")) - 1
    print("You've selected: ", storyTitles[storyChoice])
    bodyPart, color, shape, favoriteArea, time, weather = questions()
    print(storyBodies[storyChoice] % (bodyPart, color, shape, favoriteArea, time, weather))


madlibs()


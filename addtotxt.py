input = input("Add text to the txt file nerd:\n")
with open("story.txt", "a+") as data:
    data.write(input)


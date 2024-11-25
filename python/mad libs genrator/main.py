import random

# 1. Define the Story Template
story_template = """
Once upon a time in a {place}, there was a {adjective1} {animal}. It loved to {verb1} all day long.
One day, it met a {adjective2} {person}. They became best friends and decided to {verb2} together.
They lived happily ever after in their {adjective3} {place2}.
"""

# 2. Get User Inputs
def get_user_inputs():
    user_inputs = {
        "place": input("Enter a place: "),
        "adjective1": input("Enter an adjective: "),
        "animal": input("Enter an animal: "),
        "verb1": input("Enter a verb: "),
        "adjective2": input("Enter another adjective: "),
        "person": input("Enter a person's name: "),
        "verb2": input("Enter another verb: "),
        "adjective3": input("Enter one more adjective: "),
        "place2": input("Enter another place: ")
    }
    return user_inputs

# 3. Generate the Mad Libs Story
def generate_story(template, user_inputs):
    return template.format(**user_inputs)

# 4. Display the Completed Story
def main():
    print("Welcome to the Mad Libs Generator!")
    user_inputs = get_user_inputs()
    story = generate_story(story_template, user_inputs)
    print("\nHere is your Mad Libs story:\n")
    print(story)

if __name__ == "__main__":
    main()
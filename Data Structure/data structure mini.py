# ----------------------------------------------------------------------------------------
# Project 1: Dictionary of People and Interesting Facts
#
# Create a dictionary that contains a list of people and one interesting fact about each.
# Display each person and their interesting fact to the screen.
# Then:
# - Change the fact about one of the people.
# - Add a new person with their interesting fact.
# Display the updated dictionary.
# Run the program multiple times and notice if the order changes.
# ----------------------------------------------------------------------------------------

people_facts = {
    "Jeff": "is afraid of Dogs",
    "David": "Plays the piano",
    "Jason": "Can fly an airplane"
}

print("Original facts:")
for name, fact in people_facts.items():
    print(f"{name}: {fact}")

people_facts["Jeff"] = "is afraid of heights"
people_facts["Jill"] = "Can hula dance"

print("\nUpdated facts:")
for name, fact in people_facts.items():
    print(f"{name}: {fact}")


# ----------------------------------------------------------------------------------------
# Project 2: Find the Runner-Up Score
#
# Given the participant's score sheet for your University Sports Day,
# store the scores in a list and find the score of the runner-up.
# ----------------------------------------------------------------------------------------

scores = [2, 3, 6, 6, 5]
unique_scores = list(set(scores))
unique_scores.sort(reverse=True)
if len(unique_scores) >= 2:
    print("\nRunner-up score:", unique_scores[1])
else:
    print("Not enough unique scores to determine runner-up.")


# ----------------------------------------------------------------------------------------
# Project 3: Student Marks Average Using Dictionary
#
# You have records of n students. Each record contains:
# - Student's name as the key
# - List of marks in Math, Physics, Chemistry as the value
#
# Take a student's name as input and display their average percentage marks.
# ----------------------------------------------------------------------------------------

students = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

name = input("\nEnter a name: ")
if name in students:
    marks = students[name]
    average = sum(marks) / len(marks)
    print(f"Average percentage mark: {average:.1f}")
else:
    print("Student not found.")


# ----------------------------------------------------------------------------------------
# Project 4: Count Occurrence of 'Alex' in a Sentence
#
# Given a string of n words, help Alex find how many times his name appears.
#
# Constraint: 1 < n <= 200
# ----------------------------------------------------------------------------------------

text = input("\nEnter a string (max 200 characters): ")
if 1 < len(text) <= 200:
    count = text.count("Alex")
    print(f"Number of times 'Alex' appears: {count}")
else:
    print("Input length out of bounds.")

# print("Hello World!")

# # Math Practice
# print(5 + 2 * 3)
# print(8 // 5 - 3)
# print(8 + 22 * 2 - 4)
# print(16 - 3 / 2 + 7 - 1)
# print(3 ** 3 % 5)
# print(5 + 9 * 3 / 2 - 4)

# print((5 + 2) * 3)
# print((8 // 5) - 3)
# print(8 + (22 * (2 - 4)))
# print(16 - 3 / (2 + 7) - 1)
# print(3 ** (3 % 5))
# print(5 + (9 * 3 / 2 - 4))
# print(5 + (9 * 3 / (2 - 4)))


# # List practice
# counties = ["Arapahoe","Denver","Jefferson"]

# print(counties)

# #Slicing
# print(counties[0:2])

# #Adding to list
# counties.append("El Paso")

# print(counties)

# # To specify where in a list to add a new item, select the location with an index by using the following syntax: list.insert(index, obj)
# counties.insert(2, "El Paso")
# print(counties)

# # To remove an instance of "El Paso" from our list, we'll append the .remove method and specify the list item we're removing.
# counties.remove("El Paso")
# print(counties)

# # To remove the last instance of "El Paso" using the pop() method, enter counties.pop(3). "El Paso" is the fourth item in the list.
# counties.pop(3)
# print(counties)

# # Tuples
# counties_tuple = ("Arapahoe","Denver","Jefferson")
# len(counties_tuple)
# print(len(counties_tuple))
# print(counties_tuple[1])

# # Dictionaries
# counties_dict = {}
# counties_dict["Arapahoe"] = 422829
# print(counties_dict)

# counties_dict["Denver"] = 463353
# counties_dict["Jefferson"] = 432438

# print(counties_dict)
# len(counties_dict)
# print(len(counties_dict))

# #get all keys and values
# print(counties_dict.items())

# # List of dictionaries
# voting_data = []
# voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
# voting_data.append({"county":"Denver", "registered_voters": 463353})
# voting_data.append({"county":"Jefferson", "registered_voters": 432438})

# print(voting_data)


# # Decision Statements
# # How many votes did you get?
# my_votes = int(input("How many votes did you get in the election? "))
# #  Total votes in the election
# total_votes = int(input("What is the total votes in the election? "))
# # Calculate the percentage of votes you received.
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])

# # If-else practice

# temperature = int(input("What is the temperature outside? "))

# if temperature > 80:
#     print("Turn on the AC.")
# else:
#     print("Open the windows.")

#What is the score?
# score = int(input("What is your test score? "))

# Complex if-else statements (if-elif-if)
# Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# else:
#     if score >= 80:
#         print('Your grade is a B.')
#     else:
#         if score >= 70:
#             print('Your grade is a C.')
#         else:
#             if score >= 60:
#                 print('Your grade is a D.')
#             else:
#                 print('Your grade is an F.')

# What is the score?
# score = int(input("What is your test score? "))

# Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# elif score >= 80:
#     print('Your grade is a B.')
# elif score >= 70:
#     print('Your grade is a C.')
# elif score >= 60:
#     print('Your grade is a D.')
# else:
#     print('Your grade is an F.')


# Membership Operations
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

# Iterate through list
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties:
    print(county)

for voters in counties_dict.values():
    print(voters)
for county, voters in counties_dict.items():
    print(county, voters)
# Skill Drill: Printing county and voter info into string
for county, voters in counties_dict.items():
    print(county, "county has", voters, "registered voters")


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

# Get each dictinary in a list of dictionaries
for county_dict in voting_data:
    print(county_dict)

# Values from a list of Dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)


# Editing code to use f-strings
# # Original
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

# # f-strings
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")


counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


# Multiline f-strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
    # f"You received {candidate_votes} number of votes. "
    # f"The total number of votes in the election was {total_votes}. "
    # f"You received {candidate_votes / total_votes * 100}% of the total votes.")
# percentage formatted to 2 decimal places
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
print(message_to_candidate)

# format number in f-string:
# f'{value:{width}.{precision}}'


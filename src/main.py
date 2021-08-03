#lesson 39
'''
import random

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random() * 5
print(random_float)
'''

#lesson40

#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
'''
import random
print("Heads or Tail game \n")

random_coin = random.randint(0, 1)

if random_coin == 0:
    print(f"You have got Tails")
else:
    print(f"You have got Heads")


print(random_coin)
'''

#lesson 41
'''
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

states_of_america[1] = "Pencilvania"
states_of_america.append("VadymLand")
states_of_america.extend(["Angelalanda", "DogLand"])
print(states_of_america[-1])
'''

'''
#lesson42

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

print(names)

length_of_the_string = len(names)
print(length_of_the_string)

who_pays_numer = random.randint(0, length_of_the_string - 1)
print(who_pays_numer)

print(names[who_pays_numer])

'''

#lesson43

#fruits
#dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

#lesson44

'''
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
'''
'''
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)


print(dirty_dozen[1][2])
print(dirty_dozen[1][3])
'''

#lesson 45

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
computer_choice = random.randint(0, 2)

if player_choice != computer_choice:
    if player_choice == 0 and computer_choice == 1:
        print(f"Player chose {rock} \n Computer chose {paper} \n Computer won")
    elif player_choice == 0 and computer_choice == 2:
        print(f"Player chose {rock} \n Computer chose {scissors} \n You won")
    elif player_choice == 1 and computer_choice == 0:
        print(f"Player chose {paper} \n Computer chose {rock} \n You won")
    elif player_choice == 1 and computer_choice == 2:
        print(f"Player chose {paper} \n Computer chose {scissors} \n Computer won")
    elif player_choice == 2 and computer_choice == 0:
        print(f"Player chose {scissors} \n Computer chose {rock} \n computer won")
    else:
        print(f"Player chose {scissors} \n Computer chose {paper} \n You won")
else:
    print("Draw")

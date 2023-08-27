#This app will ask classmates their name and a few questions about themselves.
#Afterward, the app will share the answers given by the classmates.

#Greeting
print('Welcome back to school! Answer these 3 questions to introduce yourself!')

#Question 1
name = input('What is your name? ')
print(name)

#Question 2
favorite_color = input('What is your favorite color? ')
print(favorite_color)

#Question 3
favorite_sport = input('What is your favorite sport? ')
print(favorite_sport)

#Question 4
favorite_activity = input('What is your favorite activity? ')
print(favorite_activity)

#Question 5
print(f"Everyone, meet {name}! {name}'s favorite color is {favorite_color}. {name}'s favorite sport is {favorite_sport}. {name}'s favorite activity is {favorite_activity}.")

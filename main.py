# will respond with 'Hello {name}' once input is answered
print("Welcome to the Band Name Generator.\nTo start, please answer the below prompts.")

city = input("What city did you grow up in?\n")
pet_name = input("What is the name of a pet?\n")
band_name = city + ' ' + pet_name

print("Your new band name is: " + band_name)
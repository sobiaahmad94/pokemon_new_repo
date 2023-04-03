# Creating variables of different data types

# Strings
pokemon_1 = "Pikachu"
pokemon_2 = "Charmander"


# Integers
pikachu_card_number = 25
charmander_card_number = 4

# Floating point
pikachu_height = 90.4
charmander_height = 103.7

# Calling some methods/functions with these variables and using operators on the functions

def pikachu_facts():
    print(pokemon_1 + " is " + str(pikachu_height) + " metres tall and is card number #" + str(pikachu_card_number) + " within the Pokedex.")


def charmander_facts():
    print(pokemon_2 + " is " + str(charmander_height) + " metres tall and is card number #" + str(charmander_card_number) + " within the Pokedex.")

def pikachu_charmander_height_difference():
    pokemon_height_difference =  charmander_height - pikachu_height
    print(round(pokemon_height_difference, 2))



# Calling/invoking the functions created above
pikachu_facts()
charmander_facts()
pikachu_charmander_height_difference()
    


#import pokebase as pb
import pokepy

#Gen1
min_gen_one = 1
max_gen_one = 151

#Gen2
min_gen_two = 152
max_gen_two = 251

#Gen3
min_gen_three = 252
max_gen_three = 386

#Gen4
min_gen_four = 387
max_gen_four = 493

#Gen5
min_gen_five = 494
max_gen_five = 649

#Gen6
min_gen_six = 650
max_gen_six = 721

#Gen7
min_gen_seven = 722
max_gen_seven = 809

#Gen8
min_gen_eight = 810
max_gen_eight = 898

class Pokemon:
    def __init__(self, name, nickname, number, height, weight, type1, type2, ability1, ability2, image_png):
        self.name = name
        self.nickname = nickname
        self.number = number
        self.height = height
        self.weight = weight
        self.type1 = type1
        self.type2 = type2
        self.ability1 = ability1
        self.ability2 = ability2
        self.image_png = image_png

def get_pokemon_by_number(number):
    return client.get_pokemon(number)[0]

def get_pokemon_by_name(name):
    return client.get_pokemon(name)[0]

def get_pokemon_name_by_number(number):
    return get_pokemon_by_number(number).name.capitalize()

def get_pokemon_number_by_name(name):
    return get_pokemon_by_name(name).id

def get_pokemon_weight(number):
    return get_pokemon_by_number(number).weight

def get_pokemon_height(number):
    return get_pokemon_by_number(number).height

def get_pokemon_types(number):
    types = get_pokemon_by_number(number).types
    type_names = []
    type_names.append(types[0].type.name.capitalize())
    if len(types) > 1:
        type_names.append(types[1].type.name.capitalize())
    else:
        type_names.append(None)

    return type_names

def get_pokemon_abilities(number):
    abilities = get_pokemon_by_number(number).abilities
    ability_names = []
    ability_names.append(abilities[0].ability.name.capitalize())
    if len(abilities) > 1:
        ability_names.append(abilities[1].ability.name.capitalize())
    else:
        ability_names.append(None)

    return ability_names

def get_pokemon_image_link(number):
    return str(get_pokemon_by_number(number).sprites).split("|")[1].strip()

if __name__ == "__main__":
    client = pokepy.V2Client()
    number = input("Enter number: ")
    print(get_pokemon_name_by_number(number))
    print(get_pokemon_height(number))
    print(get_pokemon_weight(number))
    print(get_pokemon_types(number))
    print(get_pokemon_abilities(number))
    print(get_pokemon_image_link(number))


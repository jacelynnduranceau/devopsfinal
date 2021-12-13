#import pokebase as pb
import re
import pokepy

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

# def get_poke_info(number):
#     id = strip_zeros(number)
#     name = get_pokemon_name_by_number(id)
#     number_pokemon = append_zeros(id)
#     height = get_pokemon_height(id)
#     weight = get_pokemon_weight(id)
#     types = get_pokemon_types(id)
#     abilities = get_pokemon_abilities(id)
#     image = get_pokemon_image_link(id)
#     return [name, number_pokemon, height, weight, types, abilities, image]

# def random_pokemon(number):
#     info = get_poke_info(number)
#     name = info[0]
#     number_pokemon = info[1]
#     height = info[2]
#     weight = info[3]
#     types = info[4]
#     abilities = info[5]
#     image = info[6]
#     pokemon = Pokemon(name, '-', number_pokemon, height, weight, types[0], \
#         types[1], abilities[0], abilities[1], image)
#     return pokemon

def create_pokemon(number):
    name = get_pokemon_name_by_number(number)
    number_pokemon = append_zeros(number)
    height = get_pokemon_height(number)
    weight = get_pokemon_weight(number)
    types = get_pokemon_types(number)
    abilities = get_pokemon_abilities(number)
    image = get_pokemon_image_link(number)
    pokemon = Pokemon(name, '-', number_pokemon, height, weight, types[0], \
        types[1], abilities[0], abilities[1], image)
    return pokemon

def append_zeros(number):
    #1-9
    if int(number) < 10:
        return "00" + str(number)
    #10-99
    elif int(number) > 9 and int(number) < 100:
        return "0" + str(number)
    #100-898
    else:
        return number

def get_pokemon_by_number(number):
    client = pokepy.V2Client()
    return client.get_pokemon(number)[0]

def get_pokemon_by_name(name):
    client = pokepy.V2Client()
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
        type_names.append("-")

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
    return str(get_pokemon_by_number(number).sprites).split("|")[1].strip().replace(">","")

if __name__ == "__main__":
    client = pokepy.V2Client()
    number = input("Enter number: ")
    print(get_pokemon_name_by_number(number))
    print(get_pokemon_height(number))
    print(get_pokemon_weight(number))
    print(get_pokemon_types(number))
    print(get_pokemon_abilities(number))
    print(get_pokemon_image_link(number))


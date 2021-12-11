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
    def __init__(self, name, nickname, id, height, weight, type1, type2, ability1, ability2, image_png):
        self.name = name
        self.nickname = nickname
        self.id = id
        self.height = height
        self.weight = weight
        self.type1 = type1
        self.type2 = type2
        self.ability1 = ability1
        self.ability2 = ability2
        self.image_png = image_png

def get_pokemon_by_id(id):
    return client.get_pokemon(id)[0]

def get_pokemon_by_name(name):
    return client.get_pokemon(name)[0]

def get_pokemon_name_by_id(id):
    return get_pokemon_by_id(id).name.capitalize()

def get_pokemon_id_by_name(name):
    return get_pokemon_by_name(name).id

def get_pokemon_weight(id):
    return get_pokemon_by_id(id).weight

def get_pokemon_height(id):
    return get_pokemon_by_id(id).height

def get_pokemon_types(id):
    types = get_pokemon_by_id(id).types
    type_names = []
    type_names.append(types[0].type.name.capitalize())
    if len(types) > 1:
        type_names.append(types[1].type.name.capitalize())
    else:
        type_names.append(None)

    return type_names

def get_pokemon_abilities(id):
    abilities = get_pokemon_by_id(id).abilities
    ability_names = []
    ability_names.append(abilities[0].ability.name.capitalize())
    if len(abilities) > 1:
        ability_names.append(abilities[1].ability.name.capitalize())
    else:
        ability_names.append(None)

    return ability_names

def get_pokemon_image_link(id):
    return str(get_pokemon_by_id(id).sprites).split("|")[1].strip()

if __name__ == "__main__":
    client = pokepy.V2Client()
    id = input("Enter id: ")
    print(get_pokemon_name_by_id(id))
    print(get_pokemon_height(id))
    print(get_pokemon_weight(id))
    print(get_pokemon_types(id))
    print(get_pokemon_abilities(id))
    print(get_pokemon_image_link(id))


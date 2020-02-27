import json
import matplotlib.pyplot as plt
import requests

if __name__ == "__main__":

    poke_url = "https://pokeapi.co/api/v2/pokemon/"

    pokemon_json = requests.get(poke_url).text
    pokemon = json.loads(pokemon_json)
    poke_list = (pokemon['results'])
    print(len(pokemon['results']))
    print(pokemon['next'])

    ids = []
    weights = []

    for pokemanz in poke_list:
        print(pokemanz['name'])
        more_info = pokemanz['url']
        info_json = requests.get(more_info).json()
        print(info_json['weight'])
        weights.append(info_json['weight'])
        ids.append(info_json['id'])

    print(weights)
    plt.plot(ids, weights)
    plt.xlabel("IDs")
    plt.ylabel("Weights")
    plt.show()

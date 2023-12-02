import requests

response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons', 
                          json= {                                        
    "name": "generate",
    "photo": "generate",
},
headers={'Content-Type': 'application/json',
         "trainer_token": "0ae67ce0b2c9e47d955afb1436fe0126"
         }, timeout=5)
print(f'Code: {response.status_code} - {response.reason}. Message: {response.text} ')


response = requests.put(url='https://api.pokemonbattle.me:9104/pokemons', 
                          json={
    "pokemon_id": "21020",
    "name": "Ержан",
    "photo": "https://dolnikov.ru/pokemons/albums/007.png",
},
headers={'Content-Type': 'application/json',
         "trainer_token": "0ae67ce0b2c9e47d955afb1436fe0126"}, timeout=5)
print(f'Code: {response.status_code} - {response.reason}. Message: {response.text} ')


response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball', 
                          json={
    "pokemon_id": "21020"
},
headers={'Content-Type': 'application/json',
         "trainer_token": "0ae67ce0b2c9e47d955afb1436fe0126"}, timeout=5)
print(f'Code: {response.status_code} - {response.reason}. Message: {response.text} ')




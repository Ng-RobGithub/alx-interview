import requests

def get_character(character_id):
    response = requests.get(f"https://swapi.dev/api/people/{character_id}/")
    return response.json()

character = get_character(1)
print(f"Name: {character['name']}")
print(f"Height: {character['height']} cm")
print(f"Mass: {character['mass']} kg")

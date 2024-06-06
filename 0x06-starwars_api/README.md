0x06-starwars_api

This project fetches and displays characters from Star Wars movies using the Star Wars API.

Objectives:
The main objectives of this project are to:

1. Understand how to interact with a RESTful API.
Explore SWAPI Documentation: Before you start coding, go through the SWAPI documentation. This will give you an overview of the endpoints available and the kind of data you can retrieve.

2. Learn how to make HTTP requests to retrieve data.
You will use the requests library in Python to make HTTP requests to the SWAPI. Install it using pip install requests.

Example Request: Here's an example of how to make a GET request to retrieve information about a specific character (Luke Skywalker):
""" import requests

response = requests.get('https://swapi.dev/api/people/1/')
data = response.json()
print(data)
"""

3. Parse and process the data returned by the API.
The data returned by SWAPI is in JSON format. You need to parse this JSON data to extract relevant information. Python's json module can help with this...
""" import json

response = requests.get('https://swapi.dev/api/people/1/')
data = response.json()
print(data['name'])  # Output: Luke Skywalker """

4. Implement various functionalities to interact with the data.
You might implement various functions to retrieve and display different types of data. Here are some examples:

Get All People:
""" def get_all_people():
    response = requests.get('https://swapi.dev/api/people/')
    data = response.json()
    return data['results'] """

5. Handling Pagination
SWAPI endpoints often return paginated results. You need to handle pagination to retrieve all results. This typically involves checking if there is a next field in the response and making additional requests as needed.
""" def get_all_people():
    people = []
    url = 'https://swapi.dev/api/people/'
    while url:
        response = requests.get(url)
        data = response.json()
        people.extend(data['results'])
        url = data['next']
    return people
"""
6. Advanced Features
Filtering and Searching: SWAPI allows filtering and searching. For example, you can search for people by name:

""" def search_people(name):
    response = requests.get(f'https://swapi.dev/api/people/?search={name}')
    return response.json()['results']
"""


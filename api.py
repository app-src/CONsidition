import json

import requests
from requests import RequestException

base_api_path = "https://api.considition.com/api/game/"
sess = None


def mapInfo(api_key, map_name):
    try:
        global sess
        if not sess:
            sess = requests.Session()
        response = sess.get(base_api_path + "mapInfo" + "?MapName=" +
                            map_name, headers={"x-api-key": api_key}, verify=True)  
        if response.status_code == 200:
            return response.json()

        print("Fatal Error: could not start game")
        print(str(response.status_code) + " " +
              response.reason + ": " + response.text)
    except RequestException as e:
        return "Fatal Error: could not start game"
        print("Fatal Error: could not start game")
        print("Something went wrong with the request: " + str(e))


def submit_game(api_key, map_name, solution):

    solution.addMapName(map_name)
    try:
        global sess
        if not sess:
            sess = requests.Session()
        response = sess.post(base_api_path + "submit",
                             headers={"x-api-key": api_key}, verify=True, json=json.loads(solution.toJSON()))
        if response.status_code == 200:
            return response.json()

        print("Fatal Error: could not submit game")
        print(str(response.status_code) + " " +
              response.reason + ": " + response.text)
    except RequestException as e:
        print("Fatal Error: could not submit game")
        print("Something went wrong with the request: " + str(e))
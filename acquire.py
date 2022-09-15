import requests
import env
import os
import pandas as pd
import json
from env import Client_ID
from igdb.wrapper import IGDBWrapper


def connect_api():
    url = env.get_db_url()
    response = requests.post(url)
    data = response.json()
    access_token = data['access_token']
    return access_token


def connect_to_games():
    headers = {'Client-ID': f'{Client_ID}', 'Authorization': f'Bearer {access_token}'}
    data = 'fields *; popularity;sort popularity desc;'
    r = requests.post('https://api.igdb.com/v4/games' ,data=data ,  headers=headers)
    return r

def run_wrapper():
    wrapper = IGDBWrapper(f'{Client_ID}', f'{access_token}')
    return wrapper


# function that puts response list object into a dataframe for each page
def get_game_library(wrapper):
    game_library = pd.DataFrame()
    for i in range (0, 409):
        games = wrapper.api_request('games', 'fields *; limit 500;' f'offset {i * 500};')
        y = json.loads(games)
        results_df =pd.DataFrame(y)
        game_library = pd.concat([game_library, results_df])
    return game_library


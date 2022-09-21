import requests
import env
from requests.models import Request, Response
from env import Client_ID
import pandas as pd
from igdb.igdbapi_pb2 import GameResult
from typing import Dict, List, Optional, Union, cast
import acquire
import json

## for platforms**

def get_platforms():
    headers = {'Client-ID': f'{Client_ID}', 'Authorization': f'Bearer {access_token}'}
    data = 'fields *; '
    r = requests.post('https://api.igdb.com/v4/platforms' ,data=data ,  headers=headers)
    platforms = wrapper.api_request('platforms', 'fields *;limit 500;')
    x = json.loads(platforms)
    platforms =pd.DataFrame(x)
    return platforms


# make dict for missing value 
platform_dict[92] = 'not_available'

# to make index and dict
platformlist = platform[['id' , 'name']].sort_values(by='id').reset_index(drop=True)
platform_dict = platformlist.set_index('id').to_dict()['name']


#
def test_funct(random_list):
    if type(random_list) == list:
        return [platform_dict[i] for i in random_list]
    else:  
        return "Not available"

    
    
df['platforms'] = df.platforms.apply(test_funct)



#### for themes ###


def get_themes():
    headers = {'Client-ID': f'{Client_ID}', 'Authorization': f'Bearer {access_token}'}
    data = 'fields *; '
    r = requests.post('https://api.igdb.com/v4/themes' ,data=data ,  headers=headers)
    themes = wrapper.api_request('themes', 'fields *;limit 500;')
    x = json.loads(themes)
    themes=pd.DataFrame(x)
    return themes

# set dict and index
themes_list = themes[['id' , 'name']].sort_values(by='id').reset_index(drop=True)
themes_dict = themes.set_index('id').to_dict()['name']


def test_funct5(random_list):
    if type(random_list) == list:
        return [themes_dict[i] for i in random_list]
    else:  
        return "Not available"

    
df['themes'] = pd.DataFrame(df.themes.apply(test_funct5))



# for player perspective##


def get_player_perspectives():
    headers = {'Client-ID': f'{Client_ID}', 'Authorization': f'Bearer {access_token}'}
    data = 'fields *; '
    r = requests.post('https://api.igdb.com/v4/player_perspectives' ,data=data ,  headers=headers)
    player_perspectives = wrapper.api_request('player_perspectives', 'fields *;limit 500;')
    x = json.loads(player_perspectives)
    player_perspectives=pd.DataFrame(x)
    return player_perspectives


#set index and dict
player_perspectives_list = player_perspectives[['id' , 'name']].sort_values(by='id').reset_index(drop=True)
player_perspectives_dict = player_perspectives.set_index('id').to_dict()['name']


def test_funct4(random_list):
    if type(random_list) == list:
        return [player_perspectives_dict[i] for i in random_list]
    else:  
        return "Not available"


df['player_perspectives'] = pd.DataFrame(df.player_perspectives.apply(test_funct4))


## for genres ##

# function that puts response list object into a dataframe for each page
def get_genres(wrapper):
    genres = pd.DataFrame()
    for i in range (0, 409):
        genre = wrapper.api_request('genres', 'fields *; limit 500;')
        y = json.loads(genre)
        results_df =pd.DataFrame(y)
        genres = pd.concat([genres, results_df])
    return genres


genres = get_genres(wrapper)
# set index and dict
genreslist = genres[['id' , 'slug']].sort_values(by='id').reset_index(drop=True)
genres_dict = genreslist.set_index('id').to_dict()['slug']

# run function
def test_functg(random_list):
    if type(random_list) == list:
        return [genres_dict[i] for i in random_list]
    else:  
        return "Not available" 


# apply function to games_library
game_library['genres'] = pd.DataFrame(game_library.genres.apply(test_functg))



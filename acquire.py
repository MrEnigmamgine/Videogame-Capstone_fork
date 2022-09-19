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

# function that puts response list object into a dataframe 
def get_genres(wrapper):
    genres = pd.DataFrame()
    for i in range (0, 409):
        genres = wrapper.api_request('genres', 'fields *; limit 500;')
        y = json.loads(games)
        results_df =pd.DataFrame(y)
        genres = pd.concat([genres, results_df])
    return genres


def get_age_ratings(wrapper):
    age_ratings = pd.DataFrame()
    for i in range (0, 409):
        a_ratings = wrapper.api_request('age_ratings', 'fields *; limit 500;' f'offset {i * 500};')
        y = json.loads(a_ratings)
        results_df =pd.DataFrame(y)
        age_ratings = pd.concat([age_ratings, results_df])
    return age_ratings


def get_age_rating_desc(wrapper):
    age_ratings_desc = pd.DataFrame()
    for i in range (0, 409):
        a_ratings = wrapper.api_request('age_rating_content_descriptions', 'fields *; limit 500;' f'offset {i * 500};')
        y = json.loads(a_ratings)
        results_df =pd.DataFrame(y)
        age_ratings_desc = pd.concat([age_ratings_desc, results_df])
    return age_ratings_desc

def get_characters(wrapper):
    characters = pd.DataFrame()
    for i in range (0, 409):
        a_ratings = wrapper.api_request('characters', 'fields *; limit 500;' f'offset {i * 500};')
        y = json.loads(a_ratings)
        results_df =pd.DataFrame(y)
        characters = pd.concat([characters, results_df])
    return characters


def get_collections(wrapper):
    collections = pd.DataFrame()
    for i in range (0, 409):
        a_ratings = wrapper.api_request('collections', 'fields *; limit 500;' f'offset {i * 500};')
        y = json.loads(a_ratings)
        results_df =pd.DataFrame(y)
        collections = pd.concat([collections, results_df])
    return collections

def get_franchises(wrapper):
    franchises = pd.DataFrame()
    for i in range (0, 409):
        a_ratings = wrapper.api_request('franchises', 'fields *; limit 500;' f'offset {i * 500};')
        y = json.loads(a_ratings)
        results_df =pd.DataFrame(y)
        franchises = pd.concat([franchises, results_df])
    return franchises

def get_game_engines(wrapper):
    game_engines = pd.DataFrame()
    for i in range (0, 409):
        a_ratings = wrapper.api_request('game_engines', 'fields *; limit 500;' f'offset {i * 500};')
        y = json.loads(a_ratings)
        results_df =pd.DataFrame(y)
        game_engines = pd.concat([game_engines, results_df])
    return game_engines

def get_game_modes(wrapper):
    game_modes = pd.DataFrame()
    for i in range (0, 1):
        a_ratings = wrapper.api_request('game_modes', 'fields *; limit 500;')
        y = json.loads(a_ratings)
        results_df =pd.DataFrame(y)
        game_modes = pd.concat([game_modes, results_df])
    return game_modes




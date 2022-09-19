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

access_token = connect_api()

def connect_to_games():
    headers = {'Client-ID': f'{Client_ID}', 'Authorization': f'Bearer {access_token}'}
    data = 'fields *; popularity;sort popularity desc;'
    r = requests.post('https://api.igdb.com/v4/games' ,data=data ,  headers=headers)
    return r

def run_wrapper():
    wrapper = IGDBWrapper(f'{Client_ID}', f'{access_token}')
    return wrapper

wrapper = run_wrapper()

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

def get_companies(wrapper):
    companies= pd.DataFrame()
    for i in range (0, 409):
        company = wrapper.api_request('companies', 'fields *; limit 500;' f'offset {i * 500};')
        y = json.loads(company)
        results_df =pd.DataFrame(y)
        companies = pd.concat([companies, results_df])
    return companies

def get_multi_player_modes(wrapper):
    multi_player_modes= pd.DataFrame()
    for i in range (0, 409):
        modes = wrapper.api_request('multiplayer_modes', 'fields *; limit 500;' f'offset {i * 500};')
        y = json.loads(modes)
        results_df =pd.DataFrame(y)
        multi_player_modes = pd.concat([multi_player_modes, results_df])
    return multi_player_modes

def get_platform_families(wrapper):
    platform_families= pd.DataFrame()
    for i in range (0, 409):
        modes = wrapper.api_request('platform_families', 'fields *; limit 500;' f'offset {i * 500};')
        y = json.loads(modes)
        results_df =pd.DataFrame(y)
        platform_families = pd.concat([platform_families, results_df])
    return platform_families

def get_platform_version_release_dates(wrapper):
    platform_version_release_dates= pd.DataFrame()
    for i in range (0, 409):
        modes = wrapper.api_request('platform_version_release_dates', 'fields *; limit 500;' f'offset {i * 500};')
        y = json.loads(modes)
        results_df =pd.DataFrame(y)
        platform_version_release_dates = pd.concat([platform_version_release_dates, results_df])
    return platform_version_release_dates

def get_platform_version_companies(wrapper):
    platform_version_release_companies= pd.DataFrame()
    for i in range (0, 409):
        modes = wrapper.api_request('platform_version_companies', 'fields *; limit 500;' f'offset {i * 500};')
        y = json.loads(modes)
        results_df =pd.DataFrame(y)
        platform_version_release_companies = pd.concat([platform_version_release_companies, results_df])
    return platform_version_release_companies

def get_platforms(wrapper):
    platforms= pd.DataFrame()
    for i in range (0, 409):
        modes = wrapper.api_request('platforms', 'fields *; limit 500;' f'offset {i * 500};')
        y = json.loads(modes)
        results_df =pd.DataFrame(y)
        platforms = pd.concat([platforms, results_df])
    return platforms

def get_release_dates(wrapper):
    release_dates= pd.DataFrame()
    for i in range (0, 409):
        modes = wrapper.api_request('release_dates', 'fields *; limit 500;' f'offset {i * 500};')
        y = json.loads(modes)
        results_df =pd.DataFrame(y)
        release_dates = pd.concat([release_dates, results_df])
    return release_dates

def get_platform_versions(wrapper):
    platform_versions= pd.DataFrame()
    for i in range (0, 409):
        modes = wrapper.api_request('platform_versions', 'fields *; limit 500;' f'offset {i * 500};')
        y = json.loads(modes)
        results_df =pd.DataFrame(y)
        platform_versions = pd.concat([platform_versions, results_df])
    return platform_versions

def get_player_perspectives(wrapper):
    player_perspectives= pd.DataFrame()
    for i in range (0, 409):
        modes = wrapper.api_request('player_perspectives', 'fields *; limit 500;' f'offset {i * 500};')
        y = json.loads(modes)
        results_df =pd.DataFrame(y)
        player_perspectives = pd.concat([player_perspectives, results_df])
    return player_perspectives

def get_themes(wrapper):
    themes= pd.DataFrame()
    for i in range (0, 409):
        modes = wrapper.api_request('themes', 'fields *; limit 500;' f'offset {i * 500};')
        y = json.loads(modes)
        results_df =pd.DataFrame(y)
        themes = pd.concat([themes, results_df])
    return themes






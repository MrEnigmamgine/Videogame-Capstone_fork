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
        genre = wrapper.api_request('genres', 'fields *; limit 500;')
        y = json.loads(genre)
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

def get_involved_companies(wrapper):
    involved_companies= pd.DataFrame()
    for i in range (0, 409):
        i_company = wrapper.api_request('involved_companies', 'fields *; limit 500;' f'offset {i * 500};')
        y = json.loads(i_company)
        results_df =pd.DataFrame(y)
        involved_companies = pd.concat([involved_companies, results_df])
    return involved_companies

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

def get_game_version_features(wrapper):
    game_version_features = pd.DataFrame()
    for i in range (0, 409):
        a_ratings = wrapper.api_request('game_version_features', 'fields *; limit 500;' f'offset {i * 500};')
        y = json.loads(a_ratings)
        results_df =pd.DataFrame(y)
        game_version_features = pd.concat([game_version_features, results_df])
    return game_version_features


def get_game_version_feature_values(wrapper):
    game_version_feature_values = pd.DataFrame()
    for i in range (0, 409):
        a_ratings = wrapper.api_request('game_version_feature_values', 'fields *; limit 500;' f'offset {i * 500};')
        y = json.loads(a_ratings)
        results_df =pd.DataFrame(y)
        game_version_feature_values = pd.concat([game_version_feature_values, results_df])
    return game_version_feature_values

def get_game_version(wrapper):
    game_versions = pd.DataFrame()
    for i in range(0,409):
        game_version = wrapper.api_request('game_versions', 'fields *;limit 500;')
        y = json.loads(game_version)
        results_df =pd.DataFrame(y)
        game_versions = pd.concat([game_versions, results_df])
    return game_versions

def import_workbook():
    # brings manually created workbook in notebook as list object
    df_sheet_all = pd.read_excel('manual_reference_data_tables_for_IGDB_API.xlsx', sheet_name=None)
    # following codes makes dataframes for each sheet in the workbook
    age_ratings_enums_category = pd.read_excel('manual_reference_data_tables_for_IGDB_API.xlsx', sheet_name='age_ratings_enums_category')
    age_ratings_enums_rating = pd.read_excel('manual_reference_data_tables_for_IGDB_API.xlsx', sheet_name='age_ratings_enums_rating')
    age_ratings_descriptions_enums_ = pd.read_excel('manual_reference_data_tables_for_IGDB_API.xlsx', sheet_name='age_ratings_descriptions_enums_')
    character_enums_gender = pd.read_excel('manual_reference_data_tables_for_IGDB_API.xlsx', sheet_name='character_enums_gender')
    character_enums_species = pd.read_excel('manual_reference_data_tables_for_IGDB_API.xlsx', sheet_name='character_enums_species')
    company_enums_change_date_categ = pd.read_excel('manual_reference_data_tables_for_IGDB_API.xlsx', sheet_name='company_enums_change_date_categ')
    company_enums_start_date_catego = pd.read_excel('manual_reference_data_tables_for_IGDB_API.xlsx', sheet_name='company_enums_start_date_catego')
    external_game_enums_category = pd.read_excel('manual_reference_data_tables_for_IGDB_API.xlsx', sheet_name='external_game_enums_category')
    external_game_enums_media = pd.read_excel('manual_reference_data_tables_for_IGDB_API.xlsx', sheet_name='external_game_enums_media')
    company_website_enums_category = pd.read_excel('manual_reference_data_tables_for_IGDB_API.xlsx', sheet_name='company_website_enums_category')
    game_enums_category = pd.read_excel('manual_reference_data_tables_for_IGDB_API.xlsx', sheet_name='game_enums_category')
    game_enums_status = pd.read_excel('manual_reference_data_tables_for_IGDB_API.xlsx', sheet_name='game_enums_status')
    game_version_feature_eums_categ = pd.read_excel('manual_reference_data_tables_for_IGDB_API.xlsx', sheet_name='game_version_feature_eums_categ')
    game_feature_value_enums_includ = pd.read_excel('manual_reference_data_tables_for_IGDB_API.xlsx', sheet_name='game_feature_value_enums_includ')
    platform_enums_category = pd.read_excel('manual_reference_data_tables_for_IGDB_API.xlsx', sheet_name='platform_enums_category')
    platform_version_release_date_c = pd.read_excel('manual_reference_data_tables_for_IGDB_API.xlsx', sheet_name='platform_version_release_date_c')
    platform_version_release_date_r = pd.read_excel('manual_reference_data_tables_for_IGDB_API.xlsx', sheet_name='platform_version_release_date_r')
    release_date_category = pd.read_excel('manual_reference_data_tables_for_IGDB_API.xlsx', sheet_name='release_date_category')
    release_date_region = pd.read_excel('manual_reference_data_tables_for_IGDB_API.xlsx', sheet_name='release_date_region')
    platform_website_enums_category = pd.read_excel('manual_reference_data_tables_for_IGDB_API.xlsx', sheet_name='platform_website_enums_category')
    website_enums_category = pd.read_excel('manual_reference_data_tables_for_IGDB_API.xlsx', sheet_name='website_enums_category')

    return age_ratings_enums_category , age_ratings_enums_rating , age_ratings_descriptions_enums_ , character_enums_gender , character_enums_species , company_enums_change_date_categ ,  company_enums_start_date_catego , external_game_enums_category , external_game_enums_media , company_website_enums_category, game_enums_category, game_enums_status, game_version_feature_eums_categ, game_feature_value_enums_includ , platform_enums_category , platform_version_release_date_c , platform_version_release_date_r , release_date_category , release_date_region , platform_website_enums_category , website_enums_category

# Use the code below to bring all sheets into notebook
age_ratings_enums_category , age_ratings_enums_rating , age_ratings_descriptions_enums_ , character_enums_gender , character_enums_species , company_enums_change_date_categ ,  company_enums_start_date_catego , external_game_enums_category , external_game_enums_media , company_website_enums_category, game_enums_category, game_enums_status, game_version_feature_eums_categ, game_feature_value_enums_includ , platform_enums_category , platform_version_release_date_c , platform_version_release_date_r , release_date_category , release_date_region , platform_website_enums_category , website_enums_category = import_workbook()






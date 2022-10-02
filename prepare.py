import env
import pandas as pd
import json
from env import Client_ID
from igdb.wrapper import IGDBWrapper
import time
import acquire
import numpy as np
import seaborn as sns

def import_table(variable):
        path = variable['path']
        getter = variable['getter']
        if not os.path.exists(path):
            wrapper = acquire.run_wrapper()
            df = getter(wrapper)
            df = df.reset_index().drop(columns=['index'])
            df.to_json(path)
        else:
            df = pd.read_json(path)
        return df

config = {
        'game_library' : {
            'path' : 'data/game_library.json',
            'getter': acquire.get_game_library
        },
        'genres' : {
            'path' : 'data/genres.json',
            'getter': acquire.get_genres
        },
        'age_ratings' : {
            'path' : 'data/age_ratings.json',
            'getter': acquire.get_age_ratings
        },
        'age_rating_desc' : {
            'path' : 'data/age_rating_desc.json',
            'getter': acquire.get_age_rating_desc
        },
        'collections' : {
            'path' : 'data/collections.json',
            'getter': acquire.get_collections
        },
        'game_modes' : {
            'path' : 'data/game_modes.json',
            'getter': acquire.get_game_modes
        },
        'multi_player_modes' : {
            'path' : 'data/multi_player_modes.json',
            'getter': acquire.get_multi_player_modes
        },
        'platforms' : {
            'path' : 'data/platforms.json',
            'getter': acquire.get_platforms
        },
        'platform_families' : {
            'path' : 'data/platform_families.json',
            'getter': acquire.get_platform_families
        },
        'player_perspectives' : {
            'path' : 'data/player_perspectives.json',
            'getter': acquire.get_player_perspectives
        },
        'themes' : {
            'path' : 'data/themes.json',
            'getter': acquire.get_themes
        },
        'game_engines' : {
            'path' : 'data/game_engines.json',
            'getter': acquire.get_game_engines
        },
        'age_rating_desc' : {
            'path' : 'data/age_rating_desc.json',
            'getter': acquire.get_age_rating_desc
        },
    }


# If wanting to retrive all tables from the config dict
def get_tables():
    tables = {}
    for key, value in config.items():
        tables[key] = import_table(value)
        print(f'Completed import for {key}')
    return tables


def wrangle_data():
    # Scoped function to help with column expansion
    def my_list(column, word):
        if word in column:
            return 1
        else:
            return 0
    # Get cached data or download data if not cached
    tables = get_tables()
    # Define columns to keep in the final df
    to_keep = [
        'id',
        'first_release_date',
        'genres',
        'name',
        'platforms',
        'slug',
        'age_ratings',
        'game_modes',
        'player_perspectives',
        'themes',
        # 'game_engines',
        'rating',
        # 'collection',
        'multiplayer_modes',
        'dlcs',
    ]
    # Add another pointer to game library for sanity's sake
    game_library = tables['game_library']
    # Trim down to only columns we care about
    game_library = game_library[to_keep].copy()
    # Convert release date to a datetime object
    game_library['first_release_date'] = pd.to_datetime(game_library['first_release_date'],unit='s')
    
    #########
    # Multiplayer modes
    ########

    # Add multiplayer modes
    tables['multi_player_modes'].rename(columns={'id': 'multi_player_mode_id'}, inplace=True)
    # dataframe merging age ratings and age ratings enuns ratings. will need to replace context description with text values
    game_library = pd.merge(
            game_library, tables['multi_player_modes'], how='left', left_on = 'id', right_on = 'game'
            ).drop(columns=[ 'game', 
                            'checksum', 
                            'multi_player_mode_id', 
                            'platform'
                            ])
    # fill nulls with 0 or bool lean False
    game_library['campaigncoop'].fillna(False, inplace = True)
    game_library['dropin'].fillna(False, inplace = True)
    game_library['lancoop'].fillna(False, inplace = True)
    game_library['offlinecoop'].fillna(False, inplace = True)
    game_library['offlinemax'].fillna(0, inplace = True)
    game_library['onlinecoop'].fillna(False, inplace = True)
    game_library['splitscreen'].fillna(False, inplace = True)
    game_library['offlinecoopmax'].fillna(0, inplace = True)
    game_library['onlinecoopmax'].fillna(0, inplace = True)
    game_library['onlinemax'].fillna(0, inplace = True)

    game_library.drop(columns=['multiplayer_modes'], inplace=True)

    #########
    # Genres
    ########
    # Transform genres list to a list of strings instead of a list of ids
    genres_list = tables['genres'][['id' , 'slug']].sort_values(by='id').reset_index(drop=True)
    genres_dict = genres_list.set_index('id').to_dict()['slug']
    def convert_genres_col(random_list):
        if type(random_list) == list:
            return [genres_dict[i] for i in random_list]
        else:  
            return ['Not available']
    game_library['genres'] = pd.DataFrame(game_library.genres.apply(convert_genres_col))
    # list of genres to add
    genres = ['point-and-click', 'fighting', 'shooter', 'music', 'platform', 'puzzle', 'racing', 'real-time-strategy-rts', 'role-playing-rpg', 'simulator', 'sport', 'strategy', 'turn-based-strategy-tbs', 'tactical', 'hack-and-slash-beat-em-up', 'quiz-trivia', 'pinball', 'adventure', 'indie', 'arcade', 'visual-novel', 'card-and-board-game', 'moba']
    # function to loop through column list and check for genre
    for item in genres:
        game_library[item] = game_library['genres'].apply(my_list, word=item)

    #########
    # Game Modes
    ########

    # Transform game modes ids to strings
    gamemodes_list = tables['game_modes'][['id' , 'slug']].sort_values(by='id').reset_index(drop=True)
    gamemodes_dict = gamemodes_list.set_index('id').to_dict()['slug']
    def convert_gamemodes_col(random_list):
        if type(random_list) == list:
            return [gamemodes_dict[i] for i in random_list]
        else:  
            return ["Not available"]
    game_library['game_modes'] = pd.DataFrame(game_library.game_modes.apply(convert_gamemodes_col))

    modes = ['single-player', 'multiplayer', 'co-operative', 'split-screen', 'massively-multiplayer-online-mmo', 'battle-royale']
    for mode in modes:
        game_library[mode] = game_library['game_modes'].apply(my_list, word=mode)



    #########
    # Player perspectives
    ########

    # Convert player persectives
    player_perspectives_list = tables['player_perspectives'][['id' , 'slug']].sort_values(by='id').reset_index(drop=True)
    player_perspectives_dict = tables['player_perspectives'].set_index('id').to_dict()['slug']

    def convert_player_persectives_col(random_list):
        if type(random_list) == list:
            return [player_perspectives_dict[i] for i in random_list]
        else:  
            return  ["Not available"]

    game_library['player_perspectives'] = pd.DataFrame(game_library.player_perspectives.apply(convert_player_persectives_col))

    players = ['First person', 'Third person', 'Bird view / Isometric', 'Text', 'Side view', 'Virtual Reality', 'Auditory'  'Drama']
    for player in players:
        game_library[player] = game_library['player_perspectives'].apply(my_list, word=player)
        
    # Themes 
    themes_list = tables['themes'][['id' , 'slug']].sort_values(by='id').reset_index(drop=True)
    themes_dict = tables['themes'].set_index('id').to_dict()['slug']

    # COnverts themes column to string then make each them a separte column
    def convert_themes_col(random_list):
        if type(random_list) == list:
            return [themes_dict[i] for i in random_list]
        else:  
            return  ["Not available"]

    game_library['themes'] = pd.DataFrame(game_library.themes.apply(convert_themes_col))

    themes = ['thriller', 'science-fiction', 'action', 'horror', 'survival',
        'fantasy', 'historical', 'stealth', 'comedy', 'business', 'drama',
        'non-fiction', 'kids', 'sandbox', 'open-world', 'warfare',
        '4x-explore-expand-exploit-and-exterminate', 'educational',
        'mystery', 'party', 'romance', 'erotic']
        
    for theme in themes:
        game_library[theme] = game_library['themes'].apply(my_list, word=theme)

    game_library.drop(columns=['themes'], inplace=True)

    # make a column for each platform
    platformslist = tables['platforms'][['id' , 'slug']].sort_values(by='id').reset_index(drop=True)
    platforms_dict = platformslist.set_index('id').to_dict()['slug']
    def convert_platforms(random_list):
        if type(random_list) == list:
            return [platforms_dict[i] for i in random_list]
        else:  
            return 'Not available'
    platforms_dict[92] = 'Not available'
    game_library['platforms'] = pd.DataFrame(game_library.platforms.apply(convert_platforms))
    game_library
    # list of platforms to add
    platforms = [
        'Linux', 
        'Nintendo 64', 
        'Wii', 
        'PC (Microsoft Windows)', 
        'PlayStation', 
        'PlayStation 2', 
        'PlayStation 3', 
        'Xbox', 
        'Xbox 360', 
        'DOS', 
        'Mac', 
        'Nintendo Entertainment System', 
        'Super Nintendo Entertainment System', 
        'Nintendo DS', 
        'Nintendo GameCube', 
        'Game Boy Color', 
        'Game Boy Advance', 
        'Sega Mega Drive/Genesis',
        'Sega Saturn', 
        'Game Boy', 
        'Android', 
        'Nintendo 3DS',
        'PlayStatio n Portable', 
        'iOS', 
        'Wii U', 
        'PlayStation Vita', 
        'Virtual Console (Nintendo)', 
        'PlayStation 4', 
        'Xbox One', 
        'Family Computer Disk System', 
        'Arcade', 
        'Windows Phone', 
        'Apple II', 
        'Web browser', 
        'Odyssey', 
        'Commodore 16', 
        'New Nintendo 3DS']

    for platform in platforms:
        game_library[platform] = game_library['platforms'].apply(my_list, word=platform)

    # Modified DLC column
    game_library['dlcs'] = game_library['dlcs'].fillna(0)

    def dlcs_col(df):
        game_library['has_dlcs'] = np.where(game_library.dlcs != 0, 1, 0)  
        return df
    game_library = dlcs_col(game_library)

    cols_to_drop =  [
        'genres',
        'platforms',
        'dlcs',
        'player_perspectives',
        'game_modes',
        'offlinemax' ,
        'offlinecoopmax',
        'onlinecoopmax',
        'onlinemax'

    ]
    game_library = game_library.drop(columns=cols_to_drop)
    def replace_booleans(data):
        for col in data:
            data[col].replace(True, 1, inplace=True)
            data[col].replace(False, 0, inplace=True)

    replace_booleans(game_library)
    return game_library
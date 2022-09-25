# Drops unessary columns from primary dataframe
game_library = game_library.drop(columns=['artworks', 'name', 'summary' , 'cover', 'created_at', 'external_games', 'screenshots', 'similar_games',  'tags', 'updated_at', 'url', 'videos', 'websites', 'checksum',  'alternative_names',  'keywords', 'status', 'rating_count', 'storyline', 'total_rating_count',  'hypes', 'follows', 'aggregated_rating_count'], inplace=True)

# fill columns nulls with 0
game_library = game_library["parent_game"].fillna(0, inplace = True)
game_library = game_library["franchise"].fillna(0, inplace = True)
game_library = game_library["collection"].fillna(0, inplace = True)

# convert columns from float type to integer type
game_library['parent_game'] = game_library['parent_game'].astype(int)
game_library['franchise'] = game_library['franchise'].astype(int)
game_library['collection'] = game_library['collection'].astype(int)


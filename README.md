<img src="igdb.jpeg" alt="drawing" width="150"/>

# <a name="top"></a>Videogame-Capstone
![]()
Kalpana Cohort 2022

By: Lindy Castellaw, Glady Barrios, Jarrid Jones 

<p>
  <a href="https://github.com/lindyc12" target="_blank">
    <img alt="Lindy" src="https://img.shields.io/github/followers/lindyc12?label=Follow_Lindy&style=social" />
  </a>
</p>

<p>
  <a href="https://github.com/mil2tech" target="_blank">
    <img alt="Jarrid" src="https://img.shields.io/github/followers/mil2tech?label=Follow_Jarrid&style=social" />
  </a>
</p>

<p>
  <a href="https://github.com/GladyBarrios" target="_blank">
    <img alt="Glady" src="https://img.shields.io/github/followers/GladyBarrios?label=Follow_Glady&style=social" />
  </a>
</p>
**Tools & Technologies Used:** 

![](https://img.shields.io/static/v1?message=Python&logo=python&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=Pandas&logo=pandas&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=SciKit-Learn&logo=scikit-learn&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=SciPy&logo=scipy&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=NumPy&logo=numpy&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=MatPlotLib&logo=python&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=Seaborn&logo=python&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=Tableau&logo=tableau&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=Canva&logo=canva&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=Markdown&logo=markdown&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=GitHub&logo=github&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=JupyterLab&logo=jupyter&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=Trello&logo=trello&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)

***
[[Project Description](#project_description)]
[[Project Planning](#planning)]
[[Data Dictionary](#dictionary)]
[[Data Acquire and Prep](#wrangle)]
[[Data Exploration](#explore)]
[[Modeling](#model)]
[[Conclusion](#conclusion)]
___

## <a name="project_description"></a>Project Description:

In Video games there are certain characteristics that make a videogame succesful such as high ratings. In this project we will investiage the certain variables that can create a high rating in a video game. We will analize the data from IGDB and investigate the best rated vidogames and what makes them so sucessfull. To achive this we will analize videogame data from Igdb and go through the data science pipe line, more specificly use classification models to able to predict video game ratings for future games.

[[Back to top](#top)]

***
## <a name="planning"></a>Project Planning: 
[[Back to top](#top)]

### Project Outline:


        
### Inital Questions

-  Do video games on certain platforms get better user ratings?
- what is the most common genre in games that are `subperb` (the highest rating)?
  - what about the three lowest ratings ((bad, very bad , awful)) ? what is the overall most highest genre in these low rating games?
  - what about the three highest ratings (good, great, subperb) ? what is the overall most highest genre?
- what is the most common theme in games that are subperb (the highest rating)?
  - what is the most common theme in games that are three highest ratings (good, great, subperb)?
  - what is the most common theme in games that are three lowest ratings ((bad, very bad , awful)
- Do users rate games with online multiplayer modes higher than games that lack online multiplayer modes?  

### Target variable?
  
  Our target variable is to be able to idetify the diffrent variables that make a videogame have a high rating 

### Need to haves (Deliverables):
- First what is needed:
  - Account Creation
In order to use our API, you must have a Twitch Account.
The IGDB.com API is free for non-commercial usage under the terms of the Twitch Developer Service Agreement.
For more information on how to aquire this information on : https://api-docs.igdb.com/#about

- Aquire.py 
- Prepare.py
- Env.py

### Nice to haves (With more time):




***

## <a name="dictionary"></a>Data Dictionary 

<details>
  <summary>Click to expand!</summary>

| **Age Rating**                                          |                                             | https://api.igdb.com/v4/age_ratings                                                       |
|---------------------------------------------------------|---------------------------------------------|-------------------------------------------------------------------------------------------|
| **field**                                               | **type**                                    | **description**                                                                           |
| category                                                | Category Enum                               | The organization that has issued a specific rating                                        |
| checksum                                                | uuid                                        | Hash of the object                                                                        |
| content_descriptions                                    | Array of Age Rating Content Description IDs |                                                                                           |
| rating                                                  | Rating Enum                                 | The title of an age rating                                                                |
| rating_cover_url                                        | String                                      | The url for the image of a age rating                                                     |
| synopsis                                                | String                                      | A free text motivating a rating                                                           |
| **Age Rating Enums - Category**                         |                                             |                                                                                           |
| **field**                                               | **type**                                    | **description**                                                                           |
| name                                                    | String                                      | The organization that has issued a specific rating                                        |
| value                                                   | Integer                                     | The rating organization ID                                                                |
| **Age Rating Enums - Rating**                           |                                             |                                                                                           |
| **field**                                               | **type**                                    | **description**                                                                           |
| name                                                    | String                                      | Rating of the rating of rating organization                                               |
| value                                                   | Integer                                     | Rating ID                                                                                 |
| **Age Rating Content Description**                      |                                             | https://api.igdb.com/v4/age_rating_content_descriptions                                   |
| **field**                                               | **Type**                                    | **description**                                                                           |
| category                                                | Category Enum                               |                                                                                           |
| checksum                                                | uuid                                        | Hash of the object                                                                        |
| description                                             | String                                      |                                                                                           |
| **Age Rating Content Description Enums - Category**     |                                             |                                                                                           |
| **field**                                               | **type**                                    | **description**                                                                           |
| name                                                    | String                                      | Name of the organization                                                                  |
| value                                                   | Integer                                     | Organization ID                                                                           |
| **Character**                                           |                                             | https://api.igdb.com/v4/characters                                                        |
| **field**                                               | **type**                                    | **description**                                                                           |
| akas                                                    | Array of Strings                            | Alternative names for a character                                                         |
| checksum                                                | uuid                                        | Hash of the object                                                                        |
| country_name                                            | String                                      | A characters country of origin                                                            |
| created_at                                              | Unix Time Stamp                             | Date this was initially added to the IGDB database                                        |
| description                                             | String                                      | A text describing a character                                                             |
| games                                                   | Array of Game IDs                           |                                                                                           |
| gender                                                  | Gender Enum                                 |                                                                                           |
| mug_shot                                                | Reference ID for Character Mug Shot         | An image depicting a character                                                            |
| name                                                    | String                                      |                                                                                           |
| slug                                                    | String                                      | A url-safe, unique, lower-case version of the name                                        |
| species                                                 | Species Enum                                |                                                                                           |
| updated_at                                              | Unix Time Stamp                             | The last date this entry was updated in the IGDB database                                 |
| url                                                     | String                                      | The website address (URL) of the item                                                     |
| **Character Enums - Gender**                            |                                             |                                                                                           |
| **field**                                               | **type**                                    | **description**                                                                           |
| name                                                    | String                                      | Gender of the Character                                                                   |
| value                                                   | Integer                                     | Gender ID of the Character                                                                |
| **Character Enums - Species**                           |                                             |                                                                                           |
| **field**                                               | **type**                                    | **description**                                                                           |
| name                                                    | String                                      | Species of the Character                                                                  |
| value                                                   | Integer                                     | Species ID of the Character                                                               |
| **Company**                                             |                                             | https://api.igdb.com/v4/companies                                                         |
| **field**                                               | **type**                                    | **description**                                                                           |
| change_date                                             | Unix Time Stamp                             | The data when a company got a new ID                                                      |
| change_date_category                                    | Change Date Category Enum                   |                                                                                           |
| changed_company_id                                      | Reference ID for Company                    | The new ID for a company that has gone through a merger or restructuring                  |
| checksum                                                | uuid                                        | Hash of the object                                                                        |
| country                                                 | Integer                                     | ISO 3166-1 country code                                                                   |
| created_at                                              | Unix Time Stamp                             | Date this was initially added to the IGDB database                                        |
| description                                             | String                                      | A free text description of a company                                                      |
| developed                                               | Array of Game IDs                           | An array of games that a company has developed                                            |
| logo                                                    | Reference ID for Company Logo               | The company’s logo                                                                        |
| name                                                    | String                                      |                                                                                           |
| parent                                                  | Reference ID for Company                    | A company with a controlling interest in a specific company                               |
| published                                               | Array of Game IDs                           | An array of games that a company has published                                            |
| slug                                                    | String                                      | A url-safe, unique, lower-case version of the name                                        |
| start_date                                              | Unix Time Stamp                             | The date a company was founded                                                            |
| start_date_category                                     | Start Date Category Enum                    |                                                                                           |
| updated_at                                              | Unix Time Stamp                             | The last date this entry was updated in the IGDB database                                 |
| url                                                     | String                                      | The website address (URL) of the item                                                     |
| websites                                                | Array of Company Website IDs                | The companies official websites                                                           |
| **Company Enums - change_date_category**                |                                             |                                                                                           |
| **field**                                               | **type**                                    | **description**                                                                           |
| name                                                    | String                                      | Format of date                                                                            |
| value                                                   | Integer                                     | ID of Date format                                                                         |
| **Company Enums - start_date_category**                 |                                             |                                                                                           |
| **field**                                               | **type**                                    | **description**                                                                           |
| name                                                    | String                                      | Format of date                                                                            |
| value                                                   | Integer                                     | ID of Date format                                                                         |
| **Collection**                                          |                                             | https://api.igdb.com/v4/collections                                                       |
| **field**                                               | **type**                                    | **description**                                                                           |
| checksum                                                | uuid                                        | Hash of the object                                                                        |
| created_at                                              | Unix Time Stamp                             | Date this was initially added to the IGDB database                                        |
| games                                                   | Array of Game IDs                           | The games that are associated with this collection                                        |
| name                                                    | String                                      | Umbrella term for a collection of games                                                   |
| slug                                                    | String                                      | A url-safe, unique, lower-case version of the name                                        |
| updated_at                                              | Unix Time Stamp                             | The last date this entry was updated in the IGDB database                                 |
| url                                                     | String                                      | The website address (URL) of the item                                                     |
| **External Game**                                       |                                             | https://api.igdb.com/v4/external_games                                                    |
| **field**                                               | **type**                                    | **description**                                                                           |
| category                                                | Category Enum                               | The id of the other service                                                               |
| checksum                                                | uuid                                        | Hash of the object                                                                        |
| countries                                               | Array of Integers                           | The ISO country code of the external game product.                                        |
| created_at                                              | Unix Time Stamp                             | Date this was initially added to the IGDB database                                        |
| game                                                    | Reference ID for Game                       | The IGDB ID of the game                                                                   |
| media                                                   | Media Enum                                  | The media of the external game.                                                           |
| name                                                    | String                                      | The name of the game according to the other service                                       |
| platform                                                | Reference ID for Platform                   | The platform of the external game product.                                                |
| uid                                                     | String                                      | The other services ID for this game                                                       |
| updated_at                                              | Unix Time Stamp                             | The last date this entry was updated in the IGDB database                                 |
| url                                                     | String                                      | The website address (URL) of the item                                                     |
| year                                                    | Integer                                     | The year in full (2018)                                                                   |
| **External Game Enums - Category**                      |                                             |                                                                                           |
| **field**                                               | **type**                                    | **description**                                                                           |
| name                                                    | String                                      | Name of online store                                                                      |
| value                                                   | Integer                                     | ID of the online store where game can be purchased                                        |
| **External Game Enums - Media**                         |                                             |                                                                                           |
| **field**                                               | **type**                                    | **description**                                                                           |
| name                                                    | String                                      | Media type                                                                                |
| value                                                   | Integer                                     | ID of media type                                                                          |
| Franchise                                               |                                             | https://api.igdb.com/v4/franchises                                                        |
| field                                                   | type                                        | description                                                                               |
| checksum                                                | uuid                                        | Hash of the object                                                                        |
| created_at                                              | Unix Time Stamp                             | Date this was initially added to the IGDB database                                        |
| games                                                   | Array of Game IDs                           | The games that are associated with this franchise                                         |
| name                                                    | String                                      | The name of the franchise                                                                 |
| slug                                                    | String                                      | A url-safe, unique, lower-case version of the name                                        |
| updated_at                                              | Unix Time Stamp                             | The last date this entry was updated in the IGDB database                                 |
| url                                                     | String                                      | The website address (URL) of the item                                                     |
| **Game**                                                |                                             | https://api.igdb.com/v4/games                                                             |
| **field**                                               | **type**                                    | **description**                                                                           |
| age_ratings                                             | Array of Age Rating IDs                     | The PEGI rating                                                                           |
| aggregated_rating                                       | Double                                      | Rating based on external critic scores                                                    |
| aggregated_rating_count                                 | Integer                                     | Number of external critic scores                                                          |
| alternative_names                                       | Array of Alternative Name IDs               | Alternative names for this game                                                           |
| artworks                                                | Array of Artwork IDs                        | Artworks of this game                                                                     |
| bundles                                                 | Array of Game IDs                           | The bundles this game is a part of                                                        |
| category                                                | Category Enum                               | The category of this game                                                                 |
| checksum                                                | uuid                                        | Hash of the object                                                                        |
| collection                                              | Reference ID for Collection                 | The series the game belongs to                                                            |
| cover                                                   | Reference ID for Cover                      | The cover of this game                                                                    |
| created_at                                              | Unix Time Stamp                             | Date this was initially added to the IGDB database                                        |
| dlcs                                                    | Array of Game IDs                           | DLCs for this game                                                                        |
| expanded_games                                          | Array of Game IDs                           | Expanded games of this game                                                               |
| expansions                                              | Array of Game IDs                           | Expansions of this game                                                                   |
| external_games                                          | Array of External Game IDs                  | External IDs this game has on other services                                              |
| first_release_date                                      | Unix Time Stamp                             | The first release date for this game                                                      |
| follows                                                 | Integer                                     | Number of people following a game                                                         |
| forks                                                   | Array of Game IDs                           | Forks of this game                                                                        |
| franchise                                               | Reference ID for Franchise                  | The main franchise                                                                        |
| franchises                                              | Array of Franchise IDs                      | Other franchises the game belongs to                                                      |
| game_engines                                            | Array of Game Engine IDs                    | The game engine used in this game                                                         |
| game_modes                                              | Array of Game Mode IDs                      | Modes of gameplay                                                                         |
| genres                                                  | Array of Genre IDs                          | Genres of the game                                                                        |
| hypes                                                   | Integer                                     | Number of follows a game gets before release                                              |
| involved_companies                                      | Array of Involved Company IDs               | Companies who developed this game                                                         |
| keywords                                                | Array of Keyword IDs                        | Associated keywords                                                                       |
| multiplayer_modes                                       | Array of Multiplayer Mode IDs               | Multiplayer modes for this game                                                           |
| name                                                    | String                                      |                                                                                           |
| parent_game                                             | Reference ID for Game                       | If a DLC, expansion or part of a bundle, this is the main game or bundle                  |
| platforms                                               | Array of Platform IDs                       | Platforms this game was released on                                                       |
| player_perspectives                                     | Array of Player Perspective IDs             | The main perspective of the player                                                        |
| ports                                                   | Array of Game IDs                           | Ports of this game                                                                        |
| rating                                                  | Double                                      | Average IGDB user rating                                                                  |
| rating_count                                            | Integer                                     | Total number of IGDB user ratings                                                         |
| release_dates                                           | Array of Release Date IDs                   | Release dates of this game                                                                |
| remakes                                                 | Array of Game IDs                           | Remakes of this game                                                                      |
| remasters                                               | Array of Game IDs                           | Remasters of this game                                                                    |
| screenshots                                             | Array of Screenshot IDs                     | Screenshots of this game                                                                  |
| similar_games                                           | Array of Game IDs                           | Similar games                                                                             |
| slug                                                    | String                                      | A url-safe, unique, lower-case version of the name                                        |
| standalone_expansions                                   | Array of Game IDs                           | Standalone expansions of this game                                                        |
| status                                                  | Status Enum                                 | The status of the games release                                                           |
| storyline                                               | String                                      | A short description of a games story                                                      |
| summary                                                 | String                                      | A description of the game                                                                 |
| tags                                                    | Array of Tag Numbers                        | Related entities in the IGDB API                                                          |
| themes                                                  | Array of Theme IDs                          | Themes of the game                                                                        |
| total_rating                                            | Double                                      | Average rating based on both IGDB user and external critic scores                         |
| total_rating_count                                      | Integer                                     | Total number of user and external critic scores                                           |
| updated_at                                              | Unix Time Stamp                             | The last date this entry was updated in the IGDB database                                 |
| url                                                     | String                                      | The website address (URL) of the item                                                     |
| version_parent                                          | Reference ID for Game                       | If a version, this is the main game                                                       |
| version_title                                           | String                                      | Title of this version (i.e Gold edition)                                                  |
| videos                                                  | Array of Game Video IDs                     | Videos of this game                                                                       |
| websites                                                | Array of Website IDs                        | Websites associated with this game                                                        |
| **Game Enums - Category**                               |                                             |                                                                                           |
| **field**                                               | **type**                                    | **description**                                                                           |
| name                                                    | String                                      | Type of game                                                                              |
| value                                                   | Integer                                     | ID of game type                                                                           |
| **Game Enums - Status**                                 |                                             |                                                                                           |
| **field**                                               | **type**                                    | **description**                                                                           |
| name                                                    | String                                      | Status of the game                                                                        |
| value                                                   | Integer                                     | ID of game status                                                                         |
| **Game Engine**                                         |                                             | https://api.igdb.com/v4/game_engines                                                      |
| **field**                                               | **Type**                                    | **description**                                                                           |
| checksum                                                | uuid                                        | Hash of the object                                                                        |
| companies                                               | Array of Company IDs                        | Companies who used this game engine                                                       |
| created_at                                              | Unix Time Stamp                             | Date this was initially added to the IGDB database                                        |
| description                                             | String                                      | Description of the game engine                                                            |
| logo                                                    | Reference ID for Game Engine Logo           | Logo of the game engine                                                                   |
| name                                                    | String                                      | Name of the game engine                                                                   |
| platforms                                               | Array of Platform IDs                       | Platforms this game engine was deployed on                                                |
| slug                                                    | String                                      | A url-safe, unique, lower-case version of the name                                        |
| updated_at                                              | Unix Time Stamp                             | The last date this entry was updated in the IGDB database                                 |
| url                                                     | String                                      | The website address (URL) of the item                                                     |
| **Game Mode**                                           |                                             | https://api.igdb.com/v4/game_modes                                                        |
| **field**                                               | **type**                                    | **description**                                                                           |
| checksum                                                | uuid                                        | Hash of the object                                                                        |
| created_at                                              | Unix Time Stamp                             | Date this was initially added to the IGDB database                                        |
| name                                                    | String                                      | The name of the game mode                                                                 |
| slug                                                    | String                                      | A url-safe, unique, lower-case version of the name                                        |
| updated_at                                              | Unix Time Stamp                             | The last date this entry was updated in the IGDB database                                 |
| url                                                     | String                                      | The website address (URL) of the item                                                     |
| **Game Version**                                        |                                             | https://api.igdb.com/v4/game_versions                                                     |
| **field**                                               | **type**                                    | **description**                                                                           |
| checksum                                                | uuid                                        | Hash of the object                                                                        |
| created_at                                              | Unix Time Stamp                             | Date this was initially added to the IGDB database                                        |
| features                                                | Array of Game Version Feature IDs           | Features and descriptions of what makes each version/edition different from the main game |
| game                                                    | Reference ID for Game                       | The game these versions/editions are of                                                   |
| games                                                   | Array of Game IDs                           | Game Versions and Editions                                                                |
| updated_at                                              | Unix Time Stamp                             | The last date this entry was updated in the IGDB database                                 |
| url                                                     | String                                      | The website address (URL) of the item                                                     |
| **Game Version Feature**                                |                                             | https://api.igdb.com/v4/game_version_features                                             |
| **field**                                               | **type**                                    | **description**                                                                           |
| category                                                | Category Enum                               | The category of the feature description                                                   |
| checksum                                                | uuid                                        | Hash of the object                                                                        |
| description                                             | String                                      | The description of the feature                                                            |
| position                                                | Integer                                     | Position of this feature in the list of features                                          |
| title                                                   | String                                      | The title of the feature                                                                  |
| values                                                  | Array of Game Version Feature Value IDs     | The bool/text value of the feature                                                        |
| **Game Version Feature Enums- Category**                |                                             |                                                                                           |
| **field**                                               | **type**                                    | **description**                                                                           |
| name                                                    | boolean                                     | The bool/text value of the feature                                                        |
| value                                                   | Integer                                     | The bool/text value of the feature                                                        |
| **Game Version Feature Value**                          |                                             | https://api.igdb.com/v4/game_version_feature_values                                       |
| **field**                                               | **type**                                    | **description**                                                                           |
| checksum                                                | uuid                                        | Hash of the object                                                                        |
| game                                                    | Reference ID for Game                       | The version/edition this value refers to                                                  |
| game_feature                                            | Reference ID for Game Version Feature       | The id of the game feature                                                                |
| included_feature                                        | Included Feature Enum                       | The boole value of this feature                                                           |
| note                                                    | String                                      | The text value of this feature                                                            |
| **Game Version Feature Value Enums - included_feature** |                                             |                                                                                           |
| **field**                                               | **type**                                    | **description**                                                                           |
| name                                                    | String                                      | How the feature is in the game                                                            |
| value                                                   | Integer                                     | ID of how the feature is included                                                         |
| **Involved Company**                                    |                                             | https://api.igdb.com/v4/involved_companies                                                |
| **field**                                               | **type**                                    | **description**                                                                           |
| checksum                                                | uuid                                        | Hash of the object                                                                        |
| company                                                 | Reference ID for Company                    |                                                                                           |
| created_at                                              | Unix Time Stamp                             | Date this was initially added to the IGDB database                                        |
| developer                                               | boolean                                     | If the game was developed by the company                                                  |
| game                                                    | Reference ID for Game                       |                                                                                           |
| porting                                                 | boolean                                     | If the game have any ports from the company                                               |
| publisher                                               | boolean                                     | If the game was published by the company                                                  |
| supporting                                              | boolean                                     | If the game was supported by the company                                                  |
| updated_at                                              | Unix Time Stamp                             | The last date this entry was updated in the IGDB database                                 |
| **Multiplayer Mode**                                    |                                             | https://api.igdb.com/v4/multiplayer_modes                                                 |
| **field**                                               | **type**                                    | **description**                                                                           |
| campaigncoop                                            | boolean                                     | True if the game supports campaign coop                                                   |
| checksum                                                | uuid                                        | Hash of the object                                                                        |
| dropin                                                  | boolean                                     | True if the game supports drop in/out multiplayer                                         |
| game                                                    | Reference ID for Game                       | The game this multiplayer mode is associated with                                         |
| lancoop                                                 | boolean                                     | True if the game supports LAN coop                                                        |
| offlinecoop                                             | boolean                                     | True if the game supports offline coop                                                    |
| offlinecoopmax                                          | Integer                                     | Maximum number of offline players in offline coop                                         |
| offlinemax                                              | Integer                                     | Maximum number of players in offline multiplayer                                          |
| onlinecoop                                              | boolean                                     | True if the game supports online coop                                                     |
| onlinecoopmax                                           | Integer                                     | Maximum number of online players in online coop                                           |
| onlinemax                                               | Integer                                     | Maximum number of players in online multiplayer                                           |
| platform                                                | Reference ID for Platform                   | The platform this multiplayer mode refers to                                              |
| splitscreen                                             | boolean                                     | True if the game supports split screen, offline multiplayer                               |
| splitscreenonline                                       | boolean                                     | True if the game supports split screen, online multiplayer                                |
| **Genre**                                               |                                             | https://api.igdb.com/v4/genres                                                            |
| **field**                                               | **type**                                    | **description**                                                                           |
| checksum                                                | uuid                                        | Hash of the object                                                                        |
| created_at                                              | Unix Time Stamp                             | Date this was initially added to the IGDB database                                        |
| name                                                    | String                                      |                                                                                           |
| slug                                                    | String                                      | A url-safe, unique, lower-case version of the name                                        |
| updated_at                                              | Unix Time Stamp                             | The last date this entry was updated in the IGDB database                                 |
| url                                                     | String                                      | The website address (URL) of the item                                                     |
| **Platform**                                            |                                             | https://api.igdb.com/v4/platforms                                                         |
| **field**                                               | **type**                                    | **description**                                                                           |
| abbreviation                                            | String                                      | An abbreviation of the platform name                                                      |
| alternative_name                                        | String                                      | An alternative name for the platform                                                      |
| category                                                | Category Enum                               | A physical or virtual category of the platform                                            |
| checksum                                                | uuid                                        | Hash of the object                                                                        |
| created_at                                              | Unix Time Stamp                             | Date this was initially added to the IGDB database                                        |
| generation                                              | Integer                                     | The generation of the platform                                                            |
| name                                                    | String                                      | The name of the platform                                                                  |
| platform_family                                         | Reference ID for Platform Family            | The family of platforms this one belongs to                                               |
| platform_logo                                           | Reference ID for Platform Logo              | The logo of the first Version of this platform                                            |
| slug                                                    | String                                      | A url-safe, unique, lower-case version of the name                                        |
| summary                                                 | String                                      | The summary of the first Version of this platform                                         |
| updated_at                                              | Unix Time Stamp                             | The last date this entry was updated in the IGDB database                                 |
| url                                                     | String                                      | The website address (URL) of the item                                                     |
| versions                                                | Array of Platform Version IDs               | Associated versions of this platform                                                      |
| websites                                                | Array of Platform Website IDs               | The main website                                                                          |
| **Platform Enums - Category**                           |                                             |                                                                                           |
| **field**                                               | **type**                                    | **description**                                                                           |
| name                                                    | String                                      | platform type                                                                             |
| value                                                   | Integer                                     | ID of platform type                                                                       |
| **Platform Family**                                     |                                             | https://api.igdb.com/v4/platform_families                                                 |
| **field**                                               | **type**                                    | **description**                                                                           |
| checksum                                                | uuid                                        | Hash of the object                                                                        |
| name                                                    | String                                      | The name of the platform family                                                           |
| slug                                                    | String                                      | A url-safe, unique, lower-case version of the name                                        |
| **Platform Version Release Date**                       |                                             | https://api.igdb.com/v4/platform_version_release_dates                                    |
| **field**                                               | **type**                                    | **description**                                                                           |
| category                                                | Category Enum                               | The format of the release date                                                            |
| checksum                                                | uuid                                        | Hash of the object                                                                        |
| created_at                                              | Unix Time Stamp                             | Date this was initially added to the IGDB database                                        |
| date                                                    | Unix Time Stamp                             | The release date                                                                          |
| human                                                   | String                                      | A human readable version of the release date                                              |
| m                                                       | Integer                                     | The month as an integer starting at 1 (January)                                           |
| platform_version                                        | Reference ID for Platform Version           | The platform this release date is for                                                     |
| region                                                  | Region Enum                                 | The region of the release                                                                 |
| updated_at                                              | Unix Time Stamp                             | The last date this entry was updated in the IGDB database                                 |
| y                                                       | Integer                                     | The year in full (2018)                                                                   |
| **Platform Version Release Date Enums - Category**      |                                             |                                                                                           |
| **field**                                               | **type**                                    | **description**                                                                           |
| name                                                    | String                                      | Format of release date                                                                    |
| value                                                   | Integer                                     | ID of format of release date                                                              |
| **Platform Version Release Date Enums - Region**        |                                             |                                                                                           |
| **field**                                               | **type**                                    | **description**                                                                           |
| name                                                    | String                                      | Name of region                                                                            |
| value                                                   | Integer                                     | ID of Region                                                                              |
| **Platform Version Company**                            |                                             | https://api.igdb.com/v4/platform_version_companies                                        |
| **field**                                               | **type**                                    | **description**                                                                           |
| checksum                                                | uuid                                        | Hash of the object                                                                        |
| comment                                                 | String                                      | Any notable comments about the developer                                                  |
| company                                                 | Reference ID for Company                    | The company responsible for developing this platform version                              |
| developer                                               | boolean                                     |                                                                                           |
| manufacturer                                            | boolean                                     |                                                                                           |
| **Release Date**                                        |                                             | https://api.igdb.com/v4/release_dates                                                     |
| **field**                                               | **type**                                    | **description**                                                                           |
| category                                                | Category Enum                               | The format category of the release date                                                   |
| checksum                                                | uuid                                        | Hash of the object                                                                        |
| created_at                                              | Unix Time Stamp                             | Date this was initially added to the IGDB database                                        |
| date                                                    | Unix Time Stamp                             | The date of the release                                                                   |
| game                                                    | Reference ID for Game                       |                                                                                           |
| human                                                   | String                                      | A human readable representation of the date                                               |
| m                                                       | Integer                                     | The month as an integer starting at 1 (January)                                           |
| platform                                                | Reference ID for Platform                   | The platform of the release                                                               |
| region                                                  | Region Enum                                 | The region of the release                                                                 |
| updated_at                                              | Unix Time Stamp                             | The last date this entry was updated in the IGDB database                                 |
| y                                                       | Integer                                     | The year in full (2018)                                                                   |
| **Release Date Enums - Category**                       |                                             |                                                                                           |
| **field**                                               | **type**                                    | **description**                                                                           |
| name                                                    | String                                      | Date format                                                                               |
| value                                                   | Integer                                     | ID of date format                                                                         |
| **Release Date Enums - Region**                         |                                             |                                                                                           |
| **field**                                               | **type**                                    | **description**                                                                           |
| name                                                    | String                                      | Name of region                                                                            |
| value                                                   | Integer                                     | ID of Region                                                                              |
| **Platform Version**                                    |                                             | https://api.igdb.com/v4/platform_versions                                                 |
| **field**                                               | **type**                                    | **description**                                                                           |
| checksum                                                | uuid                                        | Hash of the object                                                                        |
| companies                                               | Array of Platform Version Company IDs       | Who developed this platform version                                                       |
| connectivity                                            | String                                      | The network capabilities                                                                  |
| cpu                                                     | String                                      | The integrated control processing unit                                                    |
| graphics                                                | String                                      | The graphics chipset                                                                      |
| main_manufacturer                                       | Reference ID for Platform Version Company   | Who manufactured this version of the platform                                             |
| media                                                   | String                                      | The type of media this version accepted                                                   |
| memory                                                  | String                                      | How much memory there is                                                                  |
| name                                                    | String                                      | The name of the platform version                                                          |
| os                                                      | String                                      | The operating system installed on the platform version                                    |
| output                                                  | String                                      | The output video rate                                                                     |
| platform_logo                                           | Reference ID for Platform Logo              | The logo of this platform version                                                         |
| platform_version_release_dates                          | Array of Platform Version Release Date IDs  | When this platform was released                                                           |
| resolutions                                             | String                                      | The maximum resolution                                                                    |
| slug                                                    | String                                      | A url-safe, unique, lower-case version of the name                                        |
| sound                                                   | String                                      | The sound chipset                                                                         |
| storage                                                 | String                                      | How much storage there is                                                                 |
| summary                                                 | String                                      | A short summary                                                                           |
| url                                                     | String                                      | The website address (URL) of the item                                                     |
| **Player Perspective**                                  |                                             | https://api.igdb.com/v4/player_perspectives                                               |
| **field**                                               | **type**                                    | **description**                                                                           |
| checksum                                                | uuid                                        | Hash of the object                                                                        |
| created_at                                              | Unix Time Stamp                             | Date this was initially added to the IGDB database                                        |
| name                                                    | String                                      |                                                                                           |
| slug                                                    | String                                      | A url-safe, unique, lower-case version of the name                                        |
| updated_at                                              | Unix Time Stamp                             | The last date this entry was updated in the IGDB database                                 |
| url                                                     | String                                      | The website address (URL) of the item                                                     |
| **Theme**                                               |                                             | https://api.igdb.com/v4/themes                                                            |
| **field**                                               | **type**                                    | **description**                                                                           |
| checksum                                                | uuid                                        | Hash of the object                                                                        |
| created_at                                              | Unix Time Stamp                             | Date this was initially added to the IGDB database                                        |
| name                                                    | String                                      |                                                                                           |
| slug                                                    | String                                      | A url-safe, unique, lower-case version of the name                                        |
| updated_at                                              | Unix Time Stamp                             | The last date this entry was updated in the IGDB database                                 |
| url                                                     | String                                      | The website address (URL) of the item                                                     |
</details>

***

## <a name="wrangle"></a>Data Acquisition and Preparation
[[Back to top](#top)]

![]()
Account Creation
- The first step is to sign in or sign up for a free <a href="https://dev.twitch.tv/login" target="_blank">Twitch</a>.
- Ensure you have Two Factor Authentication <a href="https://www.twitch.tv/settings/security" target="_blank">enabled</a>.
- <a href="https://dev.twitch.tv/console/apps/create" target="_blank">Register</a> your application
- <a href="https://dev.twitch.tv/console/apps" target="_blank">Manage</a> your newly created application
- Generate a Client Secret by pressing [New Secret]
- Take note of the Client ID and Client Secret

Create env.py and .gitignore
  - In env.py have a the following lines of code:
    ```python
        Client_ID = "Your_uniqe_Client_ID"

        Client_Secret = "Your_unique_Client_Secret"

        def get_db_url():
            return f'https://id.twitch.tv/oauth2/token?client_id={Client_ID}&client_secret={Client_Secret}&grant_type=client_credentials'
    ```
  - Make sure your newly genreated Client ID and Client Secret are in a string and save the file.

  - Create a .gitignore just in case not cloning our repo to exclude env.py , *.json files.

Acquire.py
  - Import these libraries:
    ```python
        import requests
        import env
        import os
        import pandas as pd
        import json
        from env import Client_ID
        from igdb.wrapper import IGDBWrapper
        import time
    ```

  - Create a function that will connect to the API and retrives the access token with similar code:
    ```python
        def connect_api():
          url = env.get_db_url()
          response = requests.post(url)
          data = response.json()
          access_token = data['access_token']
          return access_token

        access_token = connect_api()
    ```
  - Create function that will imput your Client ID and access token into a wrapper object:
  ```python
      def run_wrapper():
      wrapper = IGDBWrapper(f'{Client_ID}', f'{access_token}')
      return wrapper
    
      wrapper = run_wrapper()
  ```
  The purpose of the wrapper object is to return data acquired from API into a json object.

  - Create functions to go to each <a href="https://api-docs.igdb.com/#endpoints" target="_blank">endpoint</a> of the API. An example is  ``` get_game_library(wrapper) ```
    ```python
      def get_game_library(wrapper):
      game_library = pd.DataFrame()
      for i in range (0, 500):
          games = wrapper.api_request('games', 'fields *; limit 500;' f'offset {i * 500};')
          y = json.loads(games)
          results_df =pd.DataFrame(y)
          game_library = pd.concat([game_library, results_df])
          time.sleep(1.0)
      return game_library
    ```

  - The API has some data that is feed into endpoints from reference tables that are not included. An example is in the <a href="https://api-docs.igdb.com/#age-rating" target="_blank">Age Rating endpoint</a>, the column `category ` uses data from Age Ratings Enumns <a href="https://api-docs.igdb.com/#age-rating-enums" target="_blank">category</a> table to fill in the column.

  A spreadsheet workbook will need to be created. To save time from creating the workbook, a .xlsx file was uploaded to the repo. The function used to acquire the data tables that are not included in the API is:

  ```python
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

  ```
  - Save acquire.py

- Prepare.py

  - Import these libraries:
  ```python
    import env
    import pandas as pd
    import json
    from env import Client_ID
    from igdb.wrapper import IGDBWrapper
    import time
    import acquire
    import numpy as np
    import seaborn as sns
  ```
  - Create a function that will import json object into notebook if json object is already saved in /data folder into a dictionary. If json not availble, fuction will acquire data from API endpoint and save as .json
  ```python
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
  ```
  - Create dictionary object that will have a keyword assoiated with a path and a function in the acquire.py 

  ```python
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
  ```
  - Create a function that retrive all tables from the config dict
  ```python
      def get_tables():
          tables = {}
          for key, value in config.items():
              tables[key] = import_table(value)
              # print(f'Completed import for {key}')
          return tables
  ```
  -  Create a function that will create new columns for list objects in a field
  ```python
      def my_list(column, word):
        if word in column:
            return 1
        else:
            return 0
  ```
  - Run the `get_tables()`
  - Create  variable `to_keep` with a list object of columns to keep
  - Add a pointer to the game library dictionary object
    ```python 
        game_library = tables['game_library']
    ```
  - Trim down to only columns we care about
    ```python
        game_library = game_library[to_keep].copy()
    ```
  - Convert `game_library['first_release_date']` to datatime object
  - Add multiplayer_modes to game_library from the multiplayer_modes endpoint
    ```python
        tables['multi_player_modes'].rename(columns={'id': 'multi_player_mode_id'}, inplace=True)
    # dataframe merging game_library and multi_player_modes with left join. 
    game_library = pd.merge(
            game_library, tables['multi_player_modes'], how='left', left_on = 'id', right_on = 'game'
            ).drop(columns=[ 'game', 
                            'checksum', 
                            'multi_player_mode_id', 
                            'platform'
                            ])
    ```
  - Fill in null values and drop `multiplayer_modes`
    ```python
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
    ```
  - Make a dictionary for id and string to convert id to the nomenclature. Afterwards make new columns for each genre.
    ```python
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
    ```
  - above code block was utilized to transform columns `game_modes`, `player_perspectives`, `themes`, and `platforms`.
  - Modified the `dlcs` column to a bootlean column with the following code:
    ```python
        # Modified DLC column
    game_library['dlcs'] = game_library['dlcs'].fillna(0)

    def dlcs_col(df):
        game_library['has_dlcs'] = np.where(game_library.dlcs != 0, 1, 0)  
        return df
    game_library = dlcs_col(game_library)
    ```
  - The `ratings` column was used to create a new column `rating_bin` which contained the rating scale nomenclature.
    ```python
        game_library['rating_bin'] = pd.cut(game_library.rating, 
                           bins = [0,10,20, 30, 40, 50, 60, 70, 80, 90, 100],
                           labels = ['awful','very_bad','bad','unimpressive','average','fair','alright','good','great', 'subperb'])
    ```
  - Create a variable `cols_to_drop` with the list object containing 
        ```python
        'dlcs',
        'game_modes',
        'offlinemax' ,
        'offlinecoopmax',
        'onlinecoopmax',
        'onlinemax',
        'rating',
        'age_ratings' 
        ```
  - Modify `game_libray` with the following:
    ```python
        game_library = game_library.drop(columns=cols_to_drop)
    ```
  - Create a function that will convert all True and False values as 0 and 1. Apply the fuction to `game_library`
    ```python
        def replace_booleans(data):
        for col in data:
            data[col].replace(True, 1, inplace=True)
            data[col].replace(False, 0, inplace=True)

        replace_booleans(game_library)
    ```
  - Create two data frames. One with valid observations in `rating_bin`, and another with null values in 'rating_bin'.
    ```python
        game_ratings = game_library[game_library['rating_bin'].notnull()]
        not_rated = game_library[game_library['rating_bin'].isnull()]
    ```
  - Create a function with all the above code tasks into a function `wrangle_data()` that returns `game_library` , `game_ratings` , `not_rated`
    ```python
        game_library , game_ratings , not_rated = wrangle_data()
    ```
  - Split `game_ratings` into three data samples: train, validate, and test. Create variables `X_train` , `y_train` , `X_validate` , `y_validate` , `X_test`, and `y_test`.
    ```python
        def split(game_ratings, stratify_by='rating_bin'):
          # split df into train_validate 
          train_validate, test = train_test_split(game_ratings, test_size=.20, random_state=13)
          train, validate = train_test_split(train_validate, test_size=.3, random_state=13)
          X_train = train.drop(columns=['rating_bin'])
          y_train = train[['rating_bin']]

          X_validate = validate.drop(columns=['rating_bin'])
          y_validate = validate[['rating_bin']]

          X_test = test.drop(columns=['rating_bin'])
          y_test = test[['rating_bin']]

          return train, X_train, X_validate, X_test, y_train, y_validate, y_test
    ```
  
*********************

## <a name="explore"></a>Data Exploration:
[[Back to top](#top)]
- Python files used for exploration:
    - aquire.py 
    - prepare.py
    


### Takeaways from exploration:
_Question 1 - Do video games on certain platforms get superb user ratings?_

          - the most common platforms are `PC(microsoft Windows)`, `Play Station 4`, `X-Box one`, `Nintendo Switch`
 
  Sub Question 1.1 - What about the three lowest ratings (bad, very bad, awful)?  
  
          - PC (Microsoft Windows)
          - MAC
          - Nintendo Switch
    
_Question 2 - what is the most common genre in games that are superb?¶_

          - the most common platforms are `Indie`, `Adventure`, `Role-Playing-RPG`, `Shooter`
 
   Sub Question 2.1 - What about the three lowest ratings (bad, very bad, awful)?
      
      
         - Indie 
         - adventure
         - simulator
         - indie  


_Question 3 - What is the most common theme in games that are subperb (the highest rating)_ 

         - the most common themes in the subperb is action, fantasy, science fiction, Open World.
    
  Question 3.1 - what is the most common theme in games that are three lowest ratings ((bad, very bad , awful))?
  
          - the most common game these in the lowest ratings Action, Science fiction, Horror, Fantasy 
***

## <a name="model"></a>Modeling:
[[Back to top](#top)]

### Model Preparation: 
- Before modeling we had to drop addition columns and used Chi-Squared test for feature selection on the split data. We also made datframes to hold the models predictions.

### Baseline
    
- Baseline Results: Mode of rating class "Alright" for a baseline of 0.28
    

- Chi-Squared selected features:
    - features = ['offlinemax', 'onlinecoop', 'onlinemax', 'shooter', 'indie', 'PC (Microsoft Windows)', 'PlayStation3', 'Xbox360', 'iOS', 'PlayStation4', 'Xbox one', 'Science Fiction', 'Fantasy', 'Historical', 'Stealth', 'Comedy', 'Open world', 'Third person', 'Bird view / Isometric', 'Side view']

***

### Models:
- Will run the following classification models:
  - Random Forest
  - Decision Tree
  - Logistic Regression
  - One Vs. Rest Classifier
  - K-Nearest Neighbor

    

- For the models it was important that features of games (player perspective, genres, themes, ect.) be turned into their own binary columns, as well as converting any boolean columns. Doing this will greatly help the models predictions.
    
    
#### Model 1: Random Forest

- Train data RF best perforance: max depth of 27 and accuracy of 0.66
- Validate data RF best perforance: max depth 15 had accuracy of 0.37

### Model 2 : Decision Tree

- Train data DT best perforance: max depth of 29 and accuracy of 0.63
- Validate data DT best perforance: max depth 9 had accuracy of 0.38

### Model 3 : Logistic Regression

- Train data LR best perforance: 0.34
- Validate data LR best perforance: 0.34

### Model 4: One Vs. Rest

- Train data LR best perforance: 0.34
- Validate data LR best perforance: 0.34

### Model 5: KNN

- Train data KNN best perforance: max depth of 1 with an accuracy of 0.60
- Validate data KNN best perforance: max depth of 23 with an accuracy of 0.34


## Selecting the Best Model: 
  - The best performing model was Random Forest with a max depth of 15 on validate. That will be the model used on test data.

### Use Table below as a template for all Modeling results for easy comparison:

| Model | Validation/Out of Sample accuracy | 
| ---- | ----| 
| Baseline | 0.284647 | 
| Random Forest (RF) | 0.369651 |   
| Decision Tree (DT) | 0.346415	 |  
| Logistic Regression (LR) | 0.344007|  
| K-Nearest Neighbor (KNN) | 0.344148	 |   
| One Vs. Rest | 0.356869 | 

- {Random Forest} model performed the best


## Testing the Model

- Model Testing Results
  - All the models beat baseline on train, validate and test. We trained all of the models in two rounds; the first using Chi-Squared feature selection and the second without using it. All of the models preformed marginally better when trained with with all of the features we created in our dataset. Random Forest preformed the best on validate both with the feature selection and without. We ran it on the test data set and beat baseline with an accuracy of 0.388625
***

## <a name="conclusion"></a>Conclusion:

- After acquiring data from the IGDB API we were able to build five classification models that were trained on games with ratings, and all were able to beat the baseline. We used the model with the highest accuracy, Random Forest, to predict what class games without ratings would have based on their features. Having this insight will greatly improve any video games that will be made in the feature in regards to user ratings.


## Next Steps: 

- Next we would like to acquire more features from other API's like critic ratings and play through length to merge into the game_library dataframe, and giving the models even better accuracy.
- Exploring games with low ratings to see what features contribute to low performance for game reviews.
- Use NLP on reviews to better understand user/critic tone.
- Use regression models to predict numeric ratings.

[[Back to top](#top)]

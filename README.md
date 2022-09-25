

# <a name="top"></a>Videogame-Capstone
![]()
Kalpana Cohort 2022

by: Lindy Castellaw, Glady Barrios, Jarrid Jones 

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


***
[[Project Description](#project_description)]
[[Project Planning](#planning)]
[[Key Findings](#findings)]
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

### Nice to haves (With more time):



***

## <a name="findings"></a>Key Findings:
[[Back to top](#top)]




***

## <a name="dictionary"></a>Data Dictionary  
[[Back to top](#top)]

### Data Used
---
| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

***

## <a name="wrangle"></a>Data Acquisition and Preparation
[[Back to top](#top)]

![]()


### Wrangle steps: 


*********************

## <a name="explore"></a>Data Exploration:
[[Back to top](#top)]
- Python files used for exploration:
    - aquire.py 
    - prepare.py
    


### Takeaways from exploration:
Question 1 - Do video games on certain platforms get better user ratings?
  - Yes it looks like for the games in the three highest member ratings (good, great,subperb) the majority of those games are played on
      - PC(microsoft Windows)
      - MAC
      - X-Box 360
      - ps 3 and 4
      
Question 2 - what is the most common genre in games that are subperb (the highest rating)¶
 - the most common Genre in the higest rating are adventure, role-playing- rpg, shoter, rts, racing
 Question 2.1 - what about the three highest ratings (good, great, subperb) ? what is the overall most highest genre
  - The higest raed genres are adventure, shooter, strategy, role-playing-rpg
 Quesuestion 2.2 - what about the three lowest ratings ((bad, very bad , awful)) ? what is the overall most highest genre in these low rating games?
  - The three lowest ratings are shooter, simulator, strategy, racing, arcade 

Question 3 - What is the most common theme in games that are subperb (the highest rating) 
  - the most common themes in the subperb is action, fantasy, science fiction, historical.
  Question 3.1 - what is the most common theme in games that are three highest ratings (good, great, subperb)?
    - the most themes in the three higest ratings are action, science fiction, Comedy
  Question 3.2 - what is the most common theme in games that are three lowest ratings ((bad, very bad , awful))?
    - the most common game these in the lowest ratings Action, Non-fiction, Science fiction and Not avalible 
***

## <a name="model"></a>Modeling:
[[Back to top](#top)]

### Model Preparation:

### Baseline
    
- Baseline Results: 
    

- Selected features to input into models:
    - features = []

***

### Models and R<sup>2</sup> Values:
- Will run the following regression models:

    

- Other indicators of model performance with breif defiition and why it's important:

    
    
#### Model 1: Linear Regression (OLS)


- Model 1 results:



### Model 2 : Lasso Lars Model


- Model 2 results:


### Model 3 : Tweedie Regressor (GLM)

- Model 3 results:


### Model 4: Quadratic Regression Model

- Model 4 results:


## Selecting the Best Model:

### Use Table below as a template for all Modeling results for easy comparison:

| Model | Validation/Out of Sample RMSE | R<sup>2</sup> Value |
| ---- | ----| ---- |
| Baseline | 0.167366 | 2.2204 x 10<sup>-16</sup> |
| Linear Regression (OLS) | 0.166731 | 2.1433 x 10<sup>-3</sup> |  
| Tweedie Regressor (GLM) | 0.155186 | 9.4673 x 10<sup>-4</sup>|  
| Lasso Lars | 0.166731 | 2.2204 x 10<sup>-16</sup> |  
| Quadratic Regression | 0.027786 | 2.4659 x 10<sup>-3</sup> |  


- {} model performed the best


## Testing the Model

- Model Testing Results

***

## <a name="conclusion"></a>Conclusion:
[[Back to top](#top)]


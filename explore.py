import requests
from requests.models import Request, Response
import pandas as pd
from igdb.igdbapi_pb2 import GameResult
from typing import Dict, List, Optional, Union, cast
import acquire
import json
from igdb.wrapper import IGDBWrapper
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from prepare import wrangle_data
import plotly.graph_objects as go
import env
from env import Client_ID
import time
import numpy as np
import os




def train_validate_test_split(df):
    '''
    This function performs split on game_ratings data, stratify rating_bin.
    Returns train, validate, and test dfs.
    '''
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=13, stratify=df.rating_bin)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=13,  stratify=train_validate.rating_bin)

    return train, validate, test

def to_1D(series):
    return pd.Series([x for _list in series for x in _list])


def platforms_bar():
    colors = ['purple',] * 5


    fig = go.Figure(data=[go.Bar(
        x=['PC (Microsoft Windows)', 'PlayStation4' , 'MAC' , 'Xbox One'],
        y=[121, 63, 44,  41],
        marker_color=colors # marker color can be a single color value or an iterable
    )])
    fig.update_layout(title_text='Platforms', font=dict(size=17, color="black"))
    fig.show()

def platforms_low(df):
    fig, ax = plt.subplots(figsize = (14,4))
    ax.bar(to_1D(df["platforms"]).value_counts().iloc[:4].index,
        to_1D(df["platforms"]).value_counts().iloc[:4].values)
    ax.set_ylabel("Frequency", size = 12)
    ax.set_title("platforms", size = 14)

def genres_bar():
    colors = ['purple',] * 5
    fig = go.Figure(data=[go.Bar(
        x=['Adventure', 'Role-Playing-RPG' , 'Indie' , 'Strategy'],
        y=[104, 75, 48,  41],
        marker_color=colors # marker color can be a single color value or an iterable
    )])
    fig.update_layout(title_text='Genre', font=dict(size=17, color="black"))
    fig.show()

def genres_low(df):
    fig, ax = plt.subplots(figsize = (14,4))
    ax.bar(to_1D(df["genres"]).value_counts().iloc[:4].index,
            to_1D(df["genres"]).value_counts().iloc[:4].values)
    ax.set_ylabel("Frequency", size = 12)
    ax.set_title("genre", size = 14)

def theme_bar():
    colors = ['purple',] * 5
    fig = go.Figure(data=[go.Bar(
        x=['Action', 'Fantasy', 'Science-Fiction', 'Open-World'],
        y=[107,  66,  36,  28],
        marker_color=colors # marker color can be a single color value or an iterable
    )])
    fig.update_layout(title_text='Themes', font=dict(size=17, color="black"))
    fig.show()

def theme_low(df):
    fig, ax = plt.subplots(figsize = (14,4))
    ax.bar(to_1D(df["themes"]).value_counts().iloc[:4].index,
        to_1D(df["themes"]).value_counts().iloc[:4].values)
    ax.set_ylabel("Frequency", size = 12)
    ax.set_title("Themes", size = 14)

def player_bar():
    colors = ['purple',] * 5
    fig = go.Figure(data=[go.Bar(
        x=['Third-Person', 'Bird-view / Isometric', 'Side-View','First-Person'],
        y=[285, 226, 218,  11],
        marker_color=colors # marker color can be a single color value or an iterable
    )])
    fig.update_layout(title_text='Player Perspectives',  font=dict(size=17, color="black")) 
    fig.show()


def player_low(df):
    fig, ax = plt.subplots(figsize = (14,6))
    ax.bar(to_1D(df["player_perspectives"]).value_counts().iloc[:4].index,
        to_1D(df["player_perspectives"]).value_counts().iloc[:4].values)

    ax.set_ylabel("Frequency", size = 20)
    ax.set_title("Player Perspective")

    plt.xticks(fontsize = 15)

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd


df_game = pd.read_csv('C:/Users/hansf/Documents/ADS_2020/DataWrangling/Pandas_MovieDF/game.csv')

df_game

df_game[(df_game['team1']=="NED" )| (df_game['team2']=="NED" )]
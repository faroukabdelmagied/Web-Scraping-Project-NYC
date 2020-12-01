## Importing libraries:
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
plt.style.use('ggplot')
from scipy.stats import pearsonr

## Loading the Data frame:
df = pd.read_csv("Rocket_Data.csv")

## Checking the structure of the data:
# print(df.head(10))
# print(df.columns.tolist())


## Removing commas from the included data:
df = df.replace(',','', regex = True)

## Converting string coloumns into numeric: Integer:

## Coloumn names: ['Assists', 'Goal_Shot_Ratio', 'Goals', 'MVPs', 'Player_name', 'Rank', 'Saves', 'Shots', 'TRN_Score', 'Wins']
df['Assists'] = pd.to_numeric(df['Assists'], errors='coerce')
df['Goal_Shot_Ratio'] = pd.to_numeric(df['Goal_Shot_Ratio'], errors='coerce')
df['Goals'] = pd.to_numeric(df['Goals'], errors='coerce')
df['MVPs'] = pd.to_numeric(df['MVPs'], errors='coerce')
df['Rank'] = pd.to_numeric(df['Rank'], errors='coerce')
df['Saves'] = pd.to_numeric(df['Saves'], errors='coerce')
df['Shots'] = pd.to_numeric(df['Shots'], errors='coerce')
df['TRN_Score'] = pd.to_numeric(df['TRN_Score'], errors='coerce')
df['Wins'] = pd.to_numeric(df['Wins'], errors='coerce')

#######################################################
#######################################################


####################################################### Rankings vs Goals ######################################################

#Figure 1:
Figure_1 = plt.scatter(df['Goals'],df['Rank'], color = "#5ee3ff")
plt.title('Goals Scored vs Player Rank')
plt.xlabel('Goals Scored')
plt.ylabel('Player Rank')
plt.show()

#Covariance:
Covariance_1 = np.cov(df['Goals'], df['Rank'])
print(Covariance_1[0][1])

#Personscorr:
Personscorr_1 = pearsonr(df['Goals'], df['Rank'])
print(Personscorr_1[0])

#######################################################
#######################################################


####################################################### Rankings vs Assists ######################################################

#Figure 2:
Figure_2 = plt.scatter(df['Assists'], df['Rank'], color = "#5ee3ff")
plt.title('Assists vs Player Rank')
plt.xlabel('Assists')
plt.ylabel('Player Rank')
plt.show()

#Covariance:
Covariance_2 = np.cov(df['Assists'], df['Rank'])
print(Covariance_2[0][1])

#Personscorr:
Personscorr_2 = pearsonr(df['Assists'], df['Rank'])
print(Personscorr_2[0])

#######################################################
#######################################################


####################################################### Rankings vs MVPs ######################################################

#Figure 3:
Figure_3 = plt.scatter(df['MVPs'], df['Rank'], color = "#5ee3ff")
plt.title('MVPs vs Players Rank')
plt.xlabel('MVPs')
plt.ylabel('Players Rank')
plt.show()

#Covariance:
Covariance_3 = np.cov(df['MVPs'], df['Rank'])
print(Covariance_3[0][1])

#Personscorr:
Personscorr_3 = pearsonr(df['MVPs'], df['Rank'])
print(Personscorr_3[0])

#######################################################
#######################################################


####################################################### Rankings vs GoalShotRatio ######################################################

#Figure 4:
Figure_4 = plt.scatter(df['Goal_Shot_Ratio'], df['Rank'], color = "#5ee3ff" )
plt.title('Goal/Shot Ratio vs Players Rank')
plt.xlabel('Goal/Shot Ratio')
plt.ylabel('Players Rank')
plt.show()

#Covariance:
Covariance_4 = np.cov(df['Goal_Shot_Ratio'], df['Rank'])
print(Covariance_4[0][1])

#Personscorr:
Personscorr_4 = pearsonr(df['Goal_Shot_Ratio'], df['Rank'])
print(Personscorr_4[0])

#######################################################
#######################################################


####################################################### Rankings vs Shots ######################################################

#Figure 5:
Figure_5 = plt.scatter(df['Shots'], df['Rank'], color = "#5ee3ff" )
plt.title('Shots vs Players Rank')
plt.xlabel('Shots')
plt.ylabel('Players Rank')
plt.show()

#Covariance:
Covariance_5 = np.cov(df['Shots'], df['Rank'])
print(Covariance_5[0][1])

#Personscorr:
Personscorr_5 = pearsonr(df['Shots'], df['Rank'])
print(Personscorr_5[0])

#######################################################
#######################################################


####################################################### Rankings vs Wins ######################################################

#Figure 6:
Figure_6 = plt.scatter(df['Wins'], df['Rank'], color = "#5ee3ff")
plt.title('Wins vs Players Rank')
plt.xlabel('Wins')
plt.ylabel('Players Rank')
plt.show()

#Covariance:
Covariance_6 = np.cov(df['Wins'], df['Rank'])
print(Covariance_6[0][1])

#Personscorr:
Personscorr_6 = pearsonr(df['Wins'], df['Rank'])
print(Personscorr_6[0])

#######################################################
#######################################################


####################################################### Saves vs Rank ######################################################
#Figure 7:
Figure_7 = plt.scatter(df['Saves'], df['Rank'], color = "#5ee3ff")
plt.title('Saves vs Players Rank')
plt.xlabel('Saves')
plt.ylabel('Players Rank')
plt.show()

#Covariance:
Covariance_7 = np.cov(df['Saves'], df['Rank'])
print(Covariance_7[0][1])

#Personscorr:
Personscorr_7 = pearsonr(df['Saves'], df['Rank'])
print(Personscorr_7[0])

#######################################################
#######################################################


####################################################### Shots vs Goals ######################################################
#Figure 8:
Goals_Shots = df[['Goals', 'Shots']]
Goals_Shots = Goals_Shots.loc[Goals_Shots.apply(lambda x: np.abs(x - x.mean()) / x.std() < 3).all(axis=1)]
Figure_8 = plt.scatter(Goals_Shots['Shots'], Goals_Shots['Goals'])
plt.title('Shots Taken vs Goals Scored')
plt.xlabel('Shots Taken')
plt.ylabel('Goals scored')
plt.show()

#Covariance:
Covariance_8 = np.cov(Goals_Shots['Shots'], Goals_Shots['Goals'])
print(Covariance_8[0][1])

#Personscorr:
Personscorr_8 = pearsonr(Goals_Shots['Shots'], Goals_Shots['Goals'])
print(Personscorr_8[0])

#######################################################
#######################################################


####################################################### Goals vs Wins ######################################################
#Figure 9:
Goals_Wins = df[['Goals','Wins']]
## Removing the outliers
Goals_Wins = Goals_Wins.loc[Goals_Wins.apply(lambda x: np.abs(x - x.mean()) / x.std() < 3).all(axis=1)]

Figure_9 = plt.scatter(Goals_Wins['Goals'], Goals_Wins['Wins'])
plt.title('Goals vs Wins')
plt.xlabel('Goals Scored')
plt.ylabel('Wins')
plt.show()

#Covariance:
Covariance_9 = np.cov(Goals_Wins['Goals'], Goals_Wins['Wins'])
print(Covariance_9[0][1])

#Personscorr:
Personscorr_9 = pearsonr(Goals_Wins['Goals'], Goals_Wins['Wins'])
print(Personscorr_9[0])

#######################################################
#######################################################


####################################################### Saves vs Wins ######################################################
#Figure 10:
Saves_Wins = df[['Saves', 'Wins']]
## Removing the outliers from the Saves_Wins Data Frame:
Saves_Wins = Saves_Wins.loc[Saves_Wins.apply(lambda x: np.abs(x - x.mean()) / x.std() < 3).all(axis=1)]

Figure_10 = plt.scatter(Saves_Wins['Saves'], Saves_Wins['Wins'])
plt.title('Saves vs Wins')
plt.xlabel('Saves')
plt.ylabel('Wins')
plt.show()

#Covariance:
Covariance_10 = np.cov(Saves_Wins['Saves'], Saves_Wins['Wins'])
print(Covariance_10[0][1])

#Personscorr:
Personscorr_10 = pearsonr(Saves_Wins['Saves'], Saves_Wins['Wins'])
print(Personscorr_10[0])


#### Selecting the top 1% of the data:
n = 1
New_df = df.head(int(len(df)*(n/100)))
print(New_df['MVPs'].describe())


# Mean Wins:
Figure_11 = plt.hist(New_df['Wins'], bins = 15, color = "#666699")
plt.title('Wins')
plt.xlabel('Wins')
plt.ylabel('Frequency')
plt.show()

## Mean Goals:
Figure_12 = plt.hist(New_df['Goals'], bins = 15, color = "#666699")
plt.title('Goals')
plt.xlabel('Goals')
plt.ylabel('Frequency')
plt.show()

# Mean Saves:
Figure_13 = plt.hist(New_df['Saves'], bins = 15, color = "#666699")
plt.title('Saves')
plt.xlabel('Saves')
plt.ylabel('Frequency')
plt.show()

## Mean Assists:
Figure_14 = plt.hist(New_df['Assists'], bins = 15, color = "#666699")
plt.title('Assists')
plt.xlabel('Assists')
plt.ylabel('Frequency')
plt.show()

# ## Mean MVPS:
Figure_15 = plt.hist(New_df['MVPs'], bins = 15, color = "#666699")
plt.title('MVPs')
plt.xlabel('MVPs')
plt.ylabel('Frequency')
plt.show()

## Mean Shots:
Figure_16 = plt.hist(New_df['Shots'], bins = 15, color = "#666699")
plt.title('Shots')
plt.xlabel('Shots')
plt.ylabel('Frequency')
plt.show()


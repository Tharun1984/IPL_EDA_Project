import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
df=pd.read_csv("matches.csv")
print(df.head())
print(df.tail())
print(df.shape)
print(df.info()) 
print(df.describe())
print(df.isnull().sum()) 
df["city"]=df["city"].fillna(df["city"].mode()[0])
df["winner"]=df["winner"].fillna(df["winner"].mode()[0])
df["player_of_match"]=df["player_of_match"].fillna(df["player_of_match"].mode()[0])
df["umpire1"]=df["umpire1"].fillna(df["umpire1"].mode()[0])
df["umpire2"]=df["umpire2"].fillna(df["umpire2"].mode()[0])
df.drop("umpire3",axis=1,inplace=True)
print(df.isnull().sum()) 
sns.countplot(x="Season",data=df)
plt.title("Matches Played bY Each Season")
plt.show() # IPL 2011,2012 and 2013 had the highest number of matches compared to previus seasons because of expansion of new teams and post 2013,matches stabilished around 60 per season
sns.countplot(x="venue",data=df) 
plt.xticks(rotation=90) 
plt.title("Matches Played in Each venue")
plt.show() #Eden garden has the most number of match played compare to other venue ,followed by wankhede and chinnaswamy stadium.most international venue hosted very few matches.
sns.histplot(df["win_by_runs"],kde=True,bins=30)
plt.title("Distribution of Win by Runs")
plt.show()  # Most of the ipl matches are won around(0-25),showing T20 are closely contested.Wins above 100 runs are very rare.
sns.histplot(x="win_by_wickets",data=df)
plt.title("Distribution of Win by wickets")
plt.show()  # Most of the ipl matches are won by 2-8 wickets depending on the target set by batting team.Win by 10 wickets are very rare.
sns.boxplot(y="win_by_runs",data=df)
plt.title("Spread of Win by Runs")
plt.show() # Median win margin is around 15 runs,meaning most matches are closely contested.The box has small IQR,but many outliers above 80-140 runs nshows that one sided matches do continously occur.
sns.barplot(x="city",y="win_by_runs",data=df)
plt.xticks(rotation=90)
plt.title("Average Win by Runs across cities")
plt.show() # Dharamsala has the highest average win by runs followed by Port Elizabeth and East London.Most international Venue has fewer match.Indian cities dominate the chart as Ipl is primarlily hosted in India
sns.countplot(x="umpire1",hue="team1",data=df)
plt.xticks(rotation=90)
plt.title("Matches officiated by umpires for Teams")
plt.show()  # Dharmasena and S.Ravi has the highest number of matches across teams,making them the most frequently assigned umpires in IPL
sns.boxplot(x="dl_applied",y="win_by_runs",data=df)
plt.title("DL Method Impact on win by runs")
plt.show() # Non DL matches have a wider spread and more outliers ,while Dl applied matches show a smaller,compact box-meaning DL makes targets tighter,more controlled win margin with fewer extreme results.
sns.boxplot(x="dl_applied",y="win_by_wickets",data=df)
plt.title("DL Method Impact on win by Wickets")
plt.show() # Non DL matches has a lower median(4 wicket) with a wide spread,while DL applied have ahigher median(6 wicket) because Dl targets are often easier to chase leading to win by more wickets
sns.boxplot(x="team1",y="win_by_runs",data=df)
plt.title("Team-wise Win by Runs Analysis")
plt.xticks(rotation=90)
plt.show()  # DC and Csk shows median win margin by runs.MI have a low median but a tall box and many outliers upto 10 runs.KT and GL have a near zero median due to very few season played.
sns.scatterplot(x="win_by_runs",y="win_by_wickets",data=df)
plt.title("Relationship Between Win by Runs and Win By Wickets")
plt.show()  # THe Scatter plot shows two separate clusters x asis(win by runs) and y axis(win bt wickets) are mutually exclusive.A team can only win in one way per match,never both
sns.pairplot(df[["dl_applied","win_by_wickets","win_by_runs"]])
plt.title("Dl applied Between Win by Runs and Win By Wickets")
plt.show() # DL method is rarely applied in IPL matches.Most win happen by small runs margin or -7 wickets.win by runs and win by wickets never occurs together in the same match  
numeric_df=df.select_dtypes(include=np.number)
plt.figure(figsize=(10,6))
sns.heatmap(numeric_df.corr(),annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
print(df.info())  # when win by wickets goes up,win by runs goes down and vice versa.This is because a team can only win by runs or wickets never both in the same 



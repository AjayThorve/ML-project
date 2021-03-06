import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import metrics
# Importing the pattern Calulator custom module to analyze and calculate additional columns
import Custom_Features_Calc

pd.options.mode.chained_assignment = None  # default='warn'

# Reading data from the combined csv file including bots and non bots
data=pd.read_csv("Data/Combined_1.1.csv")

# Calculating number of occurences of 'bots' word and its variations in decription field and also number of days since account was created
data=Custom_Features_Calc.Calculate_Decription_Days(data)

RFEData=np.array(data[['desc_bot','Age','followers_count','friends_count','listed_count','favourites_count','verified','statuses_count','default_profile_image','default_profile','has_extended_profile']])
RFEDataLabels=np.array(data['bot'])


clf=RandomForestClassifier(n_estimators=10, max_depth=None,min_samples_split=2, random_state=0)
clf=RFE(clf,1)
clf.fit(RFEData,RFEDataLabels)

cols=['desc_bot','Age','followers_count','friends_count','listed_count','favourites_count','verified','statuses_count','default_profile_image','default_profile','has_extended_profile']
print("USING RFE, the ranks of each feature are:")
for i in range(len(cols)):
    print(cols[i],":",clf.ranking_[i])

#Extra tree classfier:
print("")
print("USING feature_importance property of ExtraTreesClassifier, we can see the importance of each feature")
model=ExtraTreesClassifier()
model.fit(RFEData,RFEDataLabels)
for i in range(len(cols)):
    print(cols[i],":","(importance: ",model.feature_importances_[i],")")
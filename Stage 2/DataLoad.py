#Import the necessary methods from tweepy library
import tweepy
import pandas as pd
from pandas import DataFrame
from pandas.io.json import json_normalize
import csv
import json
#Variable that contain user credentials to access Twitter API
access_token="1705054591-UmF3EDjblZ7rknx7JKYmu716X2PTbiyoVv9Tcrr"
access_token_secret="fykQJomSAXCxVa3WDvGjWS61AOtofv8E7RRdSm5lil1eC"
consumer_key="SbciRjxB88YQZTxnfVvlfGrQR"
consumer_secret="waNX7roMCQoKxVXfRJYSg42uybrWKIMthxjoTVsPnXMRIBAio4"

#Handles twitter authentication and connects to twitter Stream API
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
fields = "id id_str screen_name location description url followers_count friends_count listed_count created_at \
    favourites_count verified \
    statuses_count lang default_profile status default_profile_image has_extended_profile name Bot".split()

data=pd.read_csv('Handles_List.csv')
data['bot'].value_counts().plot(kind='bar')
#for index,row in data.iterrows():
#    row['Screen name']=row['Screen name'].replace('@','')

csvFile = open('Data_ML_project_stage_2.csv', 'a')
w=csv.DictWriter(csvFile,fields)
i=0
data=data[1991:]
for index,row in data.iterrows():
    user = api.get_user(screen_name = row['screen_name'])
    d={}
    for k in set(user._json.keys()).intersection(fields):
            d[k]=str(getattr(user,k))
    if row['bot']=="1":
        d['Bot']=1
    else:
        d['Bot']=0
    if i==0:
        w.writeheader()
        i=1
    w.writerow(d)
#for f in fields:
#    print (user.id)
#print (user)
#print(df)
#df.to_csv('results.csv')





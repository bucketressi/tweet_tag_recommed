#-*- coding:utf-8 -*-

#bearer token : AAAAAAAAAAAAAAAAAAAAAJKiAAEAAAAA0B0iKdULQ4KIe0pWIjMfJnZbasQ%3DM9qvGEMRyzxfnRPvKvma8YweT9QwdzRFv157Xd3qd88ws0F9TC

import tweepy
import sys
import re
import json
import requests
import twitter
import mysql.connector
import copy

#connect

consumer_key="c8G58hCAbUwpjzwZLmkqMHjSA"
consumer_secret="5WoiG1ZnrX9NxUtdE2JhFXqFJYdF0JJiJZ5js10FR2R5CDYDF9"

access_token="789413571641782273-exSzNSDNqOZkmO0J0YFpAmJEVSJSJaX"
access_token_secret="pRJR4tKQo1BotHoQAZwgo0RxqwhPAXiC2oaLi7yNPpgnx"

api=twitter.Api(consumer_key,consumer_secret,access_token,access_token_secret)

#api use
search = api.GetSearch("Amazon",count=500)

#db connect

mydb = mysql.connector.connect(
    host="localhost",
    user="heeeun",
    passwd="wheenue78",
    database="heeeun"
)

# db insert 
val=list() 

for tweet in search:
    follower = tweet.user.followers_count
    same=''
    mycursor = mydb.cursor()
    sql = "INSERT INTO hashtag (hashtag1, hashtag2, hashtag3, hashtag4, hashtag5, follower_count) values (%s,%s,%s,%s,%s,%s)"
    if tweet.hashtags:
        val.clear()
        for index in tweet.hashtags:
            strH = str(index).replace('"','').replace(":","").replace("{","").replace("}","").replace(" ","").replace("text","")
            if not strH[0] == "\\":
                if not strH =="":
                    val.append(strH)
        if len(val)<5:
            for _ in range(0,5-len(val)):
                val.append("")
        if not same == val[0]:
            result = val[0:5]
            result.append(follower)
            print (result)
            mycursor.execute(sql,result)
            mydb.commit()
'''


# delete bad word
mycursor = mydb.cursor()
bad_word = ['sex','porn','ass','Dildo','sexgay','gay','horny','mama','comeback','BTS','Jungkook','RM','Taejoon','Jin','EXO','SANA','MOMO','TVXQ','u0','u1','u2','u3','u4','u5','u6','u7','u8','u9']

for word in bad_word:
    for i in range(5):    
        sql = 'DELETE FROM hashtag WHERE hashtag'+str(i+1)+' LIKE '+'"%'+word+'%";'
        print(sql)
        mycursor.execute(sql)
        mydb.commit()

sql = "DELETE FROM hashtag WHERE follower_count <100;"
mycursor.execute(sql)
mydb.commit()



# record reorganize

sql = "DELETE n1 FROM hashtag n1, hashtag n2 WHERE n1.id < n2.id AND n1.hashtag1 = n2.hashtag1 and n1.hashtag2 = n2.hashtag2 and n1.hashtag3 = n2.hashtag3;"
mycursor.execute(sql)
mydb.commit()
sql = "delete from hashtag where hashtag2 = '';"
mycursor.execute(sql)
mydb.commit()
sql = "alter table hashtag auto_increment = 1;"
mycursor.execute(sql)
mydb.commit()
sql = "set @count =0;"
mycursor.execute(sql)
mydb.commit()
sql = "update hashtag set id = @count:=@count+1;"
mycursor.execute(sql)
mydb.commit()


mydb.close
'''
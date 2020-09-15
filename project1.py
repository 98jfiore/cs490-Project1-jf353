# project1.py
import flask
import os
import random
import tweepy
import html
import datetime
from dotenv import load_dotenv

#Load environmental variables
load_dotenv()

#Set up authentication for the tweepy API using environmental variables set up like in the README
auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET"))
auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))

#Get the tweepy object you can use to access the Twitter API
api = tweepy.API(auth, wait_on_rate_limit=True)

#Date to get Tweets from
date_since="2017-09-12"

#The list of possible foods to be randomly selected
foods = ["Tart", "Pie", "Cake", "Roll", "Donut", "Brittle", "Croissant", "Cupcake", "Fudge", "Creme"]

#Set up the flask app
app = flask.Flask(__name__)

@app.route('/')
def index():
    #Randomly select a food from the list of foods
    rand_food = random.randint(0, len(foods)-1)
    
    #Search twitter for tweets including the food name
    search = foods[rand_food] + " -filter:retweets -has:media -filter:reply"
    tweets = tweepy.Cursor(api.search, q=search, lang="en", tweet_mode="extended").items(10)
    
    #Get search result from list of found tweets
    tweet = None
    numTweet =  random.randint(1, 10)
    for i in range(0, numTweet):
        hold = tweets.next()
        if hold == None:
            break
        tweet = hold
    
    #Format the Tweet's datetime
    tweetDT = tweet.created_at
    tweetTimeStamp = tweetDT.strftime("%-I:%M %p\t&#xB7\t%-m/%-d/%y")
    
    #Render the page
    return flask.render_template(
        "index.html",
        selected_food = foods[rand_food],
        tweet_text = html.unescape(tweet.full_text),
        tweet_user_sname = tweet.user.screen_name,
        tweet_user_image = tweet.user.profile_image_url,
        tweet_user_name = tweet.user.name,
        tweet_timeDate = html.unescape(tweetTimeStamp)
    )

#Run the flask app
app.run(
    port=(int(os.getenv('PORT', 8080))),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)

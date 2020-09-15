# CS490-PROJECT1-JF353

## READ ME
    
    This project randomly selects a recipe and displays it, along with a picture from the recipe and a Tweet relating to the recipe.
    
    At the root directory, there is a .gitignore file set up to ignore .env, which is where API keys are currently being stored.
    In the .env file, the twitter API's consumer key, consumer secret, access token, and access token secret are saved as CONSUMER_KEY,
        CONSUMER_SECRET, ACCESS_TOKEN, and ACCESS_TOKEN_SECRET respectively.
        
    To test the app, simply run "python project1.py" on your command line while in this project's root directory.
        To see what was deployed view a preview of the currently running python file.
    
    KNOWN PROBLEMS
        The styling on the Tweets section is poor.
        No recipes are being found as I have not used the Spoonacular API yet
        Heroku is not currently being used.
    
    INSTALLATIONS
        To run this app, a few things need to be installed.
            I used pip install for tweepy, python-dotenv, and flask.
            Git also needs to be downloaded for your environment, you can check if its installed on your CLI with the command "git --version"
            
    TECHNICAL ISSUES AND SOLUTIONS
    
        There was an issue where the style.css file was not updating the format of the webpage.  The eventual solution was that in
            order for the page to be properly updated, it needed to be reloaded ignoring the cache.  I use Google Chrome, so this
            meant pressing Ctrl+Shift+r whenever I wanted to see the updated page.
            
        There was an issue with the css styling of the webpage, specifically with the recipe and pictures alignment where they
            were refusing to align horizontally.  I tried to fix this by floating them, but that pushed the border above them,
            which is something I didn't want.  The eventual solution I found was to utilize a flexbox display instead of float.
            
        There was an issue where some tweets would not retrieve their full text, so I had to set my Tweepy Cursor call to get tweets
            in tweet mode 'extended' and retrieve tweet.full_text instead of tweet.text
            
CS490-PROJECT1-JF353

READ ME
    
    This project randomly selects a recipe and displays it, along with a picture from the recipe and a Tweet relating to the recipe.
    
    KNOWN PROBLEMS
        No Tweets are currently being selected as I cannot figure out how to use config variables in python.
        No recipes are being found as I have not used the Spoonacular API yet
        Heroku is not currently being used.
        Github is not currently being used.
    
    INSTALLATIONS
        To run this app, a few things need to be installed, I used pip install.
            These are tweepy, git, and flask.
            
    TECHNICAL ISSUES AND SOLUTIONS
    
        There was an issue where the style.css file was not updating the format of the webpage.  The eventual solution was that in
            order for the page to be properly updated, it needed to be reloaded ignoring the cache.  I use Google Chrome, so this
            meant pressing Ctrl+Shift+r whenever I wanted to see the updated page.
            
        There was an issue with the css styling of the webpage, specifically with the recipe and pictures alignment where they
            were refusing to align horizontally.  I tried to fix this by floating them, but that pushed the border above them,
            which is something I didn't want.  The eventual solution I found was to utilize a flexbox display instead of float.
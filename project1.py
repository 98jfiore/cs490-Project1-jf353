# project1.py
import flask
import os
import random
import tweepy
import html
import datetime
import requests
from dotenv import load_dotenv

#Load environmental variables
load_dotenv()

#Set up authentication for the tweepy API using environmental variables set up like in the README
auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET"))
auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))

#Get the tweepy object you can use to access the Twitter API
api = tweepy.API(auth, wait_on_rate_limit=True)

#The list of possible foods to be randomly selected
foods = ["Tart", "Pie", "Cake", "Roll", "Donut", "Brittle", "Croissant", "Cupcake", "Fudge", "Creme"]

#Set up the flask app
app = flask.Flask(__name__)

@app.route('/')
def index():
    #Randomly select a food from the list of foods
    rand_food = random.randint(0, len(foods)-1)
    
    #SPOONACULAR
    
    #Set up the parameters for searching spoonacular for recipes
    recipe_searchParam = {
        'apiKey': os.getenv("SPOON_API_KEY"), 
        'query': foods[rand_food],
        'number': 15
    }
    
    #Randomly get a recipe from spoonacular utilizing the parameters
    recipes = requests.get("https://api.spoonacular.com/recipes/complexSearch", params=recipe_searchParam).json()
    #Fake recipe for testing if you run out of Spoonacular requests
    #recipes = {'results': [{'id': 1161745, 'title': 'Cake Balls', 'image': 'https://spoonacular.com/recipeImages/1161745-312x231.jpg', 'imageType': 'jpg'}], 'offset': 0, 'number': 1, 'totalResults': 453}
    recipe_num = random.randint(0, min(recipes["totalResults"]-1, recipes["number"]-1))
    recipe = recipes['results'][recipe_num]
    
    #Get the details for the recipe from spoonacular
    recipe_detailsParam = {
        'apiKey': os.getenv("SPOON_API_KEY")
    }
    details_url = "https://api.spoonacular.com/recipes/" + str(recipe['id']) + "/information"
    recipe_details = requests.get(details_url, params=recipe_detailsParam).json()
    #Fake recipe for testing if you run out of Spoonacular requests
    """
    recipe_details = {'vegetarian': False, 'vegan': False, 'glutenFree': False, 'dairyFree': False, 'veryHealthy': False, 'cheap': False, 'veryPopular': False, 'sustainable': False, 'weightWatcherSmartPoints': 21, 'gaps': 'no', 'lowFodmap': False, 
        'preparationMinutes': 60, 'cookingMinutes': 0, 'aggregateLikes': 1, 'spoonacularScore': 9.0, 'healthScore': 0.0, 'creditsText': 'Jen West', 'license': 'CC BY-SA 3.0', 'sourceName': 'Pink When', 'pricePerServing': 87.27, 'extendedIngredients':
        [{'id': 18137, 'aisle': 'Baking', 'image': 'white-cake-mix.jpg', 'consistency': 'solid', 'name': 'vanilla cake mix', 'original': '1 classic vanilla cake', 'originalString': '1 classic vanilla cake', 'originalName': 'classic vanilla cake', 'amount': 1.0, 
        'unit': '', 'meta': [], 'metaInformation': [], 'measures': {'us': {'amount': 1.0, 'unitShort': '', 'unitLong': ''}, 'metric': {'amount': 1.0, 'unitShort': '', 'unitLong': ''}}}, {'id': 10711111, 'aisle': 'Baking', 'image': 'food-coloring.png', 
        'consistency': 'solid', 'name': 'food coloring', 'original': '1/4 tsp food coloring divided', 'originalString': '1/4 tsp food coloring divided', 'originalName': 'food coloring divided', 'amount': 0.25, 'unit': 'tsp', 'meta': ['divided'], 'metaInformation': ['divided'], 
        'measures': {'us': {'amount': 0.25, 'unitShort': 'tsps', 'unitLong': 'teaspoons'}, 'metric': {'amount': 0.25, 'unitShort': 'tsps', 'unitLong': 'teaspoons'}}}, {'id': 1145, 'aisle': 'Milk, Eggs, Other Dairy', 'image': 'butter-sliced.jpg', 'consistency': 'solid', 
        'name': 'unsalted butter', 'original': '1 stick unsalted butter', 'originalString': '1 stick unsalted butter', 'originalName': 'unsalted butter', 'amount': 1.0, 'unit': 'stick', 'meta': ['unsalted'], 'metaInformation': ['unsalted'], 'measures': {'us': {'amount': 1.0,
        'unitShort': 'stick', 'unitLong': 'stick'}, 'metric': {'amount': 1.0, 'unitShort': 'stick', 'unitLong': 'stick'}}}, {'id': 19336, 'aisle': 'Baking', 'image': 'powdered-sugar.jpg', 'consistency': 'solid', 'name': "confectioners' sugar", 
        'original': "2 cups confectioners' sugar", 'originalString': "2 cups confectioners' sugar", 'originalName': "confectioners' sugar", 'amount': 2.0, 'unit': 'cups', 'meta': [], 'metaInformation': [], 'measures': {'us': {'amount': 2.0, 'unitShort': 'cups', 'unitLong': 'cups'}, 
        'metric': {'amount': 473.176, 'unitShort': 'ml', 'unitLong': 'milliliters'}}}, {'id': 1077, 'aisle': 'Milk, Eggs, Other Dairy', 'image': 'milk.png', 'consistency': 'liquid', 'name': 'milk', 'original': '1 1/2 tbsp milk', 'originalString': '1 1/2 tbsp milk', 'originalName': 'milk',
        'amount': 1.5, 'unit': 'tbsp', 'meta': [], 'metaInformation': [], 'measures': {'us': {'amount': 1.5, 'unitShort': 'Tbsps', 'unitLong': 'Tbsps'}, 'metric': {'amount': 1.5, 'unitShort': 'Tbsps', 'unitLong': 'Tbsps'}}}, {'id': 93775, 'aisle': 'Baking', 
        'image': 'chocolate-candy-melt.png', 'consistency': 'solid', 'name': 'candy melts', 'original': '2 1/2 cups candy melts', 'originalString': '2 1/2 cups candy melts', 'originalName': 'candy melts', 'amount': 2.5, 'unit': 'cups', 'meta': [], 'metaInformation': [], 
        'measures': {'us': {'amount': 2.5, 'unitShort': 'cups', 'unitLong': 'cups'}, 'metric': {'amount': 591.47, 'unitShort': 'ml', 'unitLong': 'milliliters'}}}], 'id': 1161745, 'title': 'Cake Balls', 'readyInMinutes': 60, 'servings': 12, 
        'sourceUrl': 'https://www.pinkwhen.com/cake-balls-recipe/', 'image': 'https://spoonacular.com/recipeImages/1161745-556x370.jpg', 'imageType': 'jpg', 'summary': 'The recipe Cake Balls can be made <b>in around 1 hour</b>. One portion of this dish contains about \
        <b>2g of protein</b>, <b>15g of fat</b>, and a total of <b>410 calories</b>. For <b>87 cents per serving</b>, you get a dessert that serves 12. 1 person were glad they tried this recipe. If you have classic vanilla cake, food coloring, milk, and a few other ingredients \
        on hand, you can make it. It is brought to you by Pink When. Overall, this recipe earns a <b>very bad (but still fixable) spoonacular score of 0%</b>. Users who liked this recipe also liked <a href="https://spoonacular.com/recipes/corn-cake-bean-balls-aka-fiesta-balls-25903">Corn Cake Bean Balls,\
        Aka Fiesta Balls</a>, <a href="https://spoonacular.com/recipes/cake-balls-cake-truffles-1078183">Cake Balls (Cake Truffles)</a>, and <a href="https://spoonacular.com/recipes/cake-balls-131546">Cake Balls</a>.', 'cuisines': [], 'dishTypes': ['dessert'], 'diets': [], 
        'occasions': [], 'winePairing': {'pairedWines': ['cream sherry', 'moscato dasti', 'port'], 'pairingText': "Cake works really well with Cream Sherry, Moscato d'Asti, and Port. A common wine pairing rule is to make sure your wine is sweeter than your food. Delicate desserts \
        go well with Moscato d'Asti, nutty desserts with cream sherry, and caramel or chocolate desserts pair well with port. The NV Solera Cream Sherry with a 4.5 out of 5 star rating seems like a good match. It costs about 17 dollars per bottle.", 
        'productMatches': [{'id': 428475, 'title': 'NV Solera Cream Sherry', 'description': 'The Solera Cream Sherry has a brilliant amber and deep copper hue. With butterscotch and pecan aromas, the sweet salted nut and brown spice aromas carry a complex caramel accent. \
        A sweet entry leads to a rounded, lush, moderately full-bodied palate with a lengthy, flavorful finish.', 'price': '$16.99', 'imageUrl': 'https://spoonacular.com/productImages/428475-312x231.jpg', 'averageRating': 0.9, 'ratingCount': 4.0, 'score': 0.823076923076923, 
        'link': 'https://www.amazon.com/NV-Solera-Cream-Sherry-750/dp/B00HSME8OW?tag=spoonacular-20'}]}, 'instructions': 'Instructions\n\nBake cake according to instructions, add food coloring if desired, and allow to cool.\n\nTo make the buttercream, beat together butter, sugar, \
        and milk in a mixer on low speed. Add food coloring if desired.\n\nIn a large bowl crumble cake, add buttercream, and mix well.\n\nRoll cake mixture into 2-inch balls. Makes approximately 24 cake balls. Place on a lined cookie sheet with wax paper. \
        Place in the refrigerator for a minimum of 45 minutes.\n\nPlace candy melts in microwave-safe bowl and heat in 30-second increments on half power.\n\nDip cake truffles carefully and place them back on the lined cookie sheet.\n\nAllow the cake balls to set for at least 30 minutes before serving or storing.', 
        'analyzedInstructions': [{'name': '', 'steps': [{'number': 1, 'step': 'Bake cake according to instructions, add food coloring if desired, and allow to cool.', 'ingredients': [{'id': 10711111, 'name': 'food color', 'localizedName': 'food color', 'image': 'food-coloring.png'}], 
        'equipment': [{'id': 404784, 'name': 'oven', 'localizedName': 'oven', 'image': 'oven.jpg'}]}, {'number': 2, 'step': 'To make the buttercream, beat together butter, sugar, and milk in a mixer on low speed.', 'ingredients': [{'id': 1001, 'name': 'butter', 'localizedName': 'butter', 
        'image': 'butter-sliced.jpg'}, {'id': 1053, 'name': 'cream', 'localizedName': 'cream', 'image': 'fluid-cream.jpg'}, {'id': 19335, 'name': 'sugar', 'localizedName': 'sugar', 'image': 'sugar-in-bowl.png'}, {'id': 1077, 'name': 'milk', 'localizedName': 'milk', 'image': 'milk.png'}],
        'equipment': [{'id': 404726, 'name': 'blender', 'localizedName': 'blender', 'image': 'blender.png'}]}, {'number': 3, 'step': 'Add food coloring if desired.', 'ingredients': [{'id': 10711111, 'name': 'food color', 'localizedName': 'food color', 'image': 'food-coloring.png'}], 'equipment': []}, 
        {'number': 4, 'step': 'In a large bowl crumble cake, add buttercream, and mix well.', 'ingredients': [], 'equipment': [{'id': 404783, 'name': 'bowl', 'localizedName': 'bowl', 'image': 'bowl.jpg'}]}, {'number': 5, 'step': 'Roll cake mixture into 2-inch balls. Makes approximately 24 cake balls.',
        'ingredients': [{'id': 0, 'name': 'roll', 'localizedName': 'roll', 'image': 'dinner-yeast-rolls.jpg'}], 'equipment': []}, {'number': 6, 'step': 'Place on a lined cookie sheet with wax paper.', 'ingredients': [{'id': 10118192, 'name': 'cookies', 'localizedName': 'cookies', 
        'image': 'shortbread-cookies.jpg'}], 'equipment': [{'id': 404727, 'name': 'baking sheet', 'localizedName': 'baking sheet', 'image': 'baking-sheet.jpg'}, {'id': 404739, 'name': 'wax paper', 'localizedName': 'wax paper', 'image': 'wax-paper.jpg'}]}, 
        {'number': 7, 'step': 'Place in the refrigerator for a minimum of 45 minutes.', 'ingredients': [], 'equipment': [], 'length': {'number': 45, 'unit': 'minutes'}}, {'number': 8, 'step': 'Place candy melts in microwave-safe bowl and heat in 30-second increments on half power.', 
        'ingredients': [{'id': 93775, 'name': 'candy melts', 'localizedName': 'candy melts', 'image': 'chocolate-candy-melt.png'}], 'equipment': [{'id': 404762, 'name': 'microwave', 'localizedName': 'microwave', 'image': 'microwave.jpg'}, {'id': 404783, 'name': 'bowl', 
        'localizedName': 'bowl', 'image': 'bowl.jpg'}]}, {'number': 9, 'step': 'Dip cake truffles carefully and place them back on the lined cookie sheet.', 'ingredients': [{'id': 0, 'name': 'truffles', 'localizedName': 'truffles', 'image': ''}, {'id': 10118192, 'name': 'cookies', 
        'localizedName': 'cookies', 'image': 'shortbread-cookies.jpg'}, {'id': 0, 'name': 'dip', 'localizedName': 'dip', 'image': ''}], 'equipment': [{'id': 404727, 'name': 'baking sheet', 'localizedName': 'baking sheet', 'image': 'baking-sheet.jpg'}]}, 
        {'number': 10, 'step': 'Allow the cake balls to set for at least 30 minutes before serving or storing.', 'ingredients': [], 'equipment': [], 'length': {'number': 30, 'unit': 'minutes'}}]}], 'originalId': None, 'spoonacularSourceUrl': 'https://spoonacular.com/cake-balls-1161745'}
    """
    
    #Get list of ingredients and their amounts to display
    ingredients = []
    for ingredient in recipe_details["extendedIngredients"]:
        ing = str(ingredient["amount"]) + " " + ingredient["unit"] + "\t" + ingredient["name"]
        ingredients.append(ing)
    
    #TWITTER
    
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
        recipe_img = recipe['image'],
        recipe_name = recipe['title'],
        recipe_servings = recipe_details['servings'],
        recipe_cookTime = recipe_details['readyInMinutes'],
        recipe_link = recipe_details['sourceUrl'],
        recipe_ingredients_len = len(ingredients),
        recipe_ingredients = ingredients,
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

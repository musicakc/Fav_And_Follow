from twitter import Twitter,OAuth, TwitterHTTPError

TWITTER_APP_KEY = ''
TWITTER_APP_KEY_SECRET = ''
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_TOKEN_SECRET= ''

t = Twitter(auth=OAuth(TWITTER_ACCESS_TOKEN,TWITTER_ACCESS_TOKEN_SECRET,TWITTER_APP_KEY,TWITTER_APP_KEY_SECRET))


# Function to search a particular term in tweets
def search_tweets(q,count=10,m_id=None):
    return t.search.tweets(q=q,result_type='recent',count=count,lang="en",max_id=m_id)

# Function to favorite a tweet
def favorites_create(tweet):
    try:
        result = t.favorites.create(_id=tweet['id'])
        print "Favorited: %s %s" % (result['text'],result['id'])
        return result
    except TwitterHTTPError as e:
        print "Error: ", e
        return None

# Function to search and favorite the tweet with the required term 
def search_and_fav(q,count=10,m_id=None):
    result = search_tweets(q,count,m_id)
    first_id=result['statuses'][0]['id']
    last_id = result['statuses'][-1]['id']
    success = 0
    for t in result['statuses']:
        if favorites_create(t) is not None:
            success += 1

    print "Favorites total: %i of %i" % (success, len(result['statuses']))
    print "First id %s last id %s" %(first_id, last_id)


# As an example searching for the term "natural language processing"
search_and_fav('natural language processing',3)

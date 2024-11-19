import praw

clientID = "Y-BuBBF7q2lbpsMo5r4rCQ"
clientSecret = "L9tLUktoIBMxQmbyYDuawxeUboQjwg"
password = "JujuBeat123"
userAgent = "sentwsb by u/Educational-Duck9147"
userName = "Educational-Duck9147"
reddit = praw.Reddit(client_id = clientID, client_secret = clientSecret, user_agent = userAgent, username = userName, password = password)

print(reddit.user.me())

subreddit = reddit.subreddit("wallstreetbets")
dict = {
    "TSLA": 0,
    "AAPL": 0,
    "AMZN": 0,
    "GOOGL": 0,
    "MSFT": 0,
    "FB": 0,
    "BRK.B": 0,
    "JNJ": 0,
    "JPM": 0,
    "V": 0,
    "PG": 0,
    "UNH": 0,
    "MA": 0,
    "HD": 0,
    "NVDA": 0,
    "DIS": 0,
}
for post in subreddit.new(limit = 30):
    for i in dict:
        if i in post.title:
            dict[i] += 1
print(dict)
print(max(dict))



import praw
"""
Reddit:
id : 
uMDtYdkzqU6OEw5tqzNQBQ
secret: 
G1rN_T0bpOyVXz3xiONPdlnjcxrcBg
name: 
app123
user: 
Ok-Guess7756
"""
if __name__ == '__main__':
    reddit = praw.Reddit(
        client_id='uMDtYdkzqU6OEw5tqzNQBQ',
        client_secret='G1rN_T0bpOyVXz3xiONPdlnjcxrcBg',
        redirect_uri='http://localhost:8080',
        user_agent='app123/1.0 by /u/Ok-Guess7756'
    )

    # auth_url = reddit.auth.url(['identity', 'submit'], 'UniqueState', 'permanent')
    # print("Please go to this URL and authorize access:", auth_url)

    subreddit = reddit.subreddit('learnpython')

    # Iterate through the top posts in the subreddit
    for submission in subreddit.top(limit=5):  # Limit to 5 top posts
        # print(f'Title: {submission.title}')
        # print(f'Score: {submission.score}')
        # print(f'selftext: {submission.selftext}')
        # print(f'URL: {submission.url}')
        # print('---------------------------------\n')
        x = submission.selftext

    print(x.upper())

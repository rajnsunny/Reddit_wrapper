from django.shortcuts import render
from django.http import HttpResponse
from dotenv import load_dotenv
import os
import praw
import json


# Create your views here.
def article_list(request,id):
    load_dotenv()
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    USER_AGENT = os.getenv('USER_AGENT')
    reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT)
    subreddit = reddit.subreddit(id)

    articles = subreddit.new(limit = 10)
    article_data = []
    for article in articles:
        article_data.append({
            'title': article.title,
            'author': article.author.name,
            'creation_date': article.created_utc,
            'link': article.url,
            'thread_link': f'https://www.reddit.com{article.permalink}'
        })

    json_data = json.dumps(article_data)
    
    
    #render(request, 'reddit_fetcher/article_list.html', article_data)

    return HttpResponse(json_data)


    




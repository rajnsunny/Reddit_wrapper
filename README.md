# Reddit_wrapper

youtube_link: https://youtu.be/gLykCfJl2PY
## Packages:
- python-dotenv
- praw
- Django
- django-cors-headers

## Environment Variables:
```
CLIENT_ID: <Reddit_CLIENT_ID>
CLIENT_SECRET: <Reddit_CLIENT_SERVER>    Go to https://www.reddit.com/prefs/apps to register the app.
USER_AGENT: <Unique_USER_SPECS.>
```

## Instruction to Try the Application:
  ### Server
  - Create a Virtual environment `python -m venv <env_name>`
  - Activate IT `<env_name>/Scripts/Activate.ps1`
  - Now clone the git or download the repo there
  - `cd RedditApp`
  - `pip install -r requirements.txt`   
  - `python manage.py runserver`
  - GET /reddit/<subreddit_name>


    ### Client
    - simply open the HTML file 
    - check for URL of the server (default: http://127.0.0.1:8000)
    - now it will fetch and display the result.

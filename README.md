# Smarter & intelligent Kidney function Analysis App

This is the backend of our application collaboration with a biomedical company. Aim of the project is to analyse the condition of Kidney by using this platform and a strip provided by company. Company will provide a medical strip which the user has to take an Image with our mobile app. Which will analyse the strip and based on the colour of the strip we'll try to analyse the condition of kidney.

### Usage on localhost

` pip install -r requirements`

` python main.py`

### To deploy on heroku.
#### First install heroku-cli

on mac ` brew install heroku/brew/heroku `

on linux ` sudo snap install heroku --classic `

#### Second step refresh autocomplete cache

` heroku autocomplete --refresh-cache `

#### Third step login into heroku-cli

` heroku login`

#### Build heroku app

` heroku create`

#### Add buildpacks 

` heroku buildpacks:add --index 1 heroku-community/apt`

#### Push to the heroku app

` git push heroku master`

#### To keep track of activity of your app.

` heroku logs --tail`
# Smarter & intelligent Kidney function Analysis App

This is the backend of our application collaboration with a biomedical company. Aim of the project is to analyse the condition of Kidney by using this platform and a strip provided by company. Company will provide a medical strip which the user has to take an Image with our mobile app. Which will analyse the strip and based on the colour of the strip we'll try to analyse the condition of kidney.

This app is deployed on [heroku](https://floating-retreat-64345.herokuapp.com/).

## Reuqired fields

To use above app you need to make a post request with parameters given as
- ` name` field to specify users name.
- ` age` field to specify users age.
- ` sex` field to specify users sex.
- ` contact_no` field to specify users contact number.

and also need to proved body:
- ` image` where we need to upload image of strip.


### Usage on localhost

```shell script
pip install -r requirements
python main.py
```

### To deploy on heroku.
#### First install heroku-cli

- ` brew install heroku/brew/heroku ` on mac.

- ` sudo snap install heroku --classic ` on linux.

#### NEXT
- Second step refresh autocomplete cache.
- Third step login into heroku-cli.
- Build heroku app.
- Add buildpacks 
- Push to the heroku app

```shell script
heroku autocomplete --refresh-cache
heroku login
heroku create
heroku buildpacks:add --index 1 heroku-community/apt
git push heroku master
```

#### To keep track of activity of your app.

` heroku logs --tail`
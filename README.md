![picture of responsiveness]()


# [LINK FOR LIVE VIEW](https://forum-knasten.herokuapp.com/)

# Content

1. [Introduction](#introduction)
2. [Design](#design)
3. [Data Structure](#data-structure)
4. [Wireframes](#wireframes)
5. [User Stories](#user-stories)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Validation](#validation)
9. [Tech](#tech)
10. [Credits](#credits)



# Introduction
I choose to do this cause gaming has been a hobby of mine since I was just a little kid.
So I wanted to make a place where gamers could gather round and chat/post about their favorite parts.

# Design
I choose to go with some darker colors but with alot of white around. And the colors I choose is choosen to contrast each other making sure there is high visibility. Then in some places around all theese dark brooding boring colors you will find some splashes of color. All designed to make certain functions pop out to the user.
Aswell as when a user is looking at post if he sees one he has created it will say the author name in bold. This was thoughtfully made to make sure you don't have to search for your post.

# Data Structure
![Picture of data-structure](readme/images/data-structure.jpeg)

# Wireframes
When looking at these wireframes you can see it isn't made identical to what the plan was.
This is partially because I did not have the time to fix the profile page and profile model like I would want to.
So the profile page has not been created yet but, I reckoned I might aswell show you a little something of how I plan for it to look.
1. [Landing Page](readme/images/landing_page.jpeg)
2. [Profile Page](readme/images/profile_page.jpeg)
3. [Current Post Page](readme/images/currentpost_page.jpeg)
4. [All Posts Page](readme/images/allposts_page.jpeg)

# User Stories
My sole purpose of this site was to build something to share ideas and knowledge about the games we love.
And perhaps you can find your next gaming companion or promote your twitch channel. The choice is yours.

| **As a**   | **I would like to**              | **So that I can**                             | **requisites**     | **status** |
|------------|----------------------------------|-----------------------------------------------|--------------------|------------|
| USER       | add post                         | ask questions                                 | authenticated user |    Done    |
| USER       | comment on posts                 | answer questions                              | authenticated user |    Done    |
| USER       | like post                        | show my appreciation                          | authenticated user |    Done    |
| USER       | visit my profile page            | change my profile settings                    | authenticated user | Postponed  |
| USER       | be able to upload images         | share images of variations                    | authenticated user |    Done    |
| USER       | be able to open posts            | read the content and participate              |         -          |    Done    |
| USER       | browse posts by game             | find the right post more easily               |         -          |    Done    |
| USER       | be able to style my posts        | present my information in a neat and nice way | authenticated user |    Done    |
| USER       | be able to remove my posts       | remove content I no longer wish to display    | authenticated user |    Done    |
| USER       | be able to remove my comments    | correct any mistakes I may do                 | authenticated user |    Done    |
| USER       | request removal of my account    | get any personal info deleted                 | authenticated user | Postponed  |
| USER       | PM other users                   | have an conversation in private               | authenticated user | Postponed  |
| USER       | see number of post in a category | see if it is an category with much attendance |         -          |    Done    |
| SITE OWNER | disable misbehaving users        | keep the site clean                           | superuser          | Postponed  |
| SITE OWNER | browse account removal requests  | remove the accounts in question               | superuser          | Postponed  |
| SITE OWNER | Manage any posts and comments    | remove explicit content                       | superuser          |    Done    |

## Features To Consider ##

- Direct Message System (User to User)
- Comment chains (reply system)
- Verification either email or another social media account.
- Create Profilepage
- Add total likes to profile
- Add top posters of the week board

# Testing

Automated testing has not been implemented in this project. So instead I have done all the testing manually.

* **Implementation:** Edit button and code to make it possible for a super user to edit any post.
* **Test:** To test this implementation, I wrote some test posts with different accounts. Then logged in to my super user and tried to edit a couple posts.
* **Result:** All posts was edited however I noticed it changed the original author.
* **Verdict:** Test passed it does edit the post however some fixes are needed to make sure author doesn't change.
<hr>

* **Implementation:** Delete button and viewcode to make it possible for a super user to delete any post.
* **Test:** To test this implementation, I used some of all the test post I written and went on to delete it.
* **Result:** The posts were removed and everything was working as expected
* **Verdict:** Test passed without any troubles.
<hr>


* **Implementation:** Auto selection of game on add post view
* **Test:** To test this implementation, I clicked my way in to add post page, and filled it out with some test data without choosing game.
* **Result:** It worked, after posting it jumped back to the right category again and the post were visible. However if trying to access this view from home page with url would cause an error
* **Verdict:** Test passed it did what it was supposed to however this error needs to be addressed and fixed.
<hr>

* **Implementation:** Add edit possibilty for the author of an post
* **Test:** To test this implementation, I went in on an account created an post. Then tried to edit the content and the title.
* **Result:** It all worked good, when changing title and content then applying it sent me back to the postview with all changes applied.
* **Verdict:** Test passed as expected without any bugs present.
<hr>

* **Implementation:** Add the function to like a post.
* **Test:** To test this implementation, I logged in to one of my accounts and tried liking different posts.
* **Result:** It liked like it was supposed to however if I logged out of the account and liked it threw and 500 error. 
* **Verdict:** Test passed but bugs were present. Need to add authentication to like view, and send them to login page instead if clicking when logged out.
<hr>

* **Implementation:** Making summernote more responsive
* **Test:** To test this implementation, I went in to add post and changed the device to some different phones and sizes.
* **Result:** After this implementation it does scale much better, however summernote does not seem to be preferable on phones.
The toolbar at the top does not scale well so you get an horizontal scroll inside the notepad.
* **Verdict:** Test passed but does need some review in future development
<hr>

# Bugs
* **Problem:** 500 Error on signup if email is filled out.
* **Cause:** Email verifications without any setup in django.
* **Solution:** Removed email verification by adding ACCOUNT_EMAIL_VERIFICATION = 'None' to settings.py. This to stop an email from trying to be sent.

<hr>

* **Problem:** Form error when adding comment."No Author ID"
* **Cause:** Script was missing accidently been deleted, which filled out the hidden input
* **Solution:** Checked the old commmit and copied and pasted in the code again.

<hr>

* **Problem:** By editing a post it changes the user. For instance if a superuser needs to fix some content.
* **Cause:** When editing it uses the same form as adding, so the script filled out the wrong author-id.
* **Solution:** Changed out variable for author from user to post.user and it all worked.

<hr>

* **Problem:** Trying to access add-post page from the homepage throws an error.
* **Cause:** It couldn't find the HTTP_REFFERER since there is none when trying to access it this way.
* **Solution:** Added an if statement to check if HTTP_REFFERER exists in add-post and if it doesn't it hops over the code for prepoulating game field.
<hr>

* **Problem:** When trying to like a page while not logged in, it sends you to login, but after you login it throws error.
* **Cause:** It is because it can not find the post without the id it gets from the request when clicking like.
* **Solution:** Disabled the like buttons for non logged in users instead.

# Unresolved Issues

The only known issue for me right now is summernote, it still does not look good but it is functional. At a later time I would like to see if there is, any other text editor more suited for phones. If there is one to be used it would make the phone use much easier and hopefully it would look neater aswell.

# Deployment

## Deployment Requirements
- [Cloudinary](https://cloudinary.com/homepage-ai-capabilities) account to store static files.
- [Github](https://github.com/)
- [Heroku](https://dashboard.heroku.com/)

## Deployment Steps

### Setting Up Repository
1. Get link to copy my [repository](https://github.com/Knasten/forum). You can do this by clicking the green "code" button and then copy the HTTPS link.

2. Start up your own repository and enter bash command "git clone {link you copied}". Now you have copied everything and the settings can start.

3. Add an env.py file to root directory. If you are setting up for deployment with heroku check out step 4 in Deployment to heroku, if you need help finding your DATABASE_URL. In this file you will add:
```bash
import os

os.environ["SECRET_KEY"] = "[Your Secret Key]"
os.environ["DATABASE_URL"] = "[Your DB URL]"
os.environ["CLOUDINARY_URL"] = "[Your CLOUDINARY URL]"
```

4. Run this command to install everything in requirements.txt
```bash
pip3 install -r requirements.txt
```

### Setting Up Your DB / Creating superuser
1. To setup the database you must run the following command
```bash
python3 manage.py migrate
```
2. Then create your super user by typing this command
```bash
python3 manage.py createsuperuser
```
3. Start the server by running this command
```bash
python3 manage.py runserver
```
4. You should now have gotten a message if you want to browse your server. If you click this it should be working. Though since it is your own database it won't be populated with anything until you fill it up.

### Deploying to Heroku
If you want to run this is an online environment I recommend trying heroku. Before trying this make sure you have followed the steps prior to this.
1. Either create an account or log in at [Heroku](https://dashboard.heroku.com/)
2. Set up a new app with a unique name in your region.
3. Locate resource tab and in addons field search for "postgres" and select free option

4. Locate your settings for app and reveal your config vars. Here you will find your DATABASE_URL this should be copied in to your env.py file so if you are running locally you will still be accessing the same database.
5. While you are at the config vars also add:
´´´bash
CLOUDINARY_URL : {Your Cloudinary Url}
SECRET_KEY : {Your Secret Key}
´´´
6. In heroku dasboard select deploy tab
7. Select deploy from github you can also enable auto deploy for future push
8. You can now follow the deployment in the window and when it is done you click "open app" at the top.

# Validation
* To validate my python files I ran them all through [PEP8 Online Check](http://pep8online.com/)
Below you can find the results of the tests. Only things left are some too long lines which can be seen in the document of "PEP8 settings.py"

### LINKS TO VALIDATION TEXT ###
- [PEP8 admin.py](readme/txt/result_admin.py.txt)
- [PEP8 apps.py](readme/txt/result_apps.py.txt)
- [PEP8 contexts.py](readme/txt/result_contexts.py.txt)
- [PEP8 forms.py](readme/txt/result_forms.py.txt)
- [PEP8 models.py](readme/txt/result_models.py.txt)
- [PEP8 urls.py](readme/txt/result_urls.py.txt)
- [PEP8 views.py](readme/txt/results_views.py.txt)
- [PEP8 settings.py](readme/txt/results_settings.py.txt)

* To validate my HTML I ran them through [HTML Validator](https://validator.w3.org/)
And everything turned out all right except for summernotes widget which has alot of errors, which is an cause of how summernotes are built.
This can be seen in picture number 3 all theese faults origins from summernote widget.

### HTML Validations Images and Links ####
1. [CSS Validation](readme/images/css_validation.png)
2. [Landing Page Validation](readme/images/landing_page_validation.png)
3. [Summernote Errors](readme/images/summernote_errors.png)
4. [Login Validation](readme/images/login_validation.png)
5. [Logout Validation](readme/images/logout_validation.png)
6. [Post Detail Validation](readme/images/post_detail_validation.png)
7. [Post List Validation](readme/images/postlist_validation.png)
8. [Register Validation](readme/images/register_validation.png)

# Tech Used

### Languages
- HTML
- CSS
- Javascript
- [Python](https://www.python.org/)

### Frameworks
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)

### Libraries
- [Jquery](https://jquery.com/)

### Tools
- [Cloudinary](https://cloudinary.com/homepage-ai-capabilities)
- [Heroku](https://dashboard.heroku.com/apps)
- [Postgres](https://landing.aiven.io/en/aiven-for-postgresql/?gclid=Cj0KCQiAoY-PBhCNARIsABcz7718vMAf8vQ-EwksGq3BwF7ZqbVdE4MEKDHxc3eg_mhQncDbyq-vBGAaAoJKEALw_wcB)

# Credit
Credit goes out to my mentor Richard Wells for all the awesome help during this project.

And also to Stackoverflow for having some quick answers [Link to Stackoverflow](https://stackoverflow.com/)


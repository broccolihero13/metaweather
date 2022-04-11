# MetaWeather Personalizer
Anyonymous users (currently the only option) will get the average max temperature of Salt Lake City, Los Angeles, and Boise. A user may sign up and personalize which cities they want to display (up to 10). This is a basic starting point for building a more complicated weather app using the MetaWeather API.

# Quick Start Guide
1. Run `python3 -m venv venv` to set up your virtual environment and keep your global settings from being overwritten
2. Run `. venv/bin/activate` to activate your virtual environment
3. Run `pip3 install -r requirements.txt` to get the dependencies required for this application
4. Run `uvicorn main:app` to run the application locally

# Stack: FastAPI & Chameleon
This application utilizes FastAPI (https://fastapi.tiangolo.com/) as a webframework with Chameleon for templating

# Deployed on Heroku
Visit https://lit-earth-11903.herokuapp.com/

# Nice features to consider adding
* Started the basic pieces for getting a user account structure to allow sign in and register
* Calls are made asynchronously but the page waits to load, would like to have the element state that things are loading until requests are completed
* Would love to add search functionality to find and select from a list of option

# Testing the application
The tests are located in the `/tests` folder and the testing config file is `pytest.ini` which should all run by using `pytest`

# Threading vs Asyncio
My understanding when I started this project was that concurrency was achieved either through threading or async/await functionality to avoid the service waiting around. While this is true it's only scratching the surface. In researching further, it's true that "threading" doesn't use multiple cores on the processor (see quote below). So I decided to utilize AsyncIO for the web app as it was a more comfortable process and build a separate service for testing purposes only at this time that utilized "threading".

By the end of the project, I found threading to be a bit faster (probably due to the way I implemented asyncio) so I set the city_service.py to utilize threading rather than asyncio.

"Now let’s talk about the simultaneous part of that definition. You have to be a little careful because, when you get down to the details, only multiprocessing actually runs these trains of thought at literally the same time. **Threading and asyncio both run on a single processor and therefore only run one at a time.** They just cleverly find ways to take turns to speed up the overall process. Even though they don’t run different trains of thought simultaneously, we still call this concurrency." - Jim Anderson

Anderson, J. (n.d.). Speed Up Your Python Program With Concurrency. Retrieved April 09, 2022, from https://realpython.com/python-concurrency 
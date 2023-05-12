# DolarBot
## Summarize
Hablar de que se trata el bot, y que problematica viene a resolver

---
## Installation and set up (Linux, MacOS)
To install all the packages you will need run the followings commands in you terminal
>you need *pipenv* and *pyenv* to install and run the app
```
$ pipenv --python 3.10
$ pipenv shell
(venv)$ pip install -r requirements.txt  
```
To run the app you will have set the **DISCORD_TOKEN** environmental variable into the *.env* file
```
DISCORD_TOKEN="TOKEN"
```
---
## Usage
Run this command in your terminal to run the project 
```
(venv)$ python src/main.py
```
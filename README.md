# WebServer.py

## About

Simple implementation of a Web Server behaviour using sockets

## Technologies

- Python

## Setup

### Requirements
To run and edit this project locally, certify that you have installed the following programs:

- Python 3.8
- A code editor

After that, you'll need to clone this repo:

```
git clone https://github.com/LBeghini/TCP-Chat.git
``` 

## Usage

To run this project, you'll only need two files:

- index.html
- WebServer.py

From ```cmd```, go to the folder where you installed those programs.

Then, run the server:
```
python WebServer.py
```
It will be listening on [localhost:6789](http://localhost:6789)
You can access it through your browser.

To request the ```index.html``` page, access [localhost:6789/index.html](http://localhost:6789).

> Any other requests return a 404 page template

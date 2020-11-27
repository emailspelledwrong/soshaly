# FlaPyDoNG
A Flask/Python/Docker/Nginx/Gunicorn project template

Technologies-at-Large: Flask Blueprint, Jinja, Docker-Compose, JavaScript, HTML, CSS

# How to Deploy/Start the Project
- Clone it on your Linux box or WSL2
- Install Docker
- Inside the main project folder, issue this command:
   docker-compose up -d --build  
That will use the docker-compose file to fire up the containers and their network, but let them run in the background.
- Hit http://localhost

# Raison d'Etre
I wanted a project template that I could copy and use to get Dockerized Flask/Python projects off the ground quickly.  Since this was my first time using most of these technologies, I also learned a lot about each of them, in the process of building it.

# Docker
The project template is deployed as two separate Docker containers, spun up using a docker-compose file.  

Container "nginx" holds the nginx reverse-proxy.  The job of this container is to expose ports 80 & 443 (no cert yet) on localhost (127.0.0.1), and pass requests to the "Frontend" container. 

The "Frontend" container generates & serves the root web page, and the API web page back to the "nginx" container.

The network that the two containers share is called "grapevine".

# Nginx Container 
This container is built & configured by the docker-compose.yml and the default.conf files. It causes ports 80 & 443 to be exposed on localhost.  (You'll have to generate your own SSL Certificate).

Nginx is configured to be a reverse-proxy that accepts requests the browser, and passes them to the Frontend container, on port 8000 via their private network, grapevine.

# Frontend Container
This container is loaded using Gunicorn (I may switch this to uwsgi at some point, but I couldn't get it to work right away).  It's bound to port 8000 on the private container network.

Flask & Jinja do the heavy-lifting here.  A little bit of Python and HTML make it all go.  Bootstrap is waiting in the wings, but it's not called upon to do anything yet.

# Credits
Special thanks to the following people/organizations, without whose help I would not have gotten to this point:

- Robert K. Fewster
- Julian Nash (https://pythonise.com, https://www.youtube.com/channel/UC5_oFcBFlawLcFCBmU7oNZA)
- AwesomeOpenSource.com (https://www.youtube.com/c/AwesomeOpenSource/)
- https://realpython.com
- https://pythonspeed.com
- https://flask.palletsprojects.com
- nginx.org
- docs.docker.com
- https://hub.docker.com/u/tiangolo
- Many user posts at StackOverflow.com
- GitHub

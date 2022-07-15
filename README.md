# Docker-Practice

Docker Practice to maintain and run full stack app in Docker

## To Build /W Tags:

`docker build -t dockerpractice -f .\Dockerfile-Multi . --target primary` <br/>
`docker build -t dockerpractice:debug -f .\Dockerfile-Multi . --target debugger`

## To Run:

`docker run -d -p 5678:5678 -p 5000:5000 dockerpractice backend` <br/>
`docker run -d -p 5678:5678 -p 5000:5000 dockerpractice:debug backend`

## Changes
DockerFile <br/>
Docker-Compose <br/>
Launch.json <br/>

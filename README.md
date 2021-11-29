# Chainlink Iris

## Overview
Chainlink Iris is a no code tool that will allow people to use computer vision to create custom, video based data feeds to be read by chainlink in smartcontracts.

&nbsp;
## Installation and dependencies
To run the application locally, you will need Docker and Docker Compose installed on your computer. If you don't have these already installed, I recommend installing Docker Desktop, which includes both Docker and Docker Compose.

Install Docker Desktop: https://docs.docker.com/get-docker/

## Running the application
Navigate to the root directory of the project at the command line and run this command: 

` docker-compose up `

The server will take a few minutes to build and start the first time you run it. Once its running, you should be able to view it in a browser at http://localhost:3000/ 

&nbsp;
## Problem it solves
All off chain data fed to chainlink must come from an API of some sort. Not everyone has access to hardware/people that are able to convert data about real life events into digital representation.  

## How it works
1. Register an event
2. Set a data policy for that event
3. Place a time authenticated marker (see below) in the field of view
4. Anyone can upload video of the event 
5. Computer Vision analyzes the video and extracts useful JSON data 
6. JSON data is made available to be queried via chainlink in smart contracts

## Use cases
- Smaller sports events that don't have their scores entered into common feeds
- Use cases with vehicles (self driving)
- Use cases with security systems (insurance)


## Time Authentication Markers
Time authentication markers are basic graphics that represent a point in time. Every second a new one will be shown, in an order that is unknown to the public. Video streams must include the markers in the correct order for the data from the video to be used.

![Alt text](time_marker_example.png?raw=true "Time Authentication Marker")

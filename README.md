# Chainlink Iris

## Overview
Chainlink Iris is a no code tool that will allow people to use computer vision to create custom, video based data feeds to be read by chainlink in smartcontracts.

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
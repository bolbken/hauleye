# Haul Eye

# Stream Cam

## Purpose
A camera node that supplies a low-latency stream to the master server node.

## Goals

1. The architecture should be naive to how many/ or which rpi's are streaming.

1. The rpi's should require setup to connect with the master node, then the master
node should keep the registered streamers and supply them to the client

## Architecture and Networking

The stream cams will be cabable of two modes:

2. stream:  The trailer is in motion and the driver uses a low-latency stream feed in the car to assist driving

2. secure:  The trailer is **not** in motion and the cameras implement a distributed security system powered by MotionEye

To acheive switching of these modes, the stream cams will supply a simple set of API endpoints to switch the modes between

All communication between master and slave stream cams nodes will be done within the docker swarm networking.
This could be changed... but appears to be more secure at first glance.  The only exposed ports should be on any node in the swarm and direct to the web app running on the master node, ports 443.

### Stream Mode

Activated by an authorized request to the **/stream** restapi endpoint.

Initiates a python script that runs __indefinitely__ on each stream cam node which trasmits a websocket connection of the video stream of that node over the docker swarm network.

The master node ingests this websocket data and displays it in a UI visible to an authenticated user.

### Secure Mode







## Install picamera onto a cam node.

```bash
sudo apt-get update
sudo apt-get install python-picamera python3-picamera
```
